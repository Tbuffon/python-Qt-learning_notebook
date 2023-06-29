import sys

from PyQt5.QtWidgets import (QApplication, QMainWindow,QActionGroup,
                 QLabel, QProgressBar, QSpinBox, QFontComboBox)

from PyQt5.QtCore import  Qt, pyqtSlot

from PyQt5.QtGui import  QTextCharFormat, QFont

from ui_MainWindow import Ui_MainWindow

class QmyMainWindow(QMainWindow): 
   def __init__(self, parent=None):
      super().__init__(parent)    #调用父类构造函数，创建窗体
      self.ui=Ui_MainWindow()     #创建UI对象
      self.ui.setupUi(self)       #构造UI界面
      
      self.__buildUI()            #动态创建组件，添加到工具栏和状态栏
      self.__spinFontSize.valueChanged[int].connect(
         self.do_fontSize_Changed)     # 字体大小设置
      self.__comboFontName.currentIndexChanged[str].connect(
         self.do_fontName_Changed)     # 字体选择
      self.setCentralWidget(self.ui.textEdit)


##  ============自定义功能函数================================        
   def __buildUI(self):    ##窗体上动态添加组件
   ## 创建状态栏上的组件
      self.__LabFile = QLabel(self)   # QLabel组件显示信息
      self.__LabFile.setMinimumWidth(150)
      self.__LabFile.setText("文件名：")
      self.ui.statusBar.addWidget(self.__LabFile) #添加到状态栏
      
      self.__progressBar1 = QProgressBar(self)    #进度条
      self.__progressBar1.setMinimumWidth(200)
      self.__progressBar1.setMinimum(5)
      self.__progressBar1.setMaximum(50)
      sz = self.ui.textEdit.font().pointSize()  #获取字体大小
      self.__progressBar1.setValue(sz)          #设置进度条当前值
      self.ui.statusBar.addWidget(self.__progressBar1) #添加到状态栏

      self.__LabInfo = QLabel(self)   # QLabel组件显示字体名称
      self.__LabInfo.setText("选择字体名称：")
      self.ui.statusBar.addPermanentWidget(self.__LabInfo) #添加到状态栏

   ## 为actLang_CN和actLang_EN创建QActionGroup，互斥型选择
      actionGroup = QActionGroup(self)
      actionGroup.addAction(self.ui.actLang_CN)
      actionGroup.addAction(self.ui.actLang_EN)
      actionGroup.setExclusive(True)  #设置互斥
      self.ui.actLang_CN.setChecked(True)  #默认中文
   
   ## 创建工具栏上的组件
      self.__spinFontSize = QSpinBox(self)  #创建字体大小QSpinBox组件
      self.__spinFontSize.setMaximum(50)
      self.__spinFontSize.setMinimum(5)
      sz = self.ui.textEdit.font().pointSize()  #获取字体大小
      self.__spinFontSize.setValue(sz)          #设置当前值
      self.__spinFontSize.setMinimumWidth(50)
      self.ui.mainToolBar.addWidget(self.__spinFontSize) #添加到工具栏

      self.__comboFontName = QFontComboBox(self)  #创建字体选择QFontComboBox组件
      self.__comboFontName.setMinimumWidth(100)
      self.ui.mainToolBar.addWidget(self.__comboFontName) #添加到工具栏

      self.ui.mainToolBar.addSeparator()  #添加分隔条
      self.ui.mainToolBar.addAction(self.ui.actClose) #添加关闭动作



        
##  ===========由connectSlotsByName() 自动连接的槽函数=====================      
   @pyqtSlot(bool)   ##设置粗体 
   def on_actFont_Bold_triggered(self, checked):
      fmt = self.ui.textEdit.currentCharFormat()  #获取当前字符格式
      if checked == True:
         fmt.setFontWeight(QFont.Bold)            #设置为粗体
      else:
         fmt.setFontWeight(QFont.Normal)          #设置为正常
      self.ui.textEdit.mergeCurrentCharFormat(fmt) #合并格式      

   @pyqtSlot(bool)   ##设置斜体 
   def on_actFont_Italic_triggered(self,checked):    
      fmt = self.ui.textEdit.currentCharFormat()  #获取当前字符格式
      fmt.setFontItalic(checked)                  #设置斜体
      self.ui.textEdit.mergeCurrentCharFormat(fmt) #合并格式
        
   @pyqtSlot(bool)   ##设置下划线 
   def on_actFont_UnderLine_triggered(self,checked):  
      fmt = self.ui.textEdit.currentCharFormat()  #获取当前字符格式
      fmt.setFontUnderline(checked)               #设置下划线
      self.ui.textEdit.mergeCurrentCharFormat(fmt) #合并格式

   def on_textEdit_copyAvailable(self, avi):    ##文本框内容可copy
      self.ui.actEdit_Cut.setEnabled(avi)       #设置剪切动作可用
      self.ui.actEdit_Copy.setEnabled(avi)      #设置复制动作可用
      self.ui.actEdit_Paste.setEnabled(self.ui.textEdit.canPaste()) #设置粘贴动作可用
                                         
   def on_textEdit_selectionChanged(self):      ##文本选择内容发生变化
      fmt = self.ui.textEdit.currentCharFormat()  #获取当前字符格式
      self.ui.actFont_Bold.setChecked(fmt.font().bold())  #设置粗体按钮状态
      self.ui.actFont_Italic.setChecked(fmt.fontItalic()) #设置斜体按钮状态
      self.ui.actFont_UnderLine.setChecked(fmt.fontUnderline()) #设置下划线按钮状态

   def on_textEdit_customContextMenuRequested(self,pos):  ##标准右键菜单
      popMenu = self.ui.textEdit.createStandardContextMenu()  #获取标准右键菜单
      popMenu.exec(pos)  #显示快捷菜单

   @pyqtSlot(bool)   ##设置工具栏按钮样式 
   def on_actSys_ToggleText_triggered(self,checked):  
      if (checked):
         st = Qt.ToolButtonTextUnderIcon  #工具栏按钮样式
      else:
         st = Qt.ToolButtonIconOnly
      self.ui.mainToolBar.setToolButtonStyle(st)  #设置工具栏按钮样式

   def on_actFile_New_triggered(self):     ##新建文件，不实现具体功能
      self.__LabFile.setText("新建文件")

   def on_actFile_Open_triggered(self):    ##打开文件，不实现具体功能
      self.__LabFile.setText("打开的文件")
        
   def on_actFile_Save_triggered(self):    ##保存文件，不实现具体功能
      self.__LabFile.setText("文件已保存")
        
##  =============自定义槽函数===============================        
   @pyqtSlot(int)    ##设置字体大小,关联 __spinFontSize
   def do_fontSize_Changed(self, fontSize):      
      fmt = self.ui.textEdit.currentCharFormat()  #获取当前字符格式
      fmt.setFontPointSize(fontSize)              #设置字体大小
      self.ui.textEdit.mergeCurrentCharFormat(fmt) #合并格式
      self.__progressBar1.setValue(fontSize)      #设置进度条当前值

   @pyqtSlot(str)    ##选择字体名称，关联__comboFontName
   def do_fontName_Changed(self, fontName):  
      fmt = self.ui.textEdit.currentCharFormat() #获取当前字符格式
      fmt.setFontFamily(fontName)                #设置字体名称
      self.ui.textEdit.mergeCurrentCharFormat(fmt) #合并格式
      self.__LabInfo.setText("字体名称：%s "%fontName) #状态栏显示字体名称
   
##  ===========窗体测试程序=================================        
if  __name__ == "__main__":        #用于当前窗体测试
   app = QApplication(sys.argv)    #创建GUI应用程序
   form=QmyMainWindow()            #创建窗体
   form.show()
   sys.exit(app.exec_())
