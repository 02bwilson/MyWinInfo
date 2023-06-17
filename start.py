from PyQt6.QtWidgets import QApplication

from MyWinInfo import MyWinInfo


if __name__ == "__main__":


    app = QApplication([])

    window = MyWinInfo()
    window.show()

    app.exec()