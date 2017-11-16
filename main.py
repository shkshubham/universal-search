from PyQt4 import QtGui
from PyQt4 import QtCore
import sys
import app


class MainApp(QtGui.QMainWindow, app.Ui_MainWindow):
    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self)
        self.setWindowFlags(self.windowFlags() | QtCore.Qt.WindowStaysOnTopHint)
        file = open("style.ini",'r')
        stylesheet = file.read()
        file.close()
        self.setStyleSheet(stylesheet)
def main():
    app = QtGui.QApplication(sys.argv)  # A new instance of QApplication
    form = MainApp()                 # We set the form to be our ExampleApp (design)
    form.show()                         # Show the form
    app.exec_()                         # and execute the app


if __name__ == '__main__':              # if we're running file directly and not importing it
    main()                 
