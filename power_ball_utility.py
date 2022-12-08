

import random
class TodaysLuckyNum:
    lotteryNumbers = []
    def today_luckynum(self):


        for i in range (0,5):
            number = random.randint(1,20)
            self.lotteryNumbers.append(number)


        self.lotteryNumbers.sort()

import random
class YourLuckyNo:
    usernum = []
    def yourluckyno(self):

        for i in range (0,5):
            num = random.randint(1,20)
            self.usernum.append(num)
        self.usernum.sort()



