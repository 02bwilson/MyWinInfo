import winreg

from PyQt6.QtWidgets import QWidget, QGridLayout, QLabel, QMainWindow, QLineEdit
from PyQt6.QtCore import Qt

from RegistryManager import RegMan


class MWIWidget(QWidget):

    def __init__(self, parent: QMainWindow):
        """
        The __init__ function is called when the class is instantiated.
        It sets up the initial state of an object, and is required for all classes.
        The self parameter refers to the instance of a class being created.

        :param self: Refer to the object itself
        :param parent: QMainWindow: Pass the parent window to the class
        :return: A new instance of the class
        """
        super().__init__()

        self.gridLayout = None
        self.titleLabel = None
        self.parent = None
        self.regMan = None
        self.reqInfo = None

        self.parent = parent

        self.gridLayout = QGridLayout()
        self.setLayout(self.gridLayout)

        self.regMan = RegMan()

        self.reqInfo = self.readRegValues()

        self.setupGUI()


    def setupGUI(self):
        """
        The setupGUI function is used to create the GUI for this window.
        It creates a grid layout and adds all the widgets to it.


        :param self: Refer to the object itself
        """
        self.titleLabel = QLabel()
        self.titleLabel.setStyleSheet("font-size:24pt;")
        self.titleLabel.setText("MyWinInfo v" + self.parent._VERSION)
        self.gridLayout.addWidget(self.titleLabel, 0, 0, 1, 2, Qt.AlignmentFlag.AlignCenter | Qt.AlignmentFlag.AlignTop)

        print(type(list(self.reqInfo.keys())))
        keys = list(self.reqInfo.keys())
        for keyIndex in range(len(keys)):
            keyLabel = QLabel(keys[keyIndex])
            valueLineEdit = QLineEdit()
            valueLineEdit.setMinimumWidth(250)
            valueLineEdit.setText(self.reqInfo[keys[keyIndex]])
            valueLineEdit.setReadOnly(True)

            self.gridLayout.addWidget(keyLabel, keyIndex + 1, 0, Qt.AlignmentFlag.AlignCenter | Qt.AlignmentFlag.AlignTop)
            self.gridLayout.addWidget(valueLineEdit, keyIndex + 1, 1, Qt.AlignmentFlag.AlignCenter | Qt.AlignmentFlag.AlignTop)

    def readRegValues(self):
        """
        The readRegValues function is used to read the values of certain registry keys.
        The function takes no arguments and returns a dictionary containing the following:
            - Product Name (e.g., Windows 10 Pro)
            - Current Build (e.g., 17134)
            - Product Key (the key that was used to activate Windows on this machine)

        :param self: Reference the object that is calling the function
        :return: A dictionary with the values
        """
        self.regMan.setRegAccess(winreg.HKEY_LOCAL_MACHINE)
        self.regMan.setAccessKey(r"SOFTWARE\Microsoft\Windows NT\CurrentVersion")
        returnInfo = dict()

        returnInfo["Product Name"] = self.regMan.queryValue("ProductName")[0]
        returnInfo["Current Build"] = self.regMan.queryValue("CurrentBuild")[0]
        self.regMan.setAccessKey(r"SOFTWARE\Microsoft\Windows NT\CurrentVersion\SoftwareProtectionPlatform")
        returnInfo["Product Key"] = self.regMan.queryValue("BackupProductKeyDefault")[0]

        return returnInfo