import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel
from PyQt6.QtGui import QFont

class Widget(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(700,300,1000, 600)
        
def main():
    app = QApplication([])
    window = Widget()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
