import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget, QMessageBox, QMenuBar, QMenu

class BMICalculator(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("BMI Calculator")
        self.setGeometry(500, 200, 300, 300)
        
        self.initUI()
        self.create_menu()
    
    def initUI(self):
        layout = QVBoxLayout()
        
        self.weight_label = QLabel("Enter Weight (kg):")
        self.weight_input = QLineEdit()
        layout.addWidget(self.weight_label)
        layout.addWidget(self.weight_input)
        
        self.height_label = QLabel("Enter Height (cm):")
        self.height_input = QLineEdit()
        layout.addWidget(self.height_label)
        layout.addWidget(self.height_input)
        
        self.calc_button = QPushButton("Calculate BMI")
        self.calc_button.clicked.connect(self.calculate_bmi)
        layout.addWidget(self.calc_button)
        
        self.result_label = QLabel("BMI: ")
        layout.addWidget(self.result_label)
        
        self.status_label = QLabel("Status: ")
        layout.addWidget(self.status_label)
        
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)
    
    def create_menu(self):
        menubar = self.menuBar()
        file_menu = menubar.addMenu("File")
        help_menu = menubar.addMenu("Help")
        
        exit_action = file_menu.addAction("Exit")
        exit_action.triggered.connect(self.close)
        
        clear_action = file_menu.addAction("Clear")
        clear_action.triggered.connect(self.clear_fields)
        
        help_action = help_menu.addAction("How to use")
        help_action.triggered.connect(self.show_help)
    
    def calculate_bmi(self):
        try:
            weight = float(self.weight_input.text())
            height = float(self.height_input.text())
            
            if height <= 0:
                raise ValueError("Height must be greater than zero.")
            
            pre_bmi = weight / ((height/100) ** 2)
            bmi = round(pre_bmi,2)
            self.result_label.setText(f"BMI: {bmi:.2f}")
            self.status_label.setText(f"Status: {self.get_bmi_status(bmi)}")
        except ValueError:
            QMessageBox.warning(self, "Input Error", "Please enter valid numeric values for weight and height.")
    
    def get_bmi_status(self, bmi):
        if bmi < 18.5:
            return "Underweight"
        elif 18.5 <= bmi < 25:
            return "Normal"
        elif 25 <= bmi < 30:
            return "Overweight"
        else:
            return "Obese"
    
    def clear_fields(self):
        self.weight_input.clear()
        self.height_input.clear()
        self.result_label.setText("BMI: ")
        self.status_label.setText("Status: ")
    
    def show_help(self):
        QMessageBox.information(self, "How to Use", "Enter your weight in kg and height in meters, then click 'Calculate BMI' to see your result.")

