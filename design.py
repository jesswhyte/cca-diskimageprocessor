# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design.ui'
#
# Created: Thu Sep  8 12:08:25 2016
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(582, 669)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout.addWidget(self.label_2)
        self.source1 = QtGui.QLineEdit(self.centralwidget)
        self.source1.setObjectName(_fromUtf8("source1"))
        self.verticalLayout.addWidget(self.source1)
        self.source1btn = QtGui.QPushButton(self.centralwidget)
        self.source1btn.setObjectName(_fromUtf8("source1btn"))
        self.verticalLayout.addWidget(self.source1btn)
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.verticalLayout.addWidget(self.label_3)
        self.destination1 = QtGui.QLineEdit(self.centralwidget)
        self.destination1.setObjectName(_fromUtf8("destination1"))
        self.verticalLayout.addWidget(self.destination1)
        self.destination1btn = QtGui.QPushButton(self.centralwidget)
        self.destination1btn.setObjectName(_fromUtf8("destination1btn"))
        self.verticalLayout.addWidget(self.destination1btn)
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.label)
        self.checkBox = QtGui.QCheckBox(self.centralwidget)
        self.checkBox.setObjectName(_fromUtf8("checkBox"))
        self.verticalLayout.addWidget(self.checkBox)
        self.checkBox_2 = QtGui.QCheckBox(self.centralwidget)
        self.checkBox_2.setObjectName(_fromUtf8("checkBox_2"))
        self.verticalLayout.addWidget(self.checkBox_2)
        self.checkBox_3 = QtGui.QCheckBox(self.centralwidget)
        self.checkBox_3.setObjectName(_fromUtf8("checkBox_3"))
        self.verticalLayout.addWidget(self.checkBox_3)
        self.label_7 = QtGui.QLabel(self.centralwidget)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.verticalLayout.addWidget(self.label_7)
        self.textEdit = QtGui.QTextEdit(self.centralwidget)
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.verticalLayout.addWidget(self.textEdit)
        self.label_4 = QtGui.QLabel(self.centralwidget)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.verticalLayout.addWidget(self.label_4)
        self.lineEdit = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.verticalLayout.addWidget(self.lineEdit)
        self.process = QtGui.QPushButton(self.centralwidget)
        self.process.setObjectName(_fromUtf8("process"))
        self.verticalLayout.addWidget(self.process)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Disk Image Processor", None))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">Source</span></p></body></html>", None))
        self.source1.setPlaceholderText(_translate("MainWindow", "/path/to/source", None))
        self.source1btn.setText(_translate("MainWindow", "Browse", None))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">Destination</span></p></body></html>", None))
        self.destination1.setPlaceholderText(_translate("MainWindow", "/path/to/destination", None))
        self.destination1btn.setText(_translate("MainWindow", "Browse", None))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">Options</span></p></body></html>", None))
        self.checkBox.setText(_translate("MainWindow", "Bag SIPs", None))
        self.checkBox_2.setText(_translate("MainWindow", "Export all files (not only allocated)", None))
        self.checkBox_3.setText(_translate("MainWindow", "Run bulk_extractor", None))
        self.label_7.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">Detailed output</span></p></body></html>", None))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">Status</span></p></body></html>", None))
        self.process.setText(_translate("MainWindow", "Process disk images", None))

