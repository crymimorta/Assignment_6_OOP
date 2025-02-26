from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QApplication, QMainWindow, QLineEdit
import sys
from window import BMICalculator

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = BMICalculator()
    window.show()
    sys.exit(app.exec())
