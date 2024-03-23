import sys
import psutil
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QVBoxLayout, QWidget, QComboBox
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import usb.core

class PerformanceMonitor(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Performance Monitor")
        self.setGeometry(100, 100, 800, 600)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        layout = QVBoxLayout()

        self.device_combo = QComboBox()
        self.device_combo.setFixedSize(200, 20)  # 가로 길이 100, 세로 길이 20
        self.populate_device_list()
        layout.addWidget(self.device_combo)

        self.app_combo = QComboBox()
        self.app_combo.setFixedSize(200, 20)  # 가로 길이 100, 세로 길이 20
        self.app_combo.addItems(["App 1", "App 2", "App 3"])
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
        layout.addWidget(self.canvas)

        self.central_widget.setLayout(layout)

        self.cpu_label = QLabel()
        layout.addWidget(self.cpu_label)

        self.memory_label = QLabel()
        layout.addWidget(self.memory_label)

        self.power_label = QLabel()
        layout.addWidget(self.power_label)

        self.network_label = QLabel()
        layout.addWidget(self.network_label)

        self.rex_label = QLabel()
        layout.addWidget(self.rex_label)

        self.fps_label = QLabel()
        layout.addWidget(self.fps_label)

        self.anim = None

    def populate_device_list(self):
        devices = usb.core.find(find_all=True)
        for device in devices:
            manufacturer = usb.util.get_string(device, device.iManufacturer)
            product = usb.util.get_string(device, device.iProduct)
            device_name = f"{manufacturer} {product}"
            self.device_combo.addItem(device_name)

    def start_test(self):
        self.anim = animation.FuncAnimation(self.canvas.figure, self.update_graph, interval=1000)
        # Start monitoring performance metrics here

    def stop_test(self):
        if self.anim:
            self.anim.event_source.stop()
        # Stop monitoring performance metrics here

    def update_graph(self, i):
        # Update performance metrics and draw the graph here
        cpu_percent = psutil.cpu_percent()
        memory_percent = psutil.virtual_memory().percent
        power_usage = 0  # Dummy value, need to implement
        network_status = "Good"  # Dummy value, need to implement
        rex_detection = "None"  # Dummy value, need to implement
        fps = 60  # Dummy value, need to implement

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
    sys.exit(app.exec_())