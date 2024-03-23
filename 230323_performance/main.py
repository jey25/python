import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QVBoxLayout, QWidget, QComboBox
from PyQt5.QtCore import QTimer
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from PyQt5.QtWidgets import QMessageBox
import psutil
import random
import subprocess
import serial.tools.list_ports

class PerformanceMonitor(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Performance Monitor")
        self.setGeometry(100, 100, 800, 600)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        layout = QVBoxLayout()

        self.device_combo = QComboBox()
        self.device_combo.setFixedSize(200, 20)
        self.get_serial_ports()  # 이 부분에서 수정
        layout.addWidget(self.device_combo)

        self.app_combo = QComboBox()
        self.app_combo.setFixedSize(200, 20)
        self.populate_installed_apps()  # 수정된 부분
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
        self.canvas.setStyleSheet("height: 400px;")  # 그래프 위젯의 높이 설정
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
        self.timer = QTimer()  # 타이머 생성
        self.timer.timeout.connect(self.update_data)  # 타이머 시그널을 update_data 메서드에 연결
        self.timer.start(1000)  # 1초마다 타이머가 발생

    def populate_installed_apps(self):  # 수정된 부분
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

    def get_serial_ports(self):
        serial_ports = [port.device for port in serial.tools.list_ports.comports()]
        return serial_ports

    # def populate_device_list(self):
    #     wmi = win32com.client.GetObject("winmgmts:")
    #     devices = wmi.ExecQuery("SELECT * FROM Win32_PnPEntity WHERE Name LIKE '%(COM%'")
    #     for device in devices:
    #         self.device_combo.addItem(device.Name)

    def start_test(self):
        if not self.device_combo.currentText() or not self.app_combo.currentText():
            self.show_warning_dialog("Please select a device and an app.")
            return
        self.anim = animation.FuncAnimation(self.canvas.figure, self.update_graph, interval=1000)

    def show_warning_dialog(self, message):
        warning_dialog = QMessageBox()
        warning_dialog.setIcon(QMessageBox.Warning)
        warning_dialog.setWindowTitle("Warning")
        warning_dialog.setText(message)
        warning_dialog.exec_()

    def stop_test(self):
        if self.anim:
            self.anim.event_source.stop()

    def update_data(self):
        cpu_percent = 50  
        memory_percent = 60  
        power_usage = 0  
        network_status = "Good"  
        rex_detection = "None"  
        fps = 30  
        return cpu_percent, memory_percent, power_usage, network_status, rex_detection, fps

    def update_graph(self, i):
        cpu_percent, memory_percent, power_usage, network_status, rex_detection, fps = self.update_data()

        self.cpu_label.setText(f"CPU Usage: {cpu_percent}%")
        self.memory_label.setText(f"Memory Usage: {memory_percent}%")
        self.power_label.setText(f"Power Usage: {power_usage}")
        self.network_label.setText(f"Network Status: {network_status}")
        self.rex_label.setText(f"Rex Detection: {rex_detection}")
        self.fps_label.setText(f"FPS: {fps}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    monitor = PerformanceMonitor()
    monitor.show()
    serial_ports = monitor.get_serial_ports()  
    sys.exit(app.exec_())