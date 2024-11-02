class Time:
    def __init__(self, hours, minutes, seconds):
        self.hours = self.check_hour(hours)
        self.minutes = self.check(minutes)
        self.seconds = self.check(seconds)


    @staticmethod
    def check_hour(hour):
        if hour >= 0 and hour <= 23:
            return hour
        else: 
            raise ValueError("Hour out of bound lol")

    @staticmethod
    def check(time):
        if time >= 0 and time <= 59:
            return time
        else: 
            raise ValueError("Time out of bound lol")
        

    def __lt__(self, obj):
        return (self.hours, self.minutes, self.seconds) < (obj.hours, obj.minutes, obj.seconds)

    def __gt__(self, obj):
        return (self.hours, self.minutes, self.seconds) > (obj.hours, obj.minutes, obj.seconds)

    def __eq__(self, obj):
        return (self.hours, self.minutes, self.seconds) == (obj.hours, obj.minutes, obj.seconds)

c1 = Time(22, 38, 59)
c2 = Time(22, 39, 59)
print(c1 == c2)
print(c1 > c2)
print(c1 < c2)
