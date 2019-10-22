#2018/11/15
#自訂時間&排程任務



# Schedule Library imported
import schedule
import time
# Setting up the functions
def morning_yoga():
print("Get up and do yoga")
def work():
print("Get ready for work!")
def lunch_time():
print("Have healthy lunch!")
def break_time():
print("relax for sometime!")
def drink_water():
print("Stay hydrated")
def bedtime():
print("Go to bed early!")
def visit_market():
print("Go to the market!")
#Scheduling the tasks
#Every day at 5:00 am morning_yoga() is called
schedule.every().day.at("05:00").do(morning_yoga)
#Every 30 mins drink_water() is called
schedule.every(30).minutes.do(drink_water)
#Every 3 hour break_time() is called
schedule.every(3).hour.do(break_time)
#Every day at 21:00 pm bedtime() is called
schedule.every().day.at("21:00").do(bedtime)
#Every wednesday at 19.30 pm visit_market()is called
schedule.every().wednesday.at("19:30").do(visit_market)
# Creating a loop so that the scheduling task keeps on running all time
while True:
#Checks whether the scheduled task is running or not
schedule.run_pending()
time.sleep(1)
