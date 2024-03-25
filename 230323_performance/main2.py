import sys
import subprocess
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QVBoxLayout, QWidget, QComboBox, QMessageBox
from PyQt5.QtCore import QTimer
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import serial.tools.list_ports
import re
import usb.core
import usb.util


class PerformanceMonitor(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Performance Monitor")
        self.setGeometry(100, 100, 800, 600)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        layout = QVBoxLayout()

        self.serial_combo = QComboBox()  # 수정된 부분
        self.serial_combo.setFixedSize(200, 20)
        layout.addWidget(self.serial_combo)

        self.serial_combo.currentIndexChanged.connect(self.populate_serial_ports)

        self.app_combo = QComboBox()
        self.app_combo.setFixedSize(200, 20)
        self.populate_installed_apps()  
        layout.addWidget(self.app_combo)

        self.start_button = QPushButton("Start Test")
        self.start_button.setFixedSize(100, 50)
        self.start_button.clicked.connect(self.start_test)
        layout.addWidget(self.start_button)

        self.stop_button = QPushButton("Stop Test")
        self.stop_button.clicked.connect(self.stop_test)
        self.stop_button.setFixedSize(100, 50)
        layout.addWidget(self.stop_button)

        self.canvas = FigureCanvas(plt.Figure())
        self.canvas.setStyleSheet("height: 400px;")  
        layout.addWidget(self.canvas)

        self.cpu_label = QLabel()
        layout.addWidget(self.cpu_label)

        self.memory_label = QLabel()
        layout.addWidget(self.memory_label)

        self.power_label = QLabel()
        layout.addWidget(self.power_label)

        self.network_label = QLabel()
        layout.addWidget(self.network_label)

        self.temperature_label = QLabel()
        layout.addWidget(self.temperature_label)

        self.rex_label = QLabel()
        layout.addWidget(self.rex_label)

        self.fps_label = QLabel()
        layout.addWidget(self.fps_label)

        self.central_widget.setLayout(layout)
        
        self.anim = None
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_data_and_labels)

    def get_usb_device_info(self):
        selected_device_index = self.serial_combo.currentIndex()
        selected_device = self.serial_combo.itemData(selected_device_index)
        return selected_device["vendor_id"], selected_device["product_id"]

    def find_usb_device(self, vendor_id, product_id):
        device = usb.core.find(idVendor=vendor_id, idProduct=product_id)
        if device is None:
            print("USB 디바이스를 찾을 수 없습니다.")
        return device

    def populate_serial_ports(self):
        self.serial_combo.clear()  # 콤보 박스를 초기화합니다.
        usb_devices = usb.core.find(find_all=True)  # 연결된 모든 USB 디바이스를 검색합니다.
        for device in usb_devices:
            # 각 USB 디바이스의 Vendor ID와 Product ID를 가져와서 콤보 박스에 추가합니다.
            vendor_id = device.idVendor
            product_id = device.idProduct
            self.serial_combo.addItem(f"{vendor_id}:{product_id}", {"vendor_id": vendor_id, "product_id": product_id})

    def get_serial_ports(self):
        serial_ports = [port.device for port in serial.tools.list_ports.comports()]
        return serial_ports

    def populate_installed_apps(self):  
        apps = self.get_installed_apps()
        if apps:
            self.app_combo.addItems(apps)

    def get_installed_apps(self):
        try:
            command = "adb shell pm list packages -3"  
            result = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT)
            packages = result.decode().splitlines()
            app_list = [package.split(":")[-1] for package in packages]
            return app_list
        except subprocess.CalledProcessError as e:
            print("Error:", e)
            return []

    def start_test(self):
        if not self.serial_combo.currentText() or not self.app_combo.currentText():
            self.show_warning_dialog("Please select a device and an app.")
            return
        try:
            self.anim = animation.FuncAnimation(self.canvas.figure, self.update_graph, interval=1000)
            self.timer.start(1000)  
        except subprocess.CalledProcessError as e:
            self.show_warning_dialog("Device is not connected.")
        except Exception as e:
            print("An error occurred:", e)

    def show_warning_dialog(self, message):
        warning_dialog = QMessageBox()
        warning_dialog.setIcon(QMessageBox.Warning)
        warning_dialog.setWindowTitle("Warning")
        warning_dialog.setText(message)
        warning_dialog.exec_()

    def stop_test(self):
        if self.anim:
            self.anim.event_source.stop()
            self.timer.stop()

    def update_data_and_labels(self):
        try:
            cpu_percent, memory_percent, power_usage, network_status, rex_detection, fps, temperature = self.update_data()

            self.cpu_label.setText(f"CPU Usage: {cpu_percent}%")
            self.memory_label.setText(f"Memory Usage: {memory_percent}%")
            self.power_label.setText(f"Power Usage: {power_usage}")
            self.network_label.setText(f"Network Status: {network_status}")
            self.temperature_label.setText(f"Temperature: {temperature}")
            self.rex_label.setText(f"Rex Detection: {rex_detection}")
            self.fps_label.setText(f"FPS: {fps}")
        except Exception as e:
            print("An error occurred:", e)

    def update_data(self):
        try:
            # 선택된 USB 디바이스의 Vendor ID와 Product ID를 가져옵니다.
            vendor_id, product_id = self.get_usb_device_info()
            
            # USB 디바이스를 찾습니다.
            device = self.find_usb_device(vendor_id, product_id)
            if device is None:
                return 0.0, 0.0, "", "", "", "", ""
            
            # 성능 데이터를 읽어옵니다. (예: 여기에서는 임의의 값을 사용합니다.)
            cpu_percent = 50.0
            memory_percent = 30.0
            power_usage = "20%"
            network_status = "Connected"
            rex_detection = "Not detected"
            fps = "60"
            temperature = "40°C"

            return cpu_percent, memory_percent, power_usage, network_status, rex_detection, fps, temperature
        except Exception as e:
            print("An error occurred:", e)
            return 0.0, 0.0, "", "", "", "", ""

    def update_graph(self, i):
        try:
            device, cpu_command, memory_command, temperature_command, cpu_result, cpu_percent, memory_result = self.update_data()

            if not hasattr(self, 'ax'):
                self.ax = self.canvas.figure.subplots()
                self.ax.set_xlabel('Time (s)')
                self.ax.set_ylabel('Percentage (%)')
                self.ax.set_title('CPU and Memory Usage')
                self.cpu_data = []
                self.memory_data = []
                self.time_data = []
                self.line_cpu, = self.ax.plot([], [], label='CPU Usage')
                self.line_memory, = self.ax.plot([], [], label='Memory Usage')
                self.ax.legend()

            self.cpu_data.append(float(cpu_percent))
            self.memory_data.append(float(memory_result))

            self.time_data.append(len(self.cpu_data))

            self.line_cpu.set_data(self.time_data, self.cpu_data)
            self.line_memory.set_data(self.time_data, self.memory_data)

            self.ax.set_xlim(0, max(10, len(self.cpu_data)))

            self.canvas.draw()

        except Exception as e:
            print("An error occurred:", e)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    monitor = PerformanceMonitor()
    monitor.show()
    sys.exit(app.exec_())