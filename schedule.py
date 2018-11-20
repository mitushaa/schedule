#2018/11/15
#自訂時間&排程任務


import datetime,os,platform
'''
def run_Task():
         os_platfrom = platform.platform()
         if os_platfrom.startswith('Darwin'):
                  print 'this is mac os system'
                  os.system('ls')
         elif os_platfrom.startswith('Window'):
                  print 'this is window system'
                  os.system('dir')
                  os.system('pause')
'''
def run_Task():
         print "successful"

def timerFun(sched_Timer):
         flag = 0
         while True:
                  now = datetime.datetime.now()
                  now = now.strftime('%Y-%m-%d %H:%M:%S')
                  #now=datetime.datetime.strptime(now,'%Y-%m-%d %H:%M:%S')
                  sched = sched_Timer.strftime('%Y-%m-%d %H:%M:%S')
                  if (now == sched) & (flag == 0):
                           run_Task()
                           flag = 1
                  elif (now > sched):
                           print 'Time has passed'
                           break;
                  else:
                           if flag==1:
                                    sched_Timer = sched_Timer+datetime.timedelta(seconds=5)
                                    
if __name__ == '__main__':
         sched_Timer = datetime.datetime(2018,11,19,9,33,00)
         #sched_Timer_display = sched_Timer.strftime('%Y-%m-%d %H:%M:%S')
         print 'run the time task at {0}'.format(sched_Timer)
         timerFun(sched_Timer)
