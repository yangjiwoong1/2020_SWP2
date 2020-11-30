import pickle

class Management:

    def __init__(self,fileName):
        self.listFile = fileName

    def readReservationList(self):
        #reservationList객체 생성(피클모듈로 읽음)
        try:
            fH = open(self.listFile, 'rb')
            self.reservationList =  pickle.load(fH)
        except FileNotFoundError as e:
            self.reservationList = [] #[{이름,번호,요일,날짜,시간} 의 사전을 원소로 갖는 리스트]
        fH.close()

    def writeReservationList(self):
        fH = open(self.listFile, 'wb')
        pickle.dump(self.reservationList, fH)
        fH.close()

    def getReservationList(self):
        return self.reservationList