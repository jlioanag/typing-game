class Test:
    def __init__(self):
        self.count = 0
        self.wpm = 0

    def inc_count(self):
        self.count += 10

    def get_count(self):
        return self.count

    def get_wpm(self):
        self.wpm = (self.get_count() / (90.0/60.0))
        print(self.wpm)


t = Test()
t.inc_count()
t.get_wpm()
