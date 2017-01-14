import sys
import datetime
date_format = "%Y-%m-%d"

if len(sys.argv) <= 1:
  print 'Usage: balivoa.py ' + date_format 
  print 'Example: balivoa.py 2016-11-24'

arrival_date = datetime.datetime.strptime(sys.argv[1], date_format) 
last_stay_date = arrival_date + datetime.timedelta(days=59)
print "last stay day: " + last_stay_date.strftime(date_format)
