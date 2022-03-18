import datetime
d=datetime.datetime.utcnow() + datetime.timedelta(hours=9)
y=d.year
m=d.month
dd=d.day
m='{:02d}'.format(m)
print(f"{y}-{m}-{dd}")