# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'TSAnalyzer/TSWidgets/figure_batch.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(818, 817)
        self.gridLayout_2 = QtWidgets.QGridLayout(Dialog)
        self.gridLayout_2.setContentsMargins(3, 3, 3, 3)
        self.gridLayout_2.setSpacing(3)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.splitter = QtWidgets.QSplitter(Dialog)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.layoutWidget = QtWidgets.QWidget(self.splitter)
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.horizontalLayout_22 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_22.setObjectName("horizontalLayout_22")
        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setObjectName("label")
        self.horizontalLayout_22.addWidget(self.label)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_22.addItem(spacerItem)
        self.selectButton = QtWidgets.QPushButton(self.layoutWidget)
        self.selectButton.setText("")
        self.selectButton.setObjectName("selectButton")
        self.horizontalLayout_22.addWidget(self.selectButton)
        self.verticalLayout_7.addLayout(self.horizontalLayout_22)
        self.listWidget = QtWidgets.QListWidget(self.layoutWidget)
        self.listWidget.setObjectName("listWidget")
        self.verticalLayout_7.addWidget(self.listWidget)
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.deleteButton = QtWidgets.QPushButton(self.layoutWidget)
        self.deleteButton.setObjectName("deleteButton")
        self.horizontalLayout_15.addWidget(self.deleteButton)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_15.addItem(spacerItem1)
        self.countLabel = QtWidgets.QLabel(self.layoutWidget)
        self.countLabel.setObjectName("countLabel")
        self.horizontalLayout_15.addWidget(self.countLabel)
        self.verticalLayout_7.addLayout(self.horizontalLayout_15)
        self.layoutWidget1 = QtWidgets.QWidget(self.splitter)
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_4.setContentsMargins(3, 3, 3, 3)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.groupBox = QtWidgets.QGroupBox(self.layoutWidget1)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout.setContentsMargins(6, 6, 6, 6)
        self.gridLayout.setSpacing(6)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.comboBox = QtWidgets.QComboBox(self.groupBox)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.horizontalLayout.addWidget(self.comboBox)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 2)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)
        self.dpiBox = QtWidgets.QSpinBox(self.groupBox)
        self.dpiBox.setMinimum(100)
        self.dpiBox.setMaximum(999)
        self.dpiBox.setSingleStep(10)
        self.dpiBox.setProperty("value", 300)
        self.dpiBox.setObjectName("dpiBox")
        self.horizontalLayout_2.addWidget(self.dpiBox)
        self.gridLayout.addLayout(self.horizontalLayout_2, 1, 0, 1, 1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_3.addWidget(self.label_4)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem4)
        self.errorBarCheck = QtWidgets.QCheckBox(self.groupBox)
        self.errorBarCheck.setText("")
        self.errorBarCheck.setObjectName("errorBarCheck")
        self.horizontalLayout_3.addWidget(self.errorBarCheck)
        self.gridLayout.addLayout(self.horizontalLayout_3, 1, 1, 1, 1)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_6 = QtWidgets.QLabel(self.groupBox)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_2.addWidget(self.label_6)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.offsetsEdit = QtWidgets.QLineEdit(self.groupBox)
        self.offsetsEdit.setReadOnly(True)
        self.offsetsEdit.setObjectName("offsetsEdit")
        self.horizontalLayout_5.addWidget(self.offsetsEdit)
        self.offsetsButton = QtWidgets.QToolButton(self.groupBox)
        self.offsetsButton.setText("")
        self.offsetsButton.setObjectName("offsetsButton")
        self.horizontalLayout_5.addWidget(self.offsetsButton)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        self.gridLayout.addLayout(self.verticalLayout_2, 2, 0, 1, 2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        self.label_5.setObjectName("label_5")
        self.verticalLayout.addWidget(self.label_5)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.dirEdit = QtWidgets.QLineEdit(self.groupBox)
        self.dirEdit.setReadOnly(True)
        self.dirEdit.setObjectName("dirEdit")
        self.horizontalLayout_4.addWidget(self.dirEdit)
        self.saveDirButton = QtWidgets.QToolButton(self.groupBox)
        self.saveDirButton.setText("")
        self.saveDirButton.setObjectName("saveDirButton")
        self.horizontalLayout_4.addWidget(self.saveDirButton)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.gridLayout.addLayout(self.verticalLayout, 3, 0, 1, 2)
        self.verticalLayout_4.addWidget(self.groupBox)
        self.groupBox_2 = QtWidgets.QGroupBox(self.layoutWidget1)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_3.setContentsMargins(0, 9, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.imageLabel = QtWidgets.QLabel(self.groupBox_2)
        self.imageLabel.setMinimumSize(QtCore.QSize(500, 500))
        self.imageLabel.setMaximumSize(QtCore.QSize(500, 500))
        self.imageLabel.setText("")
        self.imageLabel.setObjectName("imageLabel")
        self.verticalLayout_3.addWidget(self.imageLabel)
        self.consoleEdit = QtWidgets.QPlainTextEdit(self.groupBox_2)
        self.consoleEdit.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.consoleEdit.setFrameShadow(QtWidgets.QFrame.Raised)
        self.consoleEdit.setLineWrapMode(QtWidgets.QPlainTextEdit.WidgetWidth)
        self.consoleEdit.setReadOnly(True)
        self.consoleEdit.setObjectName("consoleEdit")
        self.verticalLayout_3.addWidget(self.consoleEdit)
        self.verticalLayout_4.addWidget(self.groupBox_2)
        self.horizontalLayout_23 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_23.setObjectName("horizontalLayout_23")
        self.label_24 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_24.setObjectName("label_24")
        self.horizontalLayout_23.addWidget(self.label_24)
        self.progressBar = QtWidgets.QProgressBar(self.layoutWidget1)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.horizontalLayout_23.addWidget(self.progressBar)
        self.batchButton = QtWidgets.QPushButton(self.layoutWidget1)
        self.batchButton.setObjectName("batchButton")
        self.horizontalLayout_23.addWidget(self.batchButton)
        self.verticalLayout_4.addLayout(self.horizontalLayout_23)
        self.gridLayout_2.addWidget(self.splitter, 0, 0, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "TSAnalyzer Figures"))
        self.label.setText(_translate("Dialog", "Time Serie Files"))
        self.listWidget.setSortingEnabled(True)
        self.deleteButton.setText(_translate("Dialog", "Delete"))
        self.countLabel.setText(_translate("Dialog", "Total: 0"))
        self.groupBox.setTitle(_translate("Dialog", "Figure Settings"))
        self.label_2.setText(_translate("Dialog", "Figure Format"))
        self.comboBox.setItemText(0, _translate("Dialog", "png"))
        self.comboBox.setItemText(1, _translate("Dialog", "eps"))
        self.comboBox.setItemText(2, _translate("Dialog", "jpg"))
        self.comboBox.setItemText(3, _translate("Dialog", "pdf"))
        self.label_3.setText(_translate("Dialog", "Figure DPI"))
        self.label_4.setText(_translate("Dialog", "ErrorBar"))
        self.label_6.setText(_translate("Dialog", "Offsets"))
        self.label_5.setText(_translate("Dialog", "Save Directory"))
        self.groupBox_2.setTitle(_translate("Dialog", "Console"))
        self.label_24.setText(_translate("Dialog", "Progress"))
        self.batchButton.setText(_translate("Dialog", "Batch"))
