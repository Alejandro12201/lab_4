from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTableWidget,QTableWidgetItem
from Clases.menu import *
from Clases.rangos import *
from Clases.obtencion import *
from Clases.reporte import *
import matplotlib.pyplot as plt 
import matplotlib.animation as animation
import sys

#------------------------------------------------------------------------------
global pause
pause = False
global y_data
y_data = []

#------------------------------------------------------------------------------
def onclick(event):
    global pause
    print("pausa")
    pause=True
    
#------------------------------------------------------------------------------
fig, ax=plt.subplots()
fig.canvas.mpl_connect("button_press_event", onclick)
            
#------------------------------------------------------------------------------
def update_data(i): 
    if not pause:
        #dato=Puerto.leer(op_pu)
        dato=int(puerto.readline().decode().strip())
        print(dato)
        y_data.append(dato)
        ax.clear()
        ax.plot(y_data)
        time.sleep(1)
        
#------------------------------------------------------------------------------
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1096, 1313)
        font = QtGui.QFont()
        font.setFamily("Monotype Koufi")
        MainWindow.setFont(font)
        MainWindow.setStyleSheet("background-color: rgb(23, 173, 253)")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(280, 30, 571, 81))
        font = QtGui.QFont()
        font.setFamily("Vladimir Script")
        font.setPointSize(36)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setStyleSheet("")
        self.label.setTextFormat(QtCore.Qt.RichText)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(230, 80, 691, 81))
        font = QtGui.QFont()
        font.setFamily("Terminal")
        font.setPointSize(36)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("")
        self.label_2.setTextFormat(QtCore.Qt.RichText)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, -10, 351, 61))
        font = QtGui.QFont()
        font.setFamily("Wide Latin")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("")
        self.label_3.setTextFormat(QtCore.Qt.RichText)
        self.label_3.setObjectName("label_3")
        self.GroupBox_Captura = QtWidgets.QGroupBox(self.centralwidget)
        self.GroupBox_Captura.setGeometry(QtCore.QRect(30, 150, 381, 221))
        self.GroupBox_Captura.setAutoFillBackground(False)
        self.GroupBox_Captura.setObjectName("GroupBox_Captura")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.GroupBox_Captura)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 50, 351, 91))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.radioButton_2 = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.radioButton_2.setObjectName("radioButton_2")
        self.verticalLayout.addWidget(self.radioButton_2)
        self.radioButton_3 = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.radioButton_3.setObjectName("radioButton_3")
        self.verticalLayout.addWidget(self.radioButton_3)
        self.pushButton = QtWidgets.QPushButton(self.GroupBox_Captura)
        self.pushButton.setGeometry(QtCore.QRect(270, 170, 93, 28))
        self.pushButton.setStyleSheet("background-color: rgb(52, 96, 255);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.ver_opcion_1)



        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(20, 10, 232, 100))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setStyleSheet("background-image: url(logo_escuela_ingenieria.png);")
        self.frame.setObjectName("frame")

        self.groupBox_Config = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_Config.setGeometry(QtCore.QRect(610, 170, 441, 491))
        self.groupBox_Config.setAutoFillBackground(False)
        self.groupBox_Config.setObjectName("groupBox_Config")
        self.pushButton_2 = QtWidgets.QPushButton(self.groupBox_Config)
        self.pushButton_2.setGeometry(QtCore.QRect(310, 290, 101, 28))
        self.pushButton_2.setStyleSheet("background-color: rgb(52, 96, 255);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.ver_opcion_2)





        self.max_normal = QtWidgets.QLineEdit(self.groupBox_Config)
        self.max_normal.setGeometry(QtCore.QRect(210, 130, 113, 22))
        self.max_normal.setObjectName("max_normal")
        self.label_5 = QtWidgets.QLabel(self.groupBox_Config)
        self.label_5.setGeometry(QtCore.QRect(110, 20, 191, 16))
        self.label_5.setObjectName("label_5")
        self.label_7 = QtWidgets.QLabel(self.groupBox_Config)
        self.label_7.setGeometry(QtCore.QRect(50, 140, 91, 16))
        self.label_7.setObjectName("label_7")
        self.min_normal = QtWidgets.QLineEdit(self.groupBox_Config)
        self.min_normal.setGeometry(QtCore.QRect(210, 160, 113, 22))
        self.min_normal.setObjectName("min_normal")
        self.label_8 = QtWidgets.QLabel(self.groupBox_Config)
        self.label_8.setGeometry(QtCore.QRect(50, 60, 91, 16))
        self.label_8.setObjectName("label_8")
        self.min_hipotermia = QtWidgets.QLineEdit(self.groupBox_Config)
        self.min_hipotermia.setGeometry(QtCore.QRect(210, 80, 113, 22))
        self.min_hipotermia.setObjectName("min_hipotermia")
        self.max_hipotermia = QtWidgets.QLineEdit(self.groupBox_Config)
        self.max_hipotermia.setGeometry(QtCore.QRect(210, 50, 113, 22))
        self.max_hipotermia.setObjectName("max_hipotermia")
        self.min_fiebre = QtWidgets.QLineEdit(self.groupBox_Config)
        self.min_fiebre.setGeometry(QtCore.QRect(210, 240, 113, 22))
        self.min_fiebre.setObjectName("min_fiebre")
        self.max_fiebre = QtWidgets.QLineEdit(self.groupBox_Config)
        self.max_fiebre.setGeometry(QtCore.QRect(210, 210, 113, 22))
        self.max_fiebre.setObjectName("max_fiebre")
        self.label_9 = QtWidgets.QLabel(self.groupBox_Config)
        self.label_9.setGeometry(QtCore.QRect(50, 220, 91, 16))
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.groupBox_Config)
        self.label_10.setGeometry(QtCore.QRect(170, 50, 31, 16))
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.groupBox_Config)
        self.label_11.setGeometry(QtCore.QRect(170, 80, 31, 16))
        self.label_11.setObjectName("label_11")
        self.label_17 = QtWidgets.QLabel(self.groupBox_Config)
        self.label_17.setGeometry(QtCore.QRect(170, 130, 31, 16))
        self.label_17.setObjectName("label_17")
        self.label_18 = QtWidgets.QLabel(self.groupBox_Config)
        self.label_18.setGeometry(QtCore.QRect(170, 160, 31, 16))
        self.label_18.setObjectName("label_18")
        self.label_19 = QtWidgets.QLabel(self.groupBox_Config)
        self.label_19.setGeometry(QtCore.QRect(170, 210, 31, 16))
        self.label_19.setObjectName("label_19")
        self.label_20 = QtWidgets.QLabel(self.groupBox_Config)
        self.label_20.setGeometry(QtCore.QRect(170, 240, 31, 16))
        self.label_20.setObjectName("label_20")
        self.tableWidget = QtWidgets.QTableWidget(self.groupBox_Config)
        self.tableWidget.setGeometry(QtCore.QRect(60, 330, 331, 141))
        self.tableWidget.setStyleSheet("background-color: rgb(105, 240, 255);")
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.GroupBox_Captura_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.GroupBox_Captura_2.setGeometry(QtCore.QRect(40, 410, 381, 311))
        self.GroupBox_Captura_2.setAutoFillBackground(False)
        self.GroupBox_Captura_2.setObjectName("GroupBox_Captura_2")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.GroupBox_Captura_2)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(10, 50, 351, 191))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.radioButton_4 = QtWidgets.QRadioButton(self.verticalLayoutWidget_2)
        self.radioButton_4.setObjectName("radioButton_4")
        self.verticalLayout_2.addWidget(self.radioButton_4)
        self.radioButton_7 = QtWidgets.QRadioButton(self.verticalLayoutWidget_2)
        self.radioButton_7.setObjectName("radioButton_7")
        self.verticalLayout_2.addWidget(self.radioButton_7)
        self.radioButton_6 = QtWidgets.QRadioButton(self.verticalLayoutWidget_2)
        self.radioButton_6.setObjectName("radioButton_6")
        self.verticalLayout_2.addWidget(self.radioButton_6)
        self.radioButton_5 = QtWidgets.QRadioButton(self.verticalLayoutWidget_2)
        self.radioButton_5.setObjectName("radioButton_5")
        self.verticalLayout_2.addWidget(self.radioButton_5)
        self.pushButton_3 = QtWidgets.QPushButton(self.GroupBox_Captura_2)
        self.pushButton_3.setGeometry(QtCore.QRect(270, 260, 93, 28))
        self.pushButton_3.setStyleSheet("background-color: rgb(52, 96, 255);")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(self.ver_opcion_3)






        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(910, 700, 141, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setStyleSheet("background-color: rgb(52, 96, 255);")
        self.pushButton_5.setObjectName("pushButton_5")
        self.label_2.raise_()
        self.label_3.raise_()
        self.label.raise_()
        self.GroupBox_Captura.raise_()
        self.groupBox_Config.raise_()
        self.GroupBox_Captura_2.raise_()
        self.pushButton_5.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1096, 26))
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
        self.label.setText(_translate("MainWindow", "Monitor De Temperatura"))
        self.label_2.setText(_translate("MainWindow", "Escuela Colombiana De Ingeniería Julio Garavito Laboratorio 4"))
        self.label_3.setText(_translate("MainWindow", "Diego Alejandro García Pulido "))
        self.GroupBox_Captura.setTitle(_translate("MainWindow", "Captura De Datos"))
        self.radioButton_2.setText(_translate("MainWindow", "Escoger cantidad de datos de captura"))
        self.radioButton_3.setText(_translate("MainWindow", "Escoger momento de captura con grafica en tiempo real"))
        self.pushButton.setText(_translate("MainWindow", "ver selección"))
        self.groupBox_Config.setTitle(_translate("MainWindow", "Configuración De Parámetros "))
        self.pushButton_2.setText(_translate("MainWindow", "Ver Parámetros "))
        self.label_5.setText(_translate("MainWindow", "Por favor ingrese valores de:"))
        self.label_7.setText(_translate("MainWindow", "Normal"))
        self.label_8.setText(_translate("MainWindow", "Hipotermia"))
        self.label_9.setText(_translate("MainWindow", "Fiebre"))
        self.label_10.setText(_translate("MainWindow", "Max"))
        self.label_11.setText(_translate("MainWindow", "Min"))
        self.label_17.setText(_translate("MainWindow", "Max"))
        self.label_18.setText(_translate("MainWindow", "Min"))
        self.label_19.setText(_translate("MainWindow", "Max"))
        self.label_20.setText(_translate("MainWindow", "Min"))
        self.GroupBox_Captura_2.setTitle(_translate("MainWindow", "Ver Reportes"))
        self.radioButton_4.setText(_translate("MainWindow", "Ver grafica de los datos capturados"))
        self.radioButton_7.setText(_translate("MainWindow", "Valor maximo"))
        self.radioButton_6.setText(_translate("MainWindow", "Valor minimo"))
        self.radioButton_5.setText(_translate("MainWindow", "Promedio de temperatura"))
        self.pushButton_3.setText(_translate("MainWindow", "ver selección"))
        self.pushButton_5.setText(_translate("MainWindow", "Salir"))
    
    
    
    def ver_opcion_1(self):
            if (self.radioButton_2.isChecked()) :
                print("Selecciono " +self.radioButton_2.text())
            elif (self.radioButton_3.isChecked()) :
                print("Selecciono " +self.radioButton_3.text())
    
    def ver_opcion_2(self):
        self.tableWidget.setColumnCount(6)
        self.tableWidget.setHorizontalHeaderLabels(('1','2','3','4','5','6'))
        inx=0
        with open('database\Parametros.csv') as f:
            usuarios=f.readlines()
        for usuario in usuarios:
            usuario=usuario.replace("\n", "")
            n1,n2,n3,n4,n5,n6=usuario.split(";")
            self.tableWidget.insertRow(inx)
            self.tableWidget.setItem(inx, 0, QTableWidgetItem(n1))
            self.tableWidget.setItem(inx, 1, QTableWidgetItem(n2))
            self.tableWidget.setItem(inx, 2, QTableWidgetItem(n3))
            self.tableWidget.setItem(inx, 3, QTableWidgetItem(n4))
            self.tableWidget.setItem(inx, 4, QTableWidgetItem(n5))
            self.tableWidget.setItem(inx, 5, QTableWidgetItem(n6))

    def ver_opcion_3(self):
            if (self.radioButton_4.isChecked()) :
                grafiquita()
            elif (self.radioButton_7.isChecked()) :
                valor_max()
            elif (self.radioButton_6.isChecked()) :
                valor_min()
            elif (self.radioButton_5.isChecked()) :
                prom_temp()
    




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
