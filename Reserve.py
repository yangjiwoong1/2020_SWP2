from Management import Management
import sys
from PyQt5.QtWidgets import (QWidget, QPushButton,
    QHBoxLayout, QVBoxLayout, QApplication, QLabel,
    QComboBox, QTextEdit, QLineEdit)
from PyQt5.QtCore import Qt
import datetime


class Reserve(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()
        self.management = Management("list.dat")
        self.management.readReservationList()
        self.gap = datetime.timedelta(0,3600)
        self.showReservationList(self.management.getReservationList(),'All')
        self.text_status.setText('Reservation Program Start!')

    def initUI(self):
        self.setGeometry(300, 300, 780, 250)
        self.setWindowTitle('Reservation System')

        #label,LineEdit,TextEdit,ComboBox 생성
        label_name = QLabel('이름:')
        label_phone = QLabel('번호:')
        label_year = QLabel('년도(yyyy):')
        label_month = QLabel('월(mm):')
        label_date = QLabel('일(dd):')
        label_hours = QLabel('시(hh):')
        label_minutes = QLabel('분(mm):')
        label_seconds = QLabel('초(ss):')
        label_key = QLabel('옵션:')
        label_status = QLabel('Status')

        self.text_name = QLineEdit()
        self.text_name.setFixedWidth(60)
        self.text_name.setAlignment(Qt.AlignRight)
        self.text_name.setMaxLength(6)
        self.text_phone = QLineEdit()
        self.text_phone.setFixedWidth(100)
        self.text_phone.setAlignment(Qt.AlignRight)
        self.text_phone.setMaxLength(11)
        self.text_year = QLineEdit()
        self.text_year.setFixedWidth(80)
        self.text_year.setAlignment(Qt.AlignRight)
        self.text_year.setMaxLength(4)
        self.text_month = QLineEdit()
        self.text_month.setFixedWidth(60)
        self.text_month.setAlignment(Qt.AlignRight)
        self.text_month.setMaxLength(2)
        self.text_date = QLineEdit()
        self.text_date.setFixedWidth(60)
        self.text_date.setAlignment(Qt.AlignRight)
        self.text_date.setMaxLength(2)
        self.text_hours = QLineEdit()
        self.text_hours.setFixedWidth(60)
        self.text_hours.setAlignment(Qt.AlignRight)
        self.text_hours.setMaxLength(2)
        self.text_minutes= QLineEdit()
        self.text_minutes.setFixedWidth(60)
        self.text_minutes.setAlignment(Qt.AlignRight)
        self.text_minutes.setMaxLength(2)
        self.text_seconds = QLineEdit()
        self.text_seconds.setFixedWidth(60)
        self.text_seconds.setAlignment(Qt.AlignRight)
        self.text_seconds.setMaxLength(2)
        self.text_status = QLineEdit()

        self.text_title = QTextEdit()
        self.text_title.setReadOnly(True)
        font = self.text_title.font()
        font.setPointSize(font.pointSize() + 20)
        self.text_title.setFont(font)
        self.text_title.setText("Reservation System")
        self.text_title.setAlignment(Qt.AlignCenter)

        self.text_print = QTextEdit()
        self.text_print.setReadOnly(True)

        self.combobox_key = QComboBox()

        #콤보박스 항목추가
        self.combobox_key.addItem('All')
        self.combobox_key.addItem('이름')
        self.combobox_key.addItem('날짜')

        #PushButton추가
        button_add = QPushButton('add')
        button_del = QPushButton('del')
        button_show = QPushButton('Show')

        #수평방향레이아웃생성
        hlayout_option1 = QHBoxLayout() #이름,번호
        hlayout_option2 = QHBoxLayout() #년도,월,일
        hlayout_option3 = QHBoxLayout() #시간
        hlayout_option4 = QHBoxLayout() #키
        hlayout_buttons = QHBoxLayout() #버튼
        hlayout_status_bar = QHBoxLayout() #상태바

        hlayout_main = QHBoxLayout()

        hlayout_option1.addStretch(300)
        hlayout_option1.addWidget(label_name)
        hlayout_option1.addWidget(self.text_name)
        hlayout_option1.addWidget(label_phone)
        hlayout_option1.addWidget(self.text_phone)

        hlayout_option2.addStretch()
        hlayout_option2.addWidget(label_year)
        hlayout_option2.addWidget(self.text_year)
        hlayout_option2.addWidget(label_month)
        hlayout_option2.addWidget(self.text_month)
        hlayout_option2.addWidget(label_date)
        hlayout_option2.addWidget(self.text_date)

        hlayout_option3.addStretch()
        hlayout_option3.addWidget(label_hours)
        hlayout_option3.addWidget(self.text_hours)
        hlayout_option3.addWidget(label_minutes)
        hlayout_option3.addWidget(self.text_minutes)
        hlayout_option3.addWidget(label_seconds)
        hlayout_option3.addWidget(self.text_seconds)

        hlayout_option4.addStretch()
        hlayout_option4.addWidget(label_key)
        hlayout_option4.addWidget(self.combobox_key)

        hlayout_buttons.addWidget(button_add)
        hlayout_buttons.addWidget(button_del)
        hlayout_buttons.addWidget(button_show)

        hlayout_status_bar.addWidget(label_status)
        hlayout_status_bar.addWidget(self.text_status)

        #수직방향레이아웃생성
        vlayout = QVBoxLayout()
        vlayout.addLayout(hlayout_option1)
        vlayout.addLayout(hlayout_option2)
        vlayout.addLayout(hlayout_option3)
        vlayout.addLayout(hlayout_option4)
        vlayout.addLayout(hlayout_buttons)
        vlayout.addWidget(self.text_title)
        vlayout.addLayout(hlayout_status_bar)

        hlayout_main.addWidget(self.text_print)
        hlayout_main.addLayout(vlayout)

        self.setLayout(hlayout_main)
        self.show()

        #신호설정
        button_add.clicked.connect(self.goAddReservationList)
        button_del.clicked.connect(self.goDelReservationList)
        button_show.clicked.connect(self.goShowReservationList)

    def closeEvent(self, event):
        self.management.writeReservationList()

    def goAddReservationList(self):
        self.addReservationList(self.management.getReservationList())
    def goDelReservationList(self):
        self.delReservationList(self.management.getReservationList())
    def goShowReservationList(self):
        self.showReservationList(self.management.getReservationList(),self.combobox_key.currentText())

    def addReservationList(self,list):
        if self.text_name.text().strip() == '' or self.text_phone.text().strip() == '' or \
                self.text_year.text().strip() == '' or self.text_month.text().strip() == '' or self.text_date.text().strip() == '' or \
                    self.text_hours.text().strip() == '' or self.text_minutes.text().strip() == '' or self.text_seconds.text().strip() == '':
            self.text_status.setText('Please input all information')
        else:
            try:
                week = self.printDayOfTheWeek(int(self.text_year.text()), int(self.text_month.text()), int(self.text_date.text()))

                record = {'name': self.text_name.text(), 'phone': int(self.text_phone.text()),
                          'week': week, 'days': datetime.datetime(int(self.text_year.text()),int(self.text_month.text()),int(self.text_date.text()),
                                                                  int(self.text_hours.text()),int(self.text_minutes.text()),int(self.text_seconds.text()))}
                for i in list:
                    if record['days'] > i['days']:
                        gap = record['days'] - i['days']
                    else:
                        gap = i['days'] - record['days']
                    if gap < self.gap:
                        self.text_status.setText('There is another person\'s reservation in %s.' % gap)
                        break
                else:
                    list.append(record)
                    self.showReservationList(list,'All')
            except ValueError:
                self.text_status.setText('Input all information except your name in exact numbers.')

    def delReservationList(self,list):
        if self.text_name.text().strip() == '' or self.text_phone.text().strip() == '' :
            self.text_status.setText('Please input name and phone number')
        else:
            try:
                length_list = len(list)
                for p in list[:]:
                    if p["phone"] == int(self.text_phone.text()) and p["name"] == self.text_name.text() :
                        list.remove(p)
                if not len(list) - length_list:
                    self.text_status.setText('Please check name and phone number.')
                else:
                    self.showReservationList(list,'All')
            except ValueError:
                self.text_status.setText('Please input your cell phone number in numbers.')

    def showReservationList(self,list,key):
        if key == 'All':
            self.text_print.clear()
            list.sort(key=lambda x: x['days'])
            for i in list:
                self.text_print.append('이름:%s 번호:%d 시간:%s %s' % (i['name'], i['phone'], i['days'], i['week']))
            self.text_status.setText('Success!')

        elif key == '이름':
            if self.text_name.text().strip() == '':
                self.text_status.setText('Please input Name')
            else:
                found_list = []
                for p in list:
                    if p['name'] == self.text_name.text():
                        found_list.append(p)
                if not found_list:
                    self.text_status.setText('He is not on the list.')
                else:
                    self.showReservationList(found_list,'All')

        elif key == '날짜':
            if self.text_year.text().strip() == '' or self.text_month.text().strip() == '' or self.text_date.text().strip() == '':
                self.text_status.setText('Please input YYYYMMDD')
            else:
                try:
                    day = datetime.datetime(int(self.text_year.text()),int(self.text_month.text()),int(self.text_date.text()))
                    found_list = []
                    for j in list:
                        if j['days'].strftime('%Y-%m-%d') == day.strftime('%Y-%m-%d'):
                            found_list.append(j)
                    if not found_list:
                             self.text_status.setText('No one made a reservation.')
                    else:
                        self.showReservationList(found_list,'All')
                except ValueError:
                    self.text_status.setText('Please input (exact) numbers')

    def printDayOfTheWeek(self,year, month, day):
        dayOfTheWeek = ["월요일", "화요일", "수요일", "목요일", "금요일", "토요일", "일요일"]
        return dayOfTheWeek[datetime.date(year, month, day).weekday()]  # --> weekday() 가 요일에 따라 0부터 인덱스 리턴


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Reserve()
    sys.exit(app.exec_())