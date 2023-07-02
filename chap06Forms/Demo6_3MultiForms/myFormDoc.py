import sys,os  #codecs

from PyQt5.QtWidgets import  (QApplication, QWidget,QFileDialog,
                         QToolBar, QVBoxLayout,QFontDialog)

from PyQt5.QtCore import  pyqtSlot, pyqtSignal,Qt

from PyQt5.QtGui import QPalette,  QFont

from ui_QWFormDoc import Ui_QWFormDoc

class QmyFormDoc(QWidget):
   docFileChanged=pyqtSignal(str)  ##自定义信号，打开文件时发射

   def __init__(self, parent=None):
      super().__init__(parent)   #调用父类构造函数，创建窗体
      self.ui=Ui_QWFormDoc()     #创建UI对象
      self.ui.setupUi(self)      #构造UI界面
      self.__curFile=""          #当前文件名称
      self.__buildUI()           #构造工具栏
      self.setAutoFillBackground(True)  #设置窗体自动填充背景

        
   def __del__(self):   ##析构函数
      print("QmyFormDoc 对象被删除了")
   

   def __buildUI(self):    ##使用UI可视化设计的Actions创建工具栏
      locToolBar = QToolBar("文档", self)  #创建工具栏
      locToolBar.addAction(self.ui.actOpen)  #添加动作
      locToolBar.addAction(self.ui.actFont)
      locToolBar.addSeparator()  #添加分隔条
      locToolBar.addAction(self.ui.actCut)
      locToolBar.addAction(self.ui.actCopy)
      locToolBar.addAction(self.ui.actPaste)
      locToolBar.addAction(self.ui.actUndo)
      locToolBar.addAction(self.ui.actRedo)
      locToolBar.addSeparator()
      locToolBar.addAction(self.ui.actClose)
      locToolBar.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)  #设置工具栏按钮文本在图标旁边
      
      Layout=QVBoxLayout()  #创建布局管理器
      Layout.addWidget(locToolBar)  #添加工具栏
      Layout.addWidget(self.ui.plainTextEdit)  #添加编辑区
      Layout.setContentsMargins(2, 2, 2, 2)  #设置边距
      Layout.setSpacing(2)  #设置控件间的间距
      self.setLayout(Layout)  #设置窗体布局管理器

##  ==============自定义功能函数============
        
        
##  ==========由connectSlotsByName() 自动连接的槽函数==================        
   @pyqtSlot()    ##打开文件
   def on_actOpen_triggered(self): 
      curPath = os.getcwd()  #获取当前路径
      filename, flt = QFileDialog.getOpenFileName(self, "打开一个文件", curPath, "文本文件(*.cpp *.h *.py);;所有文件(*.*)")
      if filename == "":
         return
      self.__curFile = filename
      self.ui.plainTextEdit.clear()  #清空编辑区
      aFile = open(filename, 'r', encoding='UTF-8')  #以只读方式打开文件
      try:
         for eachLine in aFile:
            self.ui.plainTextEdit.appendPlainText(eachLine.strip())  #添加到编辑区
      finally:
         aFile.close()
      baseFilename = os.path.basename(filename)  #获取文件名
      self.setWindowTitle(baseFilename)  #设置窗口标题
      self.docFileChanged.emit(filename)  #发射信号，传递文件名

   @pyqtSlot()    ##设置字体
   def on_actFont_triggered(self):
      iniFont = self.ui.plainTextEdit.font()  #获取编辑区字体
      font, OK = QFontDialog.getFont(iniFont)  #弹出字体选择对话框
      if OK: #如果点击了OK按钮
         self.ui.plainTextEdit.setFont(font)  #设置编辑区字体

        
##  =============自定义槽函数===============================        
        
   
##  ============窗体测试程序 ================================
if  __name__ == "__main__":
   app = QApplication(sys.argv)
   form=QmyFormDoc()
   form.show()
   sys.exit(app.exec_())
