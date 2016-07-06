#date_time

from datetime import datetime

now = datetime.now()
print now
print now.year
print now.month
print now.day

print '%s/%s/%s' % (now.year, now.month, now.day)

#Pretty Time
print '%s:%s:%s' % ( now.hour, now.minute, now.second)

#Grand Finale
print '%s/%s/%s %s:%s:%s' % (now.month, now.day, now.year, now.hour, now.minute, now.second)