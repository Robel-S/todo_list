import sys
from PyQt6.QtWidgets import QApplication, QWidget

class Widget(QWidget):
    def __init__(self):
        super().__init__()

def main():
    app = QApplication([])
    window = Widget()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
