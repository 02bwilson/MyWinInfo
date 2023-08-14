from PyQt6.QtWidgets import QMainWindow, QApplication

import qdarktheme

from Widget import MWIWidget

class MyWinInfo(QMainWindow):
    _VERSION = "1.1.0"

    def __init__(self):
        """
        The __init__ function is called when the class is instantiated.
        It sets up the window and its central widget, which in this case
        is a MWIWidget object.

        :param self: Refer to the current instance of a class
        :return: The object itself, which is assigned to the variable MyWinInfo
        """
        super().__init__()

        self.widget = None

        self.setWindowTitle("MyWinInfo v" + self._VERSION)

        self.setFixedSize(400, 400)

        qdarktheme.setup_theme('dark')

        self.widget = MWIWidget(self)
        self.setCentralWidget(self.widget)


if __name__ == "__main__":
    app = QApplication([])

    window = MyWinInfo()
    window.show()

    app.exec()