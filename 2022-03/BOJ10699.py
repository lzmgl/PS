import datetime
d=datetime.datetime.utcnow() + datetime.timedelta(hours=9)
m='{:02d}'.format(d.month)
print(f"{d.year}-{m}-{d.day}")