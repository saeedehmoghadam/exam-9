class hour():
    
    def __init__(self, hh, mm, ss):
        self.hour = hh
        self.minute = mm
        self.second = ss

        self.hour1 = hh
        self.minute1 = mm
        self.second1 = ss
        
    def sum(self):
        time ={}
        time.second = self.second + self.second1
        time.minute = self.minute + self.minute1
        time.hour = self.hour + self.hour1
        
        if time.second >= 60:
            time.second -= 60
            time.minute += 1
        
        if time.minute >= 60:
            time.minute -= 60
            time.hour += 1
            
        return time
    
    def sub(self, mehman):
        time = {}
        
        if self.second >= self.second1:
            time.second = self.second - self.second1
        else:
            self.second += 60
            self.minute -= 1
            time.second = self.second - self.second1
        
        if self.minute >= self.minute1:
           time.minute = self.minute - self.minute1
        else:
            self.minute += 60
            self.hour -= 1
            time.minute = self.minute - self.minute1
        
        time.hour = self.hour - self.hour1
        if time.hour < 0:
            time.hour += 24
        
        return time
    
    def hour_to_sec(self):
        time = {}
        time.hour = 0
        time.minute = 0
        time.second = self.second + self.minute * 60 + self.hour * 3600
        return time
    
    def sec_to_hour(self):
        time = {}
        
        time.hour = self.second // 3600
        self.second %= 3600

        time.minute = self.second // 60
        self.second %= 60

        time.second = self.second
        
        return time
    
    def show(self):
        print(self.hour, ':', self.minute, ':', self.second)

h_1 = int(input('please typr yore hour: '))
m_1 = int(input('please typr yore minute: '))
s_1 = int(input('please typr yore second: '))

h_2 = int(input('please typr yore hour1: '))
m_2 = int(input('please typr yore minute1: '))
s_2 = int(input('please typr yore second1: '))

    
a = (h_1, m_1, s_1)
b = (h_2, m_2, s_2)

c1 = a.sum(b)
c1.show()

c2 = a.sub(b)
c2.show()

c3 = a.hour_to_sec()
c3.show()

c4 = c3.sec_to_hour()
c4.show()
