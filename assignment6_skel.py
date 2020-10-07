import pickle
import sys
from PyQt5.QtWidgets import (QWidget, QPushButton,
    QHBoxLayout, QVBoxLayout, QApplication, QLabel,
    QComboBox, QTextEdit, QLineEdit)
from PyQt5.QtCore import Qt


class ScoreDB(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.dbfilename = 'assignment6.dat'
        self.readScoreDB()
        self.showScoreDB(self.scoredb)
        self.text_status.setText('ScoreDB Program Start!')

    def initUI(self):
        self.setGeometry(300, 300, 500, 250)
        #label,LineEdit,ComboBox 추가
        label_name = QLabel('Name:')
        label_score = QLabel('Score:')
        label_age = QLabel('Age:')
        label_amount = QLabel('Amount:')
        label_result = QLabel('Result:')
        label_key = QLabel('Key:')
        label_status = QLabel('Status')
        self.text_name = QLineEdit()
        self.text_score = QLineEdit()
        self.text_age = QLineEdit()
        self.text_amount = QLineEdit()
        self.text_status = QLineEdit()
        self.combobox_key = QComboBox()
        #콤보박스 항목추가
        self.combobox_key.addItem('Name')
        self.combobox_key.addItem('Age')
        self.combobox_key.addItem('Score')
        #PushButton추가
        button_add = QPushButton('Add')
        button_del = QPushButton('Del')
        button_find = QPushButton('Find')
        button_inc = QPushButton('Inc')
        button_show = QPushButton('Show')
        #수평박향레이아웃생성
        hlayout1 = QHBoxLayout()
        hlayout2 = QHBoxLayout()
        hlayout3 = QHBoxLayout()
        hlayout4 = QHBoxLayout()
        hlayout5 = QHBoxLayout()
        hlayout1.addWidget(label_name)
        hlayout1.addWidget(self.text_name)
        hlayout1.addWidget(label_age)
        hlayout1.addWidget(self.text_age)
        hlayout1.addWidget(label_score)
        hlayout1.addWidget(self.text_score)
        hlayout2.addStretch(1)
        hlayout2.addWidget(label_amount)
        hlayout2.addWidget(self.text_amount)
        hlayout2.addWidget(label_key)
        hlayout2.addWidget(self.combobox_key)
        hlayout3.addStretch(1)
        hlayout3.addWidget(button_add)
        hlayout3.addWidget(button_del)
        hlayout3.addWidget(button_find)
        hlayout3.addWidget(button_inc)
        hlayout3.addWidget(button_show)
        hlayout4.addWidget(label_result)
        hlayout4.addStretch(300)
        hlayout5.addWidget(label_status)
        hlayout5.addWidget(self.text_status)
        #수직방향레이아웃생성
        vlayout = QVBoxLayout()
        vlayout.addLayout(hlayout1)
        vlayout.addLayout(hlayout2)
        vlayout.addLayout(hlayout3)
        vlayout.addLayout(hlayout4)
        self.textEdit = QTextEdit()
        vlayout.addWidget(self.textEdit)
        vlayout.addLayout(hlayout5)
        self.setLayout(vlayout)
        self.show()
        #신호설정
        button_add.clicked.connect(self.addScoreDB)
        button_del.clicked.connect(self.delScoreDB)
        button_find.clicked.connect(self.findScoreDB)
        button_inc.clicked.connect(self.incScoreDB)
        button_show.clicked.connect(self.click_showScoreDB)

    def closeEvent(self, event):
        self.writeScoreDB()

    def readScoreDB(self):
        try:
            fH = open(self.dbfilename, 'rb')
            self.scoredb =  pickle.load(fH)
        except FileNotFoundError as e:
            self.scoredb = []
        fH.close()

    # write the data into person db
    def writeScoreDB(self):
        fH = open(self.dbfilename, 'wb')
        pickle.dump(self.scoredb, fH)
        fH.close()

    def showScoreDB(self,input_list,key='Name'):
        self.textEdit.clear()
        input_list.sort(key=lambda x: x[key])
        for i in input_list:
            self.textEdit.append('Age = %d \t Name = %s \t Score = %d' % (i['Age'], i['Name'], i['Score']))
        self.text_status.setText('Success!')

    def addScoreDB(self):
        if self.text_name.text().strip() != '' and self.text_age.text().strip() != '' and self.text_score.text().strip() != '':
            try:
                record = {'Age':int(self.text_age.text()),'Name':self.text_name.text(),'Score':int(self.text_score.text())}
                self.scoredb.append(record)
                self.showScoreDB(self.scoredb)
            except ValueError:
                self.text_status.setText('please input Age and Score as integer type,Name as string type.')
        else:
            self.text_status.setText('Please input Name and Age and Score')

    def delScoreDB(self):
        if self.text_name.text().strip() != '':
            temp = []
            for p in self.scoredb[:]:
                if p["Name"] == self.text_name.text():
                    temp.append(p['Name'])
                    self.scoredb.remove(p)
            if not temp:
                self.text_status.setText('He is not on the list.')
            else:
                self.showScoreDB(self.scoredb)
        else:
            self.text_status.setText('Please input Name')

    def findScoreDB(self):
        if self.text_name.text().strip() != '':
            temp = []
            for p in self.scoredb:
                if p["Name"] == self.text_name.text():
                    temp.append(p)
            if not temp:
                self.text_status.setText('He is not on the list.')
            else:
                self.showScoreDB(temp)
        else:
            self.text_status.setText('Please input Name')

    def incScoreDB(self):
        if self.text_name.text().strip() != '' and   self.text_amount.text().strip() != '':
            try:
                temp = []
                for p in self.scoredb:
                    if p["Name"] == self.text_name.text():
                        temp.append(p['Name'])
                        p['Score'] += int(self.text_amount.text())
                if not temp :
                    self.text_status.setText('He is not on the list.')
                else:
                    self.showScoreDB(self.scoredb)
            except ValueError:
                self.text_status.setText('please input Score as integer type.')
        else:
            self.text_status.setText('Please input Name and Amount')

    def click_showScoreDB(self):
        self.showScoreDB(self.scoredb,self.combobox_key.currentText())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = ScoreDB()
    sys.exit(app.exec_())


