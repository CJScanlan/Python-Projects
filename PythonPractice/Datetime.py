from datetime import *
import pytz

tzP = pytz.timezone('US/Pacific')
tzE = pytz.timezone('Europe/London')
tzNY = pytz.timezone('US/Eastern')

Portland = datetime.now(tzP).time()
London = datetime.now(tzE).time()
NewYork = datetime.now(tzNY).time()


start = time(9,0,0)
end = time(17,0,0)



def Hours(start, end, location,name):
    if location >= start and location <= end:
        print("{} branch is open. Current time is {}:{}".format(name,location.hour,location.minute))
    else:
        print("{} branch is closed. Current time is {}:{}".format(name,location.hour,location.minute))


print("Hours: 9:00 to 17:00")
Hours(start,end,Portland,'Portland')
Hours(start,end,London,'London')
Hours(start,end,NewYork,'New York')


