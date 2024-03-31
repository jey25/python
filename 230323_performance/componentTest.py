import subprocess
import sys
import re
import os
from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QComboBox, QPushButton

class USBInfoApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        
        # CPU usage variables
        self.prev_cpu_time = 0
        self.prev_cpu_idle = 0

    def initUI(self):
        self.setWindowTitle('USB Device Info')
        self.setGeometry(100, 100, 400, 200)

        layout = QVBoxLayout()

        # Label to display USB device info
        self.device_label = QLabel('No USB device connected')
        layout.addWidget(self.device_label)

        # Start button
        self.start_button = QPushButton('Start Measurement')
        self.start_button.clicked.connect(self.start_measurement)
        layout.addWidget(self.start_button)

        # ComboBox for connected devices
        self.device_combobox = QComboBox()
        layout.addWidget(self.device_combobox)

        # ComboBox for installed apps
        self.app_combobox = QComboBox()
        layout.addWidget(self.app_combobox)

        # Label to display CPU usage
        self.cpu_label = QLabel('')
        layout.addWidget(self.cpu_label)

        # Label to display memory usage
        self.memory_label = QLabel('')
        layout.addWidget(self.memory_label)

        # Label to display FPS
        self.fps_label = QLabel('')
        layout.addWidget(self.fps_label)

        # Label to display network usage
        self.network_label = QLabel('')
        layout.addWidget(self.network_label)
        
        # Label to display battery status
        self.battery_label = QLabel('')
        layout.addWidget(self.battery_label)
        
        # Label to display temperature
        self.temperature_label = QLabel('')
        layout.addWidget(self.temperature_label)

        self.setLayout(layout)

        # QTimer for updating CPU usage, memory usage, FPS, and network usage
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_info)
        
        # Set measurement status
        self.is_measuring = False
        
        # Populate ComboBoxes
        self.populate_devices()

    def populate_devices(self):
        try:
            result = subprocess.run(['adb', 'devices'], capture_output=True, text=True)
            output = result.stdout
            if "List of devices attached" in output:
                # Extract device information from the output
                devices = [line.split('\t')[0] for line in output.splitlines()[1:] if line.strip() != '']
                self.device_combobox.addItems(devices)
                self.device_label.setText(f'USB devices found: {len(devices)}')
            else:
                self.device_label.setText('No USB devices found')
        except FileNotFoundError:
            self.device_label.setText('ADB not found')

        try:
            result = subprocess.run(['adb', 'shell', 'pm', 'list', 'packages'], capture_output=True, text=True)
            output = result.stdout
            if "com.tencent" in output:
                # Extract packages with com.tencent
                packages = [line.split(':')[1].strip() for line in output.splitlines() if "com.tencent" in line]
                self.app_combobox.clear()
                self.app_combobox.addItems(packages)
            else:
                self.app_combobox.clear()
                self.app_combobox.addItem("No apps found with com.tencent")
        except Exception as e:
            print("Error:", e)


    def start_measurement(self):
        if not self.is_measuring:
            self.is_measuring = True
            self.timer.start(1000)  # Start timer for updating every 1 second
            self.prev_cpu_time, self.prev_cpu_idle = self.get_cpu_time()


    def update_info(self):
        selected_device = self.device_combobox.currentText()
        selected_app = self.app_combobox.currentText()

        try:
            # Get PID of the selected app
            result_pid = subprocess.run(['adb', '-s', selected_device, 'shell', 'pidof', selected_app], capture_output=True, text=True)
            pid_output = result_pid.stdout.strip()
            if pid_output:
                pid = pid_output.split()[0]

                # Get CPU usage of the app with the PID
                cpu_time, cpu_idle = self.get_cpu_time(selected_device)
                cpu_usage = self.calculate_cpu_usage(cpu_time, cpu_idle)

                # Get memory usage of the app with PID
                result_mem = subprocess.run(['adb', '-s', selected_device, 'shell', 'cat', f'/proc/{pid}/status'], capture_output=True, text=True)
                mem_output = result_mem.stdout
                # Extract memory usage from the output
                mem_lines = mem_output.splitlines()
                for line in mem_lines:
                    if line.startswith('VmRSS:'):
                        memory_usage = line.split()[1]  # Memory usage is in the second column
                        break
                else:
                    memory_usage = 'N/A'

                # Get FPS of the app
                result_fps = subprocess.run(['adb', '-s', selected_device, 'shell', 'dumpsys', 'gfxinfo', selected_app], capture_output=True, text=True)
                fps_output = result_fps.stdout
                # Search for the FPS section and extract the value
                fps_section = re.search(r'Janky frames:\s+(\d+)\s+', fps_output)
                fps = fps_section.group(1) if fps_section else 'N/A'

                # Get network usage of the app
                result_netstat = subprocess.run(['adb', '-s', selected_device, 'shell', 'cat', '/proc/net/netstat'], capture_output=True, text=True)
                netstat_output = result_netstat.stdout
                # Parse network output to extract desired data (example only)
                # Adjust parsing logic according to the specific data you want to display
                network_data = "Example network data"

                # Get battery status
                battery_level = self.update_battery_status(selected_device)
                
                # Get temperature
                temperature = self.get_device_temperature(selected_device)

                # Display temperature
                self.temperature_label.setText(f'Temperature : {temperature} °C')

                # Display CPU, memory usage, FPS, and network usage
                self.cpu_label.setText(f'CPU : {cpu_usage}')
                self.memory_label.setText(f'Memory : {memory_usage} KB')
                self.fps_label.setText(f'FPS : {fps}')
                self.network_label.setText(f'Network : {network_data}')
                self.battery_label.setText(f'Battery Level: {battery_level}%')
            else:
                self.cpu_label.setText(f'CPU : PID not found')
                self.memory_label.setText(f'Memory : N/A')
                self.fps_label.setText(f'FPS : N/A')
                self.network_label.setText(f'Network : N/A')
                self.battery_label.setText(f'Battery Level: N/A')
        except Exception as e:
            print("Error:", e)


    def calculate_cpu_usage(self, cpu_time, cpu_idle):
        cpu_usage = ((cpu_time - self.prev_cpu_time) - (cpu_idle - self.prev_cpu_idle)) / (cpu_time - self.prev_cpu_time) * 100
        self.prev_cpu_time, self.prev_cpu_idle = cpu_time, cpu_idle
        return round(cpu_usage, 2)

    def get_device_temperature(self, selected_device):
        try:
            result = subprocess.run(['adb', '-s', selected_device, 'shell', 'cat', '/sys/class/thermal/thermal_zone0/temp'], capture_output=True, text=True)
            output = result.stdout.strip()
            if output:
                temperature = int(output) / 1000  # Convert millidegree Celsius to Celsius
                return temperature
            else:
                return 'N/A'
        except Exception as e:
            print("Error:", e)
            return 'N/A'


    def get_cpu_time(self, selected_device):
        result_cpu = subprocess.run(['adb', '-s', selected_device, 'shell', 'cat', '/proc/stat'], capture_output=True, text=True)
        cpu_output = result_cpu.stdout.strip().split('\n')
        cpu_line = [line for line in cpu_output if line.startswith('cpu ')][0].split()
        cpu_time = sum(map(int, cpu_line[1:]))
        cpu_idle = int(cpu_line[4])
        return cpu_time, cpu_idle

    def update_battery_status(self, selected_device):
        try:
            result = subprocess.run(['adb', '-s', selected_device, 'shell', 'dumpsys', 'battery'], capture_output=True, text=True)
            output = result.stdout
            # Extract battery level from output
            battery_level = None
            for line in output.splitlines():
                if 'level' in line:
                    battery_level = int(line.split(':')[1].strip())
                    break

            if battery_level is not None:
                return battery_level
            else:
                return 'N/A'
        except Exception as e:
            print("Error:", e)
            return 'N/A'

def main():
    app = QApplication(sys.argv)
    usb_app = USBInfoApp()
    usb_app.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()