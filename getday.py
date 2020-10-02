import json
import datetime

with open('whmsab.json') as f:
    whms = json.load(f)

dt = datetime.datetime.today()
today = dt.day

print(whms)
print(today)

# myDayType = whms.get("Daytype")
# print(myDayType)
# for attrs in whms['theday']['Daytype']:
#     if attrs['day'] == today:
#         daytype = attrs['Daytype']
#         print('Today is ' + daytype + ' day.')
#         break
