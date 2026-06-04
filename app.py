from PySide6.QtWidgets import QApplication, QMainWindow

from ui_mainwindow import Ui_MainWindow

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.setup_connections()

    def setup_connections(self):
        pass

app = QApplication([])
window = MainWindow()
window.show()
app.exec()




