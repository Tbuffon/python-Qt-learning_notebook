## 多继承方法

import sys
from PyQt5.QtWidgets import QWidget, QApplication
from ui_FormHello import Ui_FormHello

class QmyWidget(QWidget, Ui_FormHello):
    def __init__(self, parent=None):
        super().__init__(parent) # 调用父类构造函数， 创建QWidget窗体
        # 多继承时，使用super()得到的是第一个基类，这里是QWidget
        # 所以执行这条语句后，self就是一个QWidget对象

        self.Lab = "多重继承的QmyWidget"    # 新定义的一个变量
        self.setupUi(self)      # self 是QWidget窗体，可作为参数传给setupUi()
        self.LabHello.setText(self.Lab)

if __name__ == "__main__":
    app = QApplication(sys.argv)    # 创建app
    myWidget = QmyWidget()
    myWidget.show()
    myWidget.btnClose.setText("不关闭了")
    sys.exit(app.exec_())

