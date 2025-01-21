def twoDigits(x):
    val = str(x)
    if len(val) == 1:
        val = "0" + val
    return val


class Timer:
    def __init__(self, hours=0, minutes=0, seconds=0):
        self.__hours = hours
        self.__minutes = minutes
        self.__seconds = seconds

    def __str__(self):
        return f"{twoDigits(self.__hours)}:{twoDigits(self.__minutes)}:{twoDigits(self.__seconds)}"

    def nextSecond(self):
        if self.__seconds == 59:
            self.__seconds = 0
            if self.__minutes == 59:
                self.__minutes = 0
                if self.__hours == 23:
                    self.__hours = 0
                else:
                    self.__hours += 1
            else:
                self.__minutes += 1
        else:
            self.__seconds += 1
        self.__str__()

    def prevSecond(self):
        if self.__seconds == 0:
            self.__seconds = 59
            if self.__minutes == 0:
                self.__minutes = 59
                if self.__hours == 0:
                    self.__hours = 23
                else:
                    self.__hours -= 1
            else:
                self.__minutes -= 1
        else:
            self.__seconds -= 1
        self.__str__()


timer = Timer(23, 59, 59)
print(timer)
timer.nextSecond()
print(timer)
timer.prevSecond()
print(timer)
