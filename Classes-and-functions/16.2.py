#Write a boolean function called is_after that takes two Time objects, t1 and t2, and returns True if t1 follows t2 chronologically and False otherwise. 


class Time(object) :
  "time"
time=Time()
time1=Time()
time.hour=1
time.minute=23
time.sec=12
time1.hour=2
time1.minute=23
time1.sec=12
def is_after(t1,t2) :
  print t1>t2
is_after(time,time1)
