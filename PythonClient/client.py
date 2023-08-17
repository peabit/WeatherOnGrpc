import grpc;

from CurrentWeatherInCityService_pb2_grpc import CurrentWeatherInCityServiceStub
from CurrentWeatherInCityService_pb2 import GetCurrentWeatherInCityRequest

from PyQt6.QtCore import Qt, QSize

from PyQt6.QtWidgets import (
    QApplication, 
    QWidget, 
    QMainWindow, 
    QPushButton, 
    QLineEdit, 
    QLabel, 
    QHBoxLayout,
    QVBoxLayout
)

import sys

def get_current_weather_in_city(city):
    credential = grpc.ssl_channel_credentials(open('localhost.pem', 'rb').read())

    channel = grpc.secure_channel('localhost:7168', credential)
    client = CurrentWeatherInCityServiceStub(channel)

    return client.Get(GetCurrentWeatherInCityRequest(city=city))

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("Curent weather in a city")
        self.setFixedSize(QSize(600, 250))

        self.city_input = QLineEdit() 

        refresh_btn = QPushButton("Refresh")
        refresh_btn.clicked.connect(self.refresh_btn_clickexd_handler)
        
        h_layout = QHBoxLayout()
        h_layout.addWidget(self.city_input)
        h_layout.addWidget(refresh_btn)

        self.weather_lbl = QLabel()

        weather_lbl_font = self.weather_lbl.font()
        weather_lbl_font.setPointSize(30)
        self.weather_lbl.setFont(weather_lbl_font)

        self.weather_lbl.setAlignment(Qt.AlignmentFlag.AlignHCenter)

        v_layout = QVBoxLayout()
        v_layout.addLayout(h_layout)
        v_layout.addWidget(self.weather_lbl)
        v_layout.setAlignment(Qt.AlignmentFlag.AlignVCenter)

        container = QWidget()
        container.setLayout(v_layout)
        container.setContentsMargins(30, 30, 30, 30)

        self.setCentralWidget(container)
    
    def refresh_btn_clickexd_handler(self):
        wetaher = get_current_weather_in_city(self.city_input.text())
        
        if bool(wetaher):
            self.weather_lbl.setText(f"{wetaher.temperature} ℃ - {wetaher.description}") 
        else:   
            self.weather_lbl.setText("Something went wrong...")

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()