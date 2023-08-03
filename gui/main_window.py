from PyQt6.QtWidgets import QApplication, QWidget, QPushButton

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        # Здесь вы можете добавить элементы и логику для вашего GUI
        # Например, создать кнопки, поля ввода и т.д.
        # Ниже приведен пример, как вы можете добавить простое окно с кнопкой

        self.setWindowTitle('My GUI')
        self.setGeometry(100, 100, 300, 200)

        self.button = QPushButton('Click me', self)
        self.button.setGeometry(100, 100, 100, 50)

        self.button.clicked.connect(self.on_button_click)

    def on_button_click(self):
        print('Button clicked!')