# # Schedule Library imported 
# import schedule
# import time


# def info():
#     print("I am Deepak.")
#     # print(schedule.next_run())


# def internship():
#     print(schedule.idle_seconds())
#     print("Intern in 1Rivet.")
#     # print(schedule.next_run())


# schedule.every(5).seconds.do(info)
# schedule.every(10).seconds.do(internship)
# while True:
#     # Checks whether a scheduled task
#     # is pending to run or not
#     schedule.run_pending()
#     schedule.cancel_job(internship)
#     # schedule.idle_seconds()
#     time.sleep(1)

import webbrowser
import schedule


def myinfo():
    print("I am Deepak.")
    # webbrowser.open('http://net-informations.com', new=2)
    # webbrowser.open('www.google.co.in', new=2)


schedule.every(5).seconds.do(myinfo)

flag = True
while flag == True:
    schedule.run_pending()

