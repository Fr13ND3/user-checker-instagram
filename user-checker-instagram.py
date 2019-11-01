# Coded By Zed-Team
# Please Fork Dont Copy
# And Join My Channel : @Arch_TM

import os
try:
    from PyQt5 import QtCore, QtGui, QtWidgets
    from PyQt5.QtWidgets import QFileDialog
except Exception:
    if os.name == "nt":
        os.system('pip install Pyqt5 --user')
    else:
        os.system('sudo pip install Pyqt5')
from time import sleep
try:
    import requests
except Exception:
    if os.name == "nt":
        os.system('pip install requests --user')
    else:
        os.system('sudo pip install requests')
try:
    from bs4 import BeautifulSoup
except Exception:
    if os.name == "nt":
        os.system('pip install bs4 --user')
    else:
        os.system('sudo pip install bs4')


class Ui_main_form(object):
    def setupUi(self, main_form):
        main_form.setObjectName("main_form")
        main_form.resize(335, 565)
        font = QtGui.QFont()
        font.setPointSize(9)
        main_form.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("2394490_0.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        main_form.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(main_form)
        self.centralwidget.setObjectName("centralwidget")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(20, 109, 291, 351))
        self.textEdit.setObjectName("textEdit")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(20, 58, 135, 29))
        self.pushButton.setMaximumSize(QtCore.QSize(1677721, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 479, 91, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.check_follower = QtWidgets.QCheckBox(self.centralwidget)
        self.check_follower.setGeometry(QtCore.QRect(120, 478, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.check_follower.setFont(font)
        self.check_follower.setChecked(True)
        self.check_follower.setObjectName("check_follower")
        self.check_followeing = QtWidgets.QCheckBox(self.centralwidget)
        self.check_followeing.setGeometry(QtCore.QRect(230, 478, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.check_followeing.setFont(font)
        self.check_followeing.setObjectName("check_followeing")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(177, 58, 135, 29))
        self.pushButton_2.setMaximumSize(QtCore.QSize(1677721, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.check_followeing_2 = QtWidgets.QCheckBox(self.centralwidget)
        self.check_followeing_2.setGeometry(QtCore.QRect(230, 510, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.check_followeing_2.setFont(font)
        self.check_followeing_2.setChecked(True)
        self.check_followeing_2.setObjectName("check_followeing_2")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 510, 81, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.check_follower_2 = QtWidgets.QCheckBox(self.centralwidget)
        self.check_follower_2.setGeometry(QtCore.QRect(120, 510, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.check_follower_2.setFont(font)
        self.check_follower_2.setObjectName("check_follower_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 20, 61, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(90, 18, 221, 22))
        self.lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit.setObjectName("lineEdit")
        main_form.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(main_form)
        self.statusbar.setObjectName("statusbar")
        main_form.setStatusBar(self.statusbar)

        self.retranslateUi(main_form)
        self.pushButton.clicked.connect(self.open_file)
        self.pushButton_2.clicked.connect(self.start_btn)
        QtCore.QMetaObject.connectSlotsByName(main_form)
        d = ""
    def open_file(self):
        fileName= str(QFileDialog.getOpenFileName(None,"Select Your File", "","*.txt",))
        global d
        d = fileName[2:-11]

    def start_btn(self):
        try:
            with open('user_checked.txt','x'):
                pass
        except Exception:
            pass
        sleep(0.5)
        app.processEvents()
        se = ""
        status = "False"
        with open(d) as rf:
            for i in rf.readlines():
                se+=i   
            mylists = se.split('\n')
            if self.check_follower.isChecked():
                app.processEvents()
                if self.check_follower_2.isChecked():
                    sleep(0.5)
                    status = "False"
                    try:
                        for ii in mylists:
                            if status == "False":
                                app.processEvents()
                                line_combolist = "".join(ii)
                                line_combolist = line_combolist.split(':')
                                onlyy_user =line_combolist[0]
                                
                                req = requests.get(f'http://socialclub.shop/api/info.php?user={onlyy_user}')
                                soup = str(BeautifulSoup(req.text,'html.parser'))
                                
                                soup = soup.split('"followers":')
                                soup = soup[1]
                                soup = soup.split(',')
                                
                                soup = "".join(soup[0])
                                soup = str(soup)
                                soup = soup.replace('"',"")
                                soup = "".join(soup)
                                if soup == "null":
                                    continue
                                else:
                                    try:
                                        soup = int(soup)
                                    except ValueError or TypeError:
                                        continue
                                    try:
                                        count = self.lineEdit.text()
                                        count = int(count)
                                    except ValueError or TypeError:
                                        self.textEdit.append('[ - ] Your Number is not int (Example : please Enter 10000 )')
                                    
                                    if soup >= count:
                                        self.textEdit.append(f"{onlyy_user} == {soup}")
                                        with open('user_checked.txt','a')as wf:
                                            wf.write(onlyy_user)
                                            wf.write('\n')
                            else:
                                break
                                self.textEdit.append('[ + ] Finished')
                    except IndexError:
                        self.textEdit.append('[ + ] Finished !')
                        status = "True"
                        app.processEvents()    


                                    
                elif self.check_followeing_2.isChecked():
                    app.processEvents()
                    sleep(0.5)
                    status = "False"
                    try:
                        for ii in mylists:
                            if status == "False":
                                app.processEvents()
                                onlyy_user = "".join(ii)
                            
                                
                                req = requests.get(f'http://socialclub.shop/api/info.php?user={onlyy_user}')
                                soup = str(BeautifulSoup(req.text,'html.parser'))
                                
                                soup = soup.split('"followers":')
                                soup = soup[1]
                                soup = soup.split(',')
                                
                                soup = "".join(soup[0])
                                soup = str(soup)
                                soup = soup.replace('"',"")
                                soup = "".join(soup)
                                if soup == "null":
                                    continue
                                else:
                                    try:
                                        soup = int(soup)
                                    except ValueError or TypeError:
                                        continue
                                    try:
                                        count = self.lineEdit.text()
                                        count = int(count)
                                    except ValueError or TypeError:
                                        self.textEdit.append('[ - ] Your Number is not int (Example : please Enter 10000 )')
                                    
                                    if soup >= count:
                                        self.textEdit.append(f"{onlyy_user} == {soup}")
                                        with open('user_checked.txt','a')as wf:
                                            wf.write(onlyy_user)
                                            wf.write('\n')

                            else:
                                break
                                self.textEdit.append('[ + ] Finished')
                    except IndexError:
                        self.textEdit.append('[ + ] Finished !')
                        status = "True"
                        app.processEvents()    


                      
            elif self.check_followeing.isChecked():
                if self.check_follower_2.isChecked():
                    status = "False"
                    sleep(0.5)
                    try:
                        
                        for ii in mylists:
                            if status == "False":
                                app.processEvents()
                                line_combolist = "".join(ii)
                                line_combolist = line_combolist.split(':')
                                onlyy_user =line_combolist[0]
                                
                                req = requests.get(f'http://socialclub.shop/api/info.php?user={onlyy_user}')
                                soup = str(BeautifulSoup(req.text,'html.parser'))
                                
                                soup = soup.split('"following":')
                                soup = soup[1]
                                soup = soup.split(',')
                                
                                soup = "".join(soup[0])
                                soup = str(soup)
                                soup = soup.replace('"',"")
                                soup = "".join(soup)
                                if soup == "null":
                                    continue
                                else:
                                    try:
                                        soup = int(soup)
                                    except ValueError or TypeError:
                                        continue
                                    try:
                                        count = self.lineEdit.text()
                                        count = int(count)
                                    except ValueError or TypeError:
                                        self.textEdit.append('[ - ] Your Number is not int (Example : please Enter 10000 )')
                                    if soup >= count:
                                        self.textEdit.append(f"{onlyy_user} == {soup}")
                                        with open('user_checked.txt','a')as wf:
                                            wf.write(onlyy_user)
                                            wf.write('\n')
                            else:
                                break
                                self.textEdit.append('[ + ] Finished')
                    except IndexError:
                        self.textEdit.append('[ + ] Finished !')
                        status = "True"
                        app.processEvents()    
                elif self.check_followeing_2.isChecked():
                    status = "False"
                    sleep(0.5)
                    try:
                        
                        for ii in mylists:
                            if status == "False":
                                app.processEvents()
                                onlyy_user = "".join(ii)
                                
                                req = requests.get(f'http://socialclub.shop/api/info.php?user={onlyy_user}')
                                soup = str(BeautifulSoup(req.text,'html.parser'))
                                
                                soup = soup.split('"following":')
                                soup = soup[1]
                                soup = soup.split(',')
                                
                                soup = "".join(soup[0])
                                soup = str(soup)
                                soup = soup.replace('"',"")
                                soup = "".join(soup)
                                if soup == "null":
                                    continue
                                else:
                                    try:
                                        soup = int(soup)
                                    except ValueError or TypeError:
                                        continue
                                    try:
                                        count = self.lineEdit.text()
                                        count = int(count)
                                    except ValueError or TypeError:
                                        self.textEdit.append('[ - ] Your Number is not int (Example : please Enter 10000 )')
                                    if soup >= count:
                                        self.textEdit.append(f"{onlyy_user} == {soup}")
                                        with open('user_checked.txt','a')as wf:
                                            wf.write(onlyy_user)
                                            wf.write('\n')
                            else:
                                break
                                self.textEdit.append('[ + ] Finished')
                    except IndexError:
                        self.textEdit.append('[ + ] Finished !')
                        status = "True"
                        app.processEvents()    
                else:
                    self.textEdit.append('[ * ] Please select type check!')
    def retranslateUi(self, main_form):
        _translate = QtCore.QCoreApplication.translate
        main_form.setWindowTitle(_translate("main_form", "Instagram User Cheacker By Zed-Team & Telegram : @Arch_TM"))
        self.pushButton.setText(_translate("main_form", "Load File"))
        self.label.setText(_translate("main_form", "Type Check : "))
        self.check_follower.setText(_translate("main_form", "Follower"))
        self.check_followeing.setText(_translate("main_form", "Following"))
        self.pushButton_2.setText(_translate("main_form", "Start Check"))
        self.check_followeing_2.setText(_translate("main_form", "only user"))
        self.label_2.setText(_translate("main_form", "Type File : "))
        self.check_follower_2.setText(_translate("main_form", "ComboList"))
        self.label_3.setText(_translate("main_form", "Count :"))
        self.lineEdit.setPlaceholderText(_translate("main_form", "just number"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    main_form = QtWidgets.QMainWindow()
    ui = Ui_main_form()
    ui.setupUi(main_form)
    main_form.show()
    sys.exit(app.exec_())
