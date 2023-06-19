import sys
from PyQt5 import QtWidgets
import ui_FormHello

app = QtWidgets.QApplication(sys.argv)
baseWidget = QtWidgets.QWidget()        #创建窗体的积累QWidget的实例

ui = ui_FormHello.Ui_FormHello()
ui.setupUi(baseWidget)          # 以baseWidget作为传递参数，创建完整窗体

baseWidget.show()
ui.LabHello.setText("Hello, 被程序修改")
sys.exit(app.exec_())