from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3


class Ui_MainWindow(object):

    # Insert Element to table
    def insert(self):

        name = self.name_input.text()
        phone = self.ph_input.text()   
        email = self.email_input.text()
        address = self.address_input.text()

        # Dictionary of the input field 
        input_text = {name: self.name_input, phone: self.ph_input, email: self.email_input, address: self.address_input}  

        
        if "" not in input_text:

            row_index = self.tableWidget.rowCount()
            self.tableWidget.insertRow(row_index)
          

            for i, key in enumerate(input_text):
                self.tableWidget.setItem(row_index, i, QtWidgets.QTableWidgetItem(key))
                input_text[key].setText("")

        else:
            d_Box = QtWidgets.QMessageBox()
            d_Box.setWindowTitle("Incomplete !!")
            d_Box.setText(f"Input is Incomplete")
            d_Box.addButton(QtWidgets.QPushButton("OK"), QtWidgets.QMessageBox.NoRole)
            d_Box.exec_()
                
    # Delete element from Table
    def remove(self):
        selected_indexes = self.tableWidget.selectedIndexes()

        # Collect unique row indices from selected indexes
        rows_to_remove = set(index.row() for index in selected_indexes)

        # Remove rows in reverse order to avoid index issues
        for row in sorted(rows_to_remove, reverse=True):
            self.tableWidget.removeRow(row)
      
    # Load Data  
    def load(self):
        conn = sqlite3.connect("demo.db")
        self.c = conn.cursor()
        result = self.c.execute("""SELECT * FROM demo_table""")

        self.tableWidget.setRowCount(0)

        for row_count, row_data in enumerate(result):
            self.tableWidget.insertRow(row_count)
            for col_count, col_data in enumerate(row_data):
                self.tableWidget.setItem(row_count, col_count, QtWidgets.QTableWidgetItem(str(col_data)))


    def setupUi(self, MainWindow):

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(687, 656)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.headder = QtWidgets.QFrame(self.centralwidget)
        self.headder.setGeometry(QtCore.QRect(20, 0, 641, 81))
        self.headder.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.headder.setFrameShadow(QtWidgets.QFrame.Raised)
        self.headder.setObjectName("headder")

        self.label = QtWidgets.QLabel(self.headder)
        self.label.setGeometry(QtCore.QRect(220, 20, 201, 41))
        font = QtGui.QFont()
        font.setFamily("Poor Richard")
        font.setPointSize(22)
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(20, 90, 651, 141))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")

        self.label_2 = QtWidgets.QLabel(self.frame_2)
        self.label_2.setGeometry(QtCore.QRect(30, 80, 101, 21))
        font = QtGui.QFont()
        font.setFamily("Poor Richard")
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")

        self.label_3 = QtWidgets.QLabel(self.frame_2)
        self.label_3.setGeometry(QtCore.QRect(70, 30, 81, 21))
        font = QtGui.QFont()
        font.setFamily("Poor Richard")
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")

        self.label_4 = QtWidgets.QLabel(self.frame_2)
        self.label_4.setGeometry(QtCore.QRect(400, 30, 51, 21))
        font = QtGui.QFont()
        font.setFamily("Poor Richard")
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")

        self.label_6 = QtWidgets.QLabel(self.frame_2)
        self.label_6.setGeometry(QtCore.QRect(390, 80, 71, 20))
        font = QtGui.QFont()
        font.setFamily("Poor Richard")
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")

        self.name_input = QtWidgets.QLineEdit(self.frame_2)
        self.name_input.setGeometry(QtCore.QRect(130, 30, 141, 21))
        self.name_input.setObjectName("name_input")

        self.ph_input = QtWidgets.QLineEdit(self.frame_2)
        self.ph_input.setGeometry(QtCore.QRect(130, 80, 141, 21))
        self.ph_input.setObjectName("ph_input")

        self.email_input = QtWidgets.QLineEdit(self.frame_2)
        self.email_input.setGeometry(QtCore.QRect(460, 30, 151, 21))
        self.email_input.setObjectName("email_input")

        self.address_input = QtWidgets.QLineEdit(self.frame_2)
        self.address_input.setGeometry(QtCore.QRect(460, 80, 141, 21))
        self.address_input.setObjectName("address_input")

        self.frame_3 = QtWidgets.QFrame(self.centralwidget)
        self.frame_3.setGeometry(QtCore.QRect(20, 240, 651, 61))
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")

        self.add = QtWidgets.QPushButton(self.frame_3, clicked = lambda: self.insert())
        self.add.setGeometry(QtCore.QRect(30, 20, 93, 28))
        self.add.setObjectName("add")

        self.clear = QtWidgets.QPushButton(self.frame_3, clicked = lambda: self.remove())
        self.clear.setGeometry(QtCore.QRect(160, 20, 93, 28))
        self.clear.setObjectName("delete")

        self.save = QtWidgets.QPushButton(self.frame_3)
        self.save.setGeometry(QtCore.QRect(280, 20, 93, 28))
        self.save.setObjectName("save")

        self.open = QtWidgets.QPushButton(self.frame_3)
        self.open.setGeometry(QtCore.QRect(410, 20, 93, 28))
        self.open.setObjectName("open")

        self.exit = QtWidgets.QPushButton(self.frame_3, clicked = lambda: exit())
        self.exit.setGeometry(QtCore.QRect(530, 20, 93, 28))
        self.exit.setObjectName("exit")

        self.frame_4 = QtWidgets.QFrame(self.centralwidget)
        self.frame_4.setGeometry(QtCore.QRect(20, 320, 651, 281))
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")

        self.tableWidget = QtWidgets.QTableWidget(self.frame_4)
        self.tableWidget.setGeometry(QtCore.QRect(0, 10, 651, 271))
        self.tableWidget.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.tableWidget.setObjectName("tableWidget")

        self.tableWidget.setColumnCount(4)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        self.tableWidget.verticalHeader().setStretchLastSection(False)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 687, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Contact Book"))
        self.label_2.setText(_translate("MainWindow", "Ph. Number :"))
        self.label_3.setText(_translate("MainWindow", "Name :"))
        self.label_4.setText(_translate("MainWindow", "Email. :"))
        self.label_6.setText(_translate("MainWindow", "Address :"))
        self.add.setText(_translate("MainWindow", "Add"))
        self.clear.setText(_translate("MainWindow", "Clear"))
        self.save.setText(_translate("MainWindow", "Save"))
        self.open.setText(_translate("MainWindow", "Open"))
        self.exit.setText(_translate("MainWindow", "Exit"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Name"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Ph. Number"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Email"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Address"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
