# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Paolo\Desktop\templateIter3.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
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

class Ui_SimpleButton(object):
    def setupUi(self, SimpleButton):
        SimpleButton.setObjectName(_fromUtf8("SimpleButton"))
        SimpleButton.resize(858, 701)
        self.verticalLayoutWidget_2 = QtGui.QWidget(SimpleButton)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(70, 450, 161, 181))
        self.verticalLayoutWidget_2.setObjectName(_fromUtf8("verticalLayoutWidget_2"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.CalibrateButton = QtGui.QPushButton(self.verticalLayoutWidget_2)
        self.CalibrateButton.setObjectName(_fromUtf8("CalibrateButton"))
        self.verticalLayout_2.addWidget(self.CalibrateButton)
        self.StartButton = QtGui.QPushButton(self.verticalLayoutWidget_2)
        self.StartButton.setObjectName(_fromUtf8("StartButton"))
        self.verticalLayout_2.addWidget(self.StartButton)
        self.StopButton = QtGui.QPushButton(self.verticalLayoutWidget_2)
        self.StopButton.setObjectName(_fromUtf8("StopButton"))
        self.verticalLayout_2.addWidget(self.StopButton)
        self.CancelButton = QtGui.QPushButton(self.verticalLayoutWidget_2)
        self.CancelButton.setObjectName(_fromUtf8("CancelButton"))
        self.verticalLayout_2.addWidget(self.CancelButton)
        self.BREEZETitle = QtGui.QLabel(SimpleButton)
        self.BREEZETitle.setGeometry(QtCore.QRect(340, 0, 211, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.BREEZETitle.setFont(font)
        self.BREEZETitle.setObjectName(_fromUtf8("BREEZETitle"))
        self.horizontalLayoutWidget_2 = QtGui.QWidget(SimpleButton)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(70, 70, 721, 84))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.horizontalLayoutWidget_2.setFont(font)
        self.horizontalLayoutWidget_2.setObjectName(_fromUtf8("horizontalLayoutWidget_2"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setSpacing(7)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.verticalLayout_5 = QtGui.QVBoxLayout()
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.PatientIDLabel = QtGui.QLabel(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.PatientIDLabel.setFont(font)
        self.PatientIDLabel.setObjectName(_fromUtf8("PatientIDLabel"))
        self.verticalLayout_5.addWidget(self.PatientIDLabel)
        self.FirstNameLabel = QtGui.QLabel(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.FirstNameLabel.setFont(font)
        self.FirstNameLabel.setObjectName(_fromUtf8("FirstNameLabel"))
        self.verticalLayout_5.addWidget(self.FirstNameLabel)
        self.LastNameLabel = QtGui.QLabel(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.LastNameLabel.setFont(font)
        self.LastNameLabel.setObjectName(_fromUtf8("LastNameLabel"))
        self.verticalLayout_5.addWidget(self.LastNameLabel)
        self.horizontalLayout_2.addLayout(self.verticalLayout_5)
        self.verticalLayout_7 = QtGui.QVBoxLayout()
        self.verticalLayout_7.setObjectName(_fromUtf8("verticalLayout_7"))
        self.PatientIDDisplay = QtGui.QLineEdit(self.horizontalLayoutWidget_2)
        self.PatientIDDisplay.setObjectName(_fromUtf8("PatientIDDisplay"))
        self.verticalLayout_7.addWidget(self.PatientIDDisplay)
        self.FirstNameDisplay = QtGui.QLineEdit(self.horizontalLayoutWidget_2)
        self.FirstNameDisplay.setObjectName(_fromUtf8("FirstNameDisplay"))
        self.verticalLayout_7.addWidget(self.FirstNameDisplay)
        self.LastNameDisplay = QtGui.QLineEdit(self.horizontalLayoutWidget_2)
        self.LastNameDisplay.setObjectName(_fromUtf8("LastNameDisplay"))
        self.verticalLayout_7.addWidget(self.LastNameDisplay)
        self.horizontalLayout_2.addLayout(self.verticalLayout_7)
        self.verticalLayout_6 = QtGui.QVBoxLayout()
        self.verticalLayout_6.setObjectName(_fromUtf8("verticalLayout_6"))
        self.GenderLabel = QtGui.QLabel(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.GenderLabel.setFont(font)
        self.GenderLabel.setObjectName(_fromUtf8("GenderLabel"))
        self.verticalLayout_6.addWidget(self.GenderLabel)
        self.SmokerLabel = QtGui.QLabel(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.SmokerLabel.setFont(font)
        self.SmokerLabel.setObjectName(_fromUtf8("SmokerLabel"))
        self.verticalLayout_6.addWidget(self.SmokerLabel)
        self.HeightLabel = QtGui.QLabel(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.HeightLabel.setFont(font)
        self.HeightLabel.setObjectName(_fromUtf8("HeightLabel"))
        self.verticalLayout_6.addWidget(self.HeightLabel)
        self.horizontalLayout_2.addLayout(self.verticalLayout_6)
        self.verticalLayout_8 = QtGui.QVBoxLayout()
        self.verticalLayout_8.setObjectName(_fromUtf8("verticalLayout_8"))
        self.GenderDisplay = QtGui.QLineEdit(self.horizontalLayoutWidget_2)
        self.GenderDisplay.setObjectName(_fromUtf8("GenderDisplay"))
        self.verticalLayout_8.addWidget(self.GenderDisplay)
        self.WeightDisplay = QtGui.QLineEdit(self.horizontalLayoutWidget_2)
        self.WeightDisplay.setObjectName(_fromUtf8("WeightDisplay"))
        self.verticalLayout_8.addWidget(self.WeightDisplay)
        self.HeightDisplay = QtGui.QLineEdit(self.horizontalLayoutWidget_2)
        self.HeightDisplay.setObjectName(_fromUtf8("HeightDisplay"))
        self.verticalLayout_8.addWidget(self.HeightDisplay)
        self.horizontalLayout_2.addLayout(self.verticalLayout_8)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.DOBLabel = QtGui.QLabel(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.DOBLabel.setFont(font)
        self.DOBLabel.setObjectName(_fromUtf8("DOBLabel"))
        self.verticalLayout.addWidget(self.DOBLabel)
        self.EthnicGroupLabel = QtGui.QLabel(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.EthnicGroupLabel.setFont(font)
        self.EthnicGroupLabel.setObjectName(_fromUtf8("EthnicGroupLabel"))
        self.verticalLayout.addWidget(self.EthnicGroupLabel)
        self.EthnicGroupLabel_2 = QtGui.QLabel(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.EthnicGroupLabel_2.setFont(font)
        self.EthnicGroupLabel_2.setObjectName(_fromUtf8("EthnicGroupLabel_2"))
        self.verticalLayout.addWidget(self.EthnicGroupLabel_2)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        self.verticalLayout_9 = QtGui.QVBoxLayout()
        self.verticalLayout_9.setObjectName(_fromUtf8("verticalLayout_9"))
        self.DOBDisplay = QtGui.QLineEdit(self.horizontalLayoutWidget_2)
        self.DOBDisplay.setObjectName(_fromUtf8("DOBDisplay"))
        self.verticalLayout_9.addWidget(self.DOBDisplay)
        self.EthnicGroupDisplay = QtGui.QLineEdit(self.horizontalLayoutWidget_2)
        self.EthnicGroupDisplay.setObjectName(_fromUtf8("EthnicGroupDisplay"))
        self.verticalLayout_9.addWidget(self.EthnicGroupDisplay)
        self.EthnicGroupDisplay_2 = QtGui.QLineEdit(self.horizontalLayoutWidget_2)
        self.EthnicGroupDisplay_2.setObjectName(_fromUtf8("EthnicGroupDisplay_2"))
        self.verticalLayout_9.addWidget(self.EthnicGroupDisplay_2)
        self.horizontalLayout_2.addLayout(self.verticalLayout_9)
        self.horizontalLayoutWidget = QtGui.QWidget(SimpleButton)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(70, 200, 171, 231))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.horizontalLayoutWidget.setFont(font)
        self.horizontalLayoutWidget.setObjectName(_fromUtf8("horizontalLayoutWidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.TVLabel = QtGui.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.TVLabel.setFont(font)
        self.TVLabel.setObjectName(_fromUtf8("TVLabel"))
        self.verticalLayout_3.addWidget(self.TVLabel)
        self.RVLabel = QtGui.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.RVLabel.setFont(font)
        self.RVLabel.setObjectName(_fromUtf8("RVLabel"))
        self.verticalLayout_3.addWidget(self.RVLabel)
        self.ERVLabel = QtGui.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.ERVLabel.setFont(font)
        self.ERVLabel.setObjectName(_fromUtf8("ERVLabel"))
        self.verticalLayout_3.addWidget(self.ERVLabel)
        self.ICLabel = QtGui.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.ICLabel.setFont(font)
        self.ICLabel.setObjectName(_fromUtf8("ICLabel"))
        self.verticalLayout_3.addWidget(self.ICLabel)
        self.VCLabel = QtGui.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.VCLabel.setFont(font)
        self.VCLabel.setObjectName(_fromUtf8("VCLabel"))
        self.verticalLayout_3.addWidget(self.VCLabel)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        self.verticalLayout_4 = QtGui.QVBoxLayout()
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.TVDisplay = QtGui.QLineEdit(self.horizontalLayoutWidget)
        self.TVDisplay.setObjectName(_fromUtf8("TVDisplay"))
        self.verticalLayout_4.addWidget(self.TVDisplay)
        self.RVDisplay = QtGui.QLineEdit(self.horizontalLayoutWidget)
        self.RVDisplay.setObjectName(_fromUtf8("RVDisplay"))
        self.verticalLayout_4.addWidget(self.RVDisplay)
        self.ERVDisplay = QtGui.QLineEdit(self.horizontalLayoutWidget)
        self.ERVDisplay.setObjectName(_fromUtf8("ERVDisplay"))
        self.verticalLayout_4.addWidget(self.ERVDisplay)
        self.ICDisplay = QtGui.QLineEdit(self.horizontalLayoutWidget)
        self.ICDisplay.setObjectName(_fromUtf8("ICDisplay"))
        self.verticalLayout_4.addWidget(self.ICDisplay)
        self.TCDisplay = QtGui.QLineEdit(self.horizontalLayoutWidget)
        self.TCDisplay.setObjectName(_fromUtf8("TCDisplay"))
        self.verticalLayout_4.addWidget(self.TCDisplay)
        self.horizontalLayout.addLayout(self.verticalLayout_4)
        self.EditPatientButton = QtGui.QPushButton(SimpleButton)
        self.EditPatientButton.setGeometry(QtCore.QRect(360, 160, 161, 32))
        self.EditPatientButton.setObjectName(_fromUtf8("EditPatientButton"))
        self.plotWidget = PlotWidget(SimpleButton)
        self.plotWidget.setGeometry(QtCore.QRect(270, 200, 521, 281))
        self.plotWidget.setObjectName(_fromUtf8("plotWidget"))
        self.checkBox = QtGui.QCheckBox(SimpleButton)
        self.checkBox.setGeometry(QtCore.QRect(270, 493, 495, 20))
        self.checkBox.setChecked(True)
        self.checkBox.setObjectName(_fromUtf8("checkBox"))
        self.pushButton_2 = QtGui.QPushButton(SimpleButton)
        self.pushButton_2.setGeometry(QtCore.QRect(270, 555, 521, 28))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.pushButton_3 = QtGui.QPushButton(SimpleButton)
        self.pushButton_3.setGeometry(QtCore.QRect(270, 590, 521, 28))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.pushButton = QtGui.QPushButton(SimpleButton)
        self.pushButton.setGeometry(QtCore.QRect(270, 520, 521, 28))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))

        self.retranslateUi(SimpleButton)
        QtCore.QMetaObject.connectSlotsByName(SimpleButton)

    def retranslateUi(self, SimpleButton):
        SimpleButton.setWindowTitle(_translate("SimpleButton", "Simple Form", None))
        self.CalibrateButton.setText(_translate("SimpleButton", "Calibrate", None))
        self.StartButton.setText(_translate("SimpleButton", "Start", None))
        self.StopButton.setText(_translate("SimpleButton", "Stop", None))
        self.CancelButton.setText(_translate("SimpleButton", "Cancel", None))
        self.BREEZETitle.setText(_translate("SimpleButton", "TEST RESULTS", None))
        self.PatientIDLabel.setText(_translate("SimpleButton", "Patient ID", None))
        self.FirstNameLabel.setText(_translate("SimpleButton", "First Name", None))
        self.LastNameLabel.setText(_translate("SimpleButton", "Last Name", None))
        self.GenderLabel.setText(_translate("SimpleButton", "Gender", None))
        self.SmokerLabel.setText(_translate("SimpleButton", "Smoker?", None))
        self.HeightLabel.setText(_translate("SimpleButton", "Height (cm)", None))
        self.DOBLabel.setText(_translate("SimpleButton", "Date of Birth", None))
        self.EthnicGroupLabel.setText(_translate("SimpleButton", "Ethnic Group", None))
        self.EthnicGroupLabel_2.setText(_translate("SimpleButton", "Current Diagnosis", None))
        self.TVLabel.setText(_translate("SimpleButton", "TV (L)", None))
        self.RVLabel.setText(_translate("SimpleButton", "RV (L)", None))
        self.ERVLabel.setText(_translate("SimpleButton", "ERV (L)", None))
        self.ICLabel.setText(_translate("SimpleButton", "IC (L)", None))
        self.VCLabel.setText(_translate("SimpleButton", "TLC (L)", None))
        self.EditPatientButton.setText(_translate("SimpleButton", "Edit Patient Details", None))
        self.checkBox.setText(_translate("SimpleButton", "Mouse Enabled", None))
        self.pushButton_2.setText(_translate("SimpleButton", "Volumetric Flow", None))
        self.pushButton_3.setText(_translate("SimpleButton", "Volume", None))
        self.pushButton.setText(_translate("SimpleButton", "Breath Speed", None))

from pyqtgraph import PlotWidget

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    SimpleButton = QtGui.QWidget()
    ui = Ui_SimpleButton()
    ui.setupUi(SimpleButton)
    SimpleButton.show()
    sys.exit(app.exec_())

