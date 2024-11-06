class Clock:
    def __init__(self, hour, min, sec):
        self.hour = hour
        self.min = min
        self.sec = sec

    def __str__(self):
        return "{}:{}:{}".format(self.hour, self.min, self.sec)

    def tick(self, n):
        for i in range(n):
            self.sec += 1
            if self.sec >= 60:
                self.sec = 0
                self.min += 1
                if self.min >= 60:
                    self.min = 0
                    self.hour += 1
                    if self.hour >= 24:
                        self.hour = 0

    def set(self, set_hour, set_min, set_sec):
        self.hour = set_hour
        self.min = set_min
        self.sec = set_sec


clock = Clock(1, 30, 48)
clock.tick(15)
print(clock)

clock.set(2, 3, 58)
clock.tick(5)
print(clock)

clock.set(23, 59, 57)
clock.tick(5)
print(clock)
