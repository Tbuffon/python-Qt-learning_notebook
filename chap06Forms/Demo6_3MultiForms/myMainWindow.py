import sys

from PyQt5.QtWidgets import  QApplication, QMainWindow

from PyQt5.QtCore import  pyqtSlot, Qt

##from PyQt5.QtWidgets import  

from PyQt5.QtGui import QPainter, QPixmap

from ui_MainWindow import Ui_MainWindow

from myFormDoc import QmyFormDoc

from myFormTable import QmyFormTable

class QmyMainWindow(QMainWindow):
   def __init__(self, parent=None):
      super().__init__(parent)    #调用父类构造函数，创建窗体
      self.ui=Ui_MainWindow()     #创建UI对象
      self.ui.setupUi(self)       #构造UI界面
      self.ui.tabWidget.setVisible(False)  #隐藏tabWidget
      self.ui.tabWidget.clear()   #清除tabWidget中的所有页面
      self.ui.tabWidget.setTabsClosable(True)  #设置tabWidget中的页面可关闭
      self.ui.tabWidget.setDocumentMode(True)  #设置tabWidget中的页面以文档模式显示

      self.setCentralWidget(self.ui.tabWidget)
      self.setWindowState(Qt.WindowMaximized)  #窗口最大化显示
      self.setAutoFillBackground(True)  #设置窗体自动填充背景
      self.__pic = QPixmap("seal.jpg")  #载入背景图片到内存，提高绘制速度


##  ==============自定义功能函数============

##  =============event事件处理函数============
   def paintEvent(self,event):
      painter = QPainter(self) #创建QPainter对象
      painter.drawPixmap(0, self.ui.mainToolBar.height(), self.width(),
      self.height()-self.ui.mainToolBar.height()-self.ui.statusBar.height(), self.__pic) #绘制背景图片
      super().paintEvent(event)
      
        
##  ==========由connectSlotsByName() 自动连接的槽函数==================        
   @pyqtSlot()    ## "嵌入式Widget"
   def on_actWidgetInsite_triggered(self):
      formDoc = QmyFormDoc(self)  #创建窗体
      formDoc.setAttribute(Qt.WA_DeleteOnClose)  #关闭时自动删除
      formDoc.docFileChanged.connect(self.do_docFileChanged)  #连接信号
      title = "Doc %d" % (self.ui.tabWidget.count())  #设置窗体标题
      curIndex = self.ui.tabWidget.addTab(formDoc, title)  #添加窗体到tabWidget
      self.ui.tabWidget.setCurrentIndex(curIndex)  #设置当前窗体
      self.ui.tabWidget.setVisible(True)  #显示tabWidget



   @pyqtSlot()    ##独立Widget窗口
   def on_actWidget_triggered(self):
      formDoc = QmyFormDoc(self)  #创建窗体
      formDoc.setAttribute(Qt.WA_DeleteOnClose)  #关闭时自动删除
      formDoc.setWindowTitle("基于Qwindow的窗体，关闭时自动删除")
      formDoc.setWindowFlag(Qt.Window, True)  #设置窗体为独立窗口
      formDoc.setWindowOpacity(0.9) #设置窗体透明度
      formDoc.show()  #显示窗体


   @pyqtSlot()    ##"嵌入式MainWindow"
   def on_actWindowInsite_triggered(self):
      formTable = QmyFormTable(self)  #创建窗体
      formTable.setAttribute(Qt.WA_DeleteOnClose)  #关闭时自动删除
      title = "Table %d" % (self.ui.tabWidget.count())  #设置窗体标题
      curIndex = self.ui.tabWidget.addTab(formTable, title)  #添加窗体到tabWidget
      self.ui.tabWidget.setCurrentIndex(curIndex)  #设置当前窗体
      self.ui.tabWidget.setVisible(True)  #显示tabWidget


   @pyqtSlot()    ##"独立MainWindow窗口"
   def on_actWindow_triggered(self):
      formTable = QmyFormTable(self)  #创建窗体
      formTable.setAttribute(Qt.WA_DeleteOnClose)  #关闭时自动删除
      formTable.setWindowTitle("基于QMainWindow的窗体，关闭时自动删除")
      formTable.setWindowFlag(Qt.Window, True)  #设置窗体为独立窗口
      formTable.setWindowOpacity(0.9) #设置窗体透明度
      formTable.show()  #显示窗体


   def on_tabWidget_currentChanged(self,index):    ##tabWidget当前页面变化
      hasTabs = self.ui.tabWidget.count() > 0
      self.ui.tabWidget.setVisible(hasTabs)
   

   def on_tabWidget_tabCloseRequested(self,index):  ##分页关闭时关闭窗体
      if (index < 0):
         return
      aForm = self.ui.tabWidget.widget(index) #获取当前页面的窗体
      aForm.close()  #关闭窗体
        
    
##  =============自定义槽函数===============================        
   @pyqtSlot(str)
   def do_docFileChanged(self,shotFilename):   ##显示文件名
      index = self.ui.tabWidget.currentIndex()  #获取当前页面的索引
      self.ui.tabWidget.setTabText(index, shotFilename)  #设置当前页面的标题
       
   
##  ============窗体测试程序 ================================
if  __name__ == "__main__":
   app = QApplication(sys.argv)
   form=QmyMainWindow()
   form.show()
   sys.exit(app.exec_())
