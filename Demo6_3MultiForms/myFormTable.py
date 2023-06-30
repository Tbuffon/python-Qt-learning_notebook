import sys

from PyQt5.QtWidgets import  (QApplication, QMainWindow,
                     QLabel,QAbstractItemView,QDialog)

from PyQt5.QtCore import  pyqtSlot, Qt, QItemSelectionModel

from PyQt5.QtGui import QStandardItemModel

from ui_QWFormTable import Ui_QWFormTable

from myDialogSize import QmyDialogSize

from myDialogHeaders import QmyDialogHeaders

class QmyFormTable(QMainWindow):

   def __init__(self, parent=None):
      super().__init__(parent)    #调用父类构造函数，创建窗体
      self.ui=Ui_QWFormTable()    #创建UI对象
      self.ui.setupUi(self)       #构造UI界面
      
      self.__digSetHeaders = None  #表头设置对话框
      self.setAutoFillBackground(True)  #设置窗体自动填充背景
      self.ui.tableView.setAlternatingRowColors(True)  #设置交替行颜色
   ## 构建 Model/View
      self.itemModel = QStandardItemModel(10, 5, self)  #创建标准ItemModel
      self.selectionModel = QItemSelectionModel(self.itemModel)  #创建选择模型
      self.ui.tableView.setModel(self.itemModel)  #设置数据模型
      self.ui.tableView.setSelectionModel(self.selectionModel)  #设置选择模型

        
   def __del__(self): ##析构函数
      print("QmyFormTable 对象被删除了")

##  ==============自定义功能函数============

        
##  ==========由connectSlotsByName() 自动连接的槽函数==================        
   @pyqtSlot()    ##设置表格大小
   def on_actSetSize_triggered(self): 
      digTableSize = QmyDialogSize()  #局部变量，构件式不能传递self
      digTableSize.setIniSize(self.itemModel.rowCount(), self.itemModel.columnCount())
      ret = digTableSize.exec()  #以模态方式显示对话框
      if ret == QDialog.Accepted:  #判断对话框的返回值
         rows, cols = digTableSize.getTableSize()  #获取对话框中的表格大小
         self.itemModel.setRowCount(rows)  #设置表格行数
         self.itemModel.setColumnCount(cols)  #设置表格列数


   @pyqtSlot()    ##设置表头标题
   def on_actSetHeader_triggered(self):  
      if self.__digSetHeaders == None:
         self.__digSetHeaders = QmyDialogHeaders(self)  #创建对话框
      count = len(self.__digSetHeaders.headerList())  #获取表头个数
      if count != self.itemModel.columnCount():
         strList = []
         for i in range(self.itemModel.columnCount()):
            text = str(self.itemModel.headerData(i, Qt.Horizontal, Qt.DisplayRole)) #获取表头标题
            strList.append(text)
         self.__digSetHeaders.setHeaderList(strList)  #设置表头标题
      ret = self.__digSetHeaders.exec()  #以模态方式显示对话框
      if ret == QDialog.Accepted:  #判断对话框的返回值
         strList2 = self.__digSetHeaders.headerList()  #获取对话框中的表头标题
         self.itemModel.setHorizontalHeaderLabels(strList2)  #设置表头标题
        
##  =============自定义槽函数===============================        
        
   
##  ============窗体测试程序 ================================
if  __name__ == "__main__":
   app = QApplication(sys.argv)
   form=QmyFormTable()
   form.show()
   sys.exit(app.exec_())
