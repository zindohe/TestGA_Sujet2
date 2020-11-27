# -*- coding: utf-8 -*-
# @Author: Z.BOUDAOUD
# @Email: zinedddine97@gmail.com

from scheduler.script import Script


if __name__ == '__main__':
    print("Choose a day to run the script :\n1 - Monday\n2 - Tuesday\n3 - Wednesday\n4 - Thursday\n5 - Friday\n6 - Saturday\n7 - Sunday")
    day = int(input())
    print("Type an hour (0-23) :")
    hour = input()
    script = Script(0)
    script.schedule(day, hour)



