# the requests library, list comprehension, datetime, matplotlib plotting
import requests
import matplotlib.pyplot as plt
from matplotlib.dates import DateFormatter
from datetime import datetime

# https://tidesandcurrents.noaa.gov/map/index.shtml?region=Hawaii
# https://tidesandcurrents.noaa.gov/waterlevels.html?id=1612480&units=standard&bdate=20180601&edate=20180602&timezone=GMT&datum=MLLW&interval=6&action=


url = 'https://tidesandcurrents.noaa.gov/api/datagetter?product=water_level&application=NOS.COOPS.TAC.WL&begin_date=20180601&end_date=20180602&datum=MLLW&station=1612480&time_zone=GMT&units=english&format=json'


# noaa
r = requests.get(url).json()
dt = [datetime.strptime(d['t'], '%Y-%m-%d %H:%M') for d in r['data']]       # <- list comprehension
feet = [float(d['v']) for d in r['data']]


# plot
plt.figure(figsize=(16, 9))
ax = plt.subplot(1, 1, 1)

ax.plot_date(dt, feet, 'r.:')

ax.set_title('who cares')
ax.set_xlabel('Datetime (GMT)')
ax.set_ylabel('MLLW, feet')
ax.legend(loc=2)
ax.grid(True)
plt.tight_layout()
plt.gcf().autofmt_xdate()
#plt.savefig('haha.png', dpi=300)
plt.show()
