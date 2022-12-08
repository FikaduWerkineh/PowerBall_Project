import colorama

from power_ball_utility import *

from colorama import Fore
colorama.init(autoreset=True)
class UrLuckAndToday(YourLuckyNo,TodaysLuckyNum):

    def urLuckAndtoday(self):
        yourlucky=self.usernum
        todaywin=self.lotteryNumbers
        count=0
        for nu in yourlucky:
            if nu in todaywin:
                count += 1
        powerballNum1 = random.randint(1,10)
        # yourlucky.append(powerballNum1)

        powerballNum2 = random.randint(1,10)
        # todaywin.append(powerballNum2)

        # print(f"Your Lucky_numbers: {Fore.BLUE} {yourlucky} {Fore.RESET}")
        # print(f"Today's winNumber : {Fore.BLUE} {todaywin} {Fore.RESET}")
        # print(f'You got {count} correct numbers')
        print(f"Your Lucky_numbers:" ,Fore.BLUE+str(yourlucky),Fore.YELLOW+str(powerballNum1))
        print(f"Today's winNumber :" ,Fore.BLUE+str(todaywin), Fore.YELLOW+str(powerballNum2))
        print(f'You got {count} correct numbers')


        if powerballNum1 != powerballNum2 and count == 0:
             print ("Try again ")
        elif powerballNum1 == powerballNum2 and count == 0:
             print ("you got 4$")
        elif powerballNum1 == powerballNum2 and count == 1:
             print ("you got 4$")
        elif powerballNum1 != powerballNum2 and count == 1:
            print("try Again! ")
        elif powerballNum1 == powerballNum2 and count == 2:
             print ("you got 7$ ")
        elif powerballNum1 != powerballNum2 and count == 2:
            print("Try again!")
        elif powerballNum1 != powerballNum2 and count == 3:
             print ("you got 7$ ")
        elif powerballNum1 == powerballNum2 and count == 3:
             print ("you got 100$")
        elif powerballNum1 != powerballNum2 and count == 4:
             print ("you got 100$ ")

        elif powerballNum1 == powerballNum2 and count == 4:
             print ("you got 10,000$")
        elif powerballNum1 != powerballNum2 and count == 5:
             print("you got 1,000,000$" )
        elif powerballNum1 ==powerballNum2 and count == 5:
             print("you got $324,000,000")

# bothclas = UrLuckAndToday()
# bothclas.urLuckAndtoday()

class Mainclass(UrLuckAndToday):
    def main(self):
        print("wowow")
mainclass=Mainclass()
mainclass. main()
yourluckynum=YourLuckyNo()
yourluckynum.yourluckyno()
todayLucky=TodaysLuckyNum()
todayLucky.today_luckynum()
bothclas = UrLuckAndToday()
bothclas.urLuckAndtoday()