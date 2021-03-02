from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

import temp_ui as ui

class Main(QMainWindow, ui.Ui_MainWindow):
    def __init__(self):
         super().__init__()
         self.setupUi(self)

if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = Main()
    window.show()
    sys.exit(app.exec_())
    
    
class Main(QMainWindow, ui.Ui_MainWindow):
# 初始化线程
def __init__(self):
    super().__init__()
    self.setupUi(self)
    self.pbstart.clicked.connect(self.StartProgram)
    self.pbstop.clicked.connect(self.StopProgram)

def run(self):
    global startprogram, temprev, datarev, waittime
    while True:
        if startprogram == True:
            DetectTemp()
            self.texttemprev.setText(str(temprev))
            DetectSet()
            self.texttempset.setText(str(datarev))
        sleep(waittime)

def StartProgram(self):
    global startprogram
    startprogram = True

def StopProgram(self):
    global startprogram
    startprogram = False
    
    
    
    
    
    
    
if uiini == True:
        # 打开一个UI界面
        import sys
        app = QtWidgets.QApplication(sys.argv)
        window = Main()
        window.show()
        sys.exit(app.exec_())
        uiini = False


    if uiini == True:
        # 打开一个UI界面
        import sys
        app = QtWidgets.QApplication(sys.argv)
        window = Main()
        window.show()
        sys.exit(app.exec_())
        uiini = False
