#internet speed logger using pyspeedtest 1.2.27
#length of  logging to be changed in line 8 (minutes=?)
#interval to be changed in row 12 (MINUTELY, HOURLY, SECONDLY)
import pyspeedtest
import csv
from dateutil import rrule
from datetime import datetime, timedelta

now = datetime.now()
finishingtime = now + timedelta(minutes=3)

for dt in rrule.rrule(rrule.MINUTELY, dtstart=now, until=finishingtime):
    with open('speedlog.csv', mode='a', newline='') as speedlog:
	    st = pyspeedtest.SpeedTest()
	    ping = st.ping()
	    dls = st.download()
	    uls = st.upload()
	    date = now.strftime("%Y-%m-%d %H:%M")
	    print ("Date: ",date , "Ping: ", ping, "Download speed: ", dls / 1000000, "Mb/s", "Upload speed: ", uls / 1000000, "Mb/s")
	    speedlogger = csv.writer(speedlog, delimiter=',', quotechar='"', quoting=csv.QUOTE_NONNUMERIC)
	    speedlogger.writerow([date, ping, dls/1000000, uls/1000000])
           



 