import requests
import matplotlib.pyplot as plt
from matplotlib.dates import DateFormatter
from datetime import datetime

# https://tidesandcurrents.noaa.gov/map/index.shtml?region=Hawaii
# https://tidesandcurrents.noaa.gov/waterlevels.html?id=1612480&units=standard&bdate=20180601&edate=20180602&timezone=GMT&datum=MLLW&interval=6&action=

# 1 day
noaa_pd_url = 'https://tidesandcurrents.noaa.gov/api/datagetter?product=predictions&application=NOS.COOPS.TAC.WL&begin_date=20180601&end_date=20180602&datum=MLLW&station=1612480&time_zone=GMT&units=english&interval=&format=json'
noaa_wl_url = 'https://tidesandcurrents.noaa.gov/api/datagetter?product=water_level&application=NOS.COOPS.TAC.WL&begin_date=20180601&end_date=20180602&datum=MLLW&station=1612480&time_zone=GMT&units=english&format=json'
meshlab_d2w_url = 'https://grogdata.soest.hawaii.edu/data/2/node-046/ReceptionTime,Timestamp,d2w.json?time_col=ReceptionTime&begin=1527811200&end=1527984000'

# 1 month
#noaa_pd_url = 'https://tidesandcurrents.noaa.gov/api/datagetter?product=predictions&application=NOS.COOPS.TAC.WL&begin_date=20180601&end_date=20180630&datum=MLLW&station=1612480&time_zone=GMT&units=english&interval=&format=json'
#noaa_wl_url = 'https://tidesandcurrents.noaa.gov/api/datagetter?product=water_level&application=NOS.COOPS.TAC.WL&begin_date=20180601&end_date=20180630&datum=MLLW&station=1612480&time_zone=GMT&units=english&format=json'
#meshlab_d2w_url = 'https://grogdata.soest.hawaii.edu/data/2/node-046/ReceptionTime,Timestamp,d2w.json?time_col=ReceptionTime&begin=1527811200&end=1530403200'


def feet2meter(foot):
    return 0.3048*foot

def d2w2m(x):
    return (1400 - x)/1e3


# noaa
r = requests.get(noaa_wl_url)
r = r.json()
dtnoaa = [datetime.strptime(d['t'], '%Y-%m-%d %H:%M') for d in r['data']]
feet = [float(d['v']) for d in r['data']]
meternoaa = [feet2meter(f) for f in feet]

# meshlab
r = requests.get(meshlab_d2w_url)
r = r.json()
rt, ts, mm = zip(*r)
dtmesh = [datetime.utcfromtimestamp(t) for t in ts]
metermesh = [d2w2m(m) for m in mm]


# plot
plt.figure(figsize=(16, 9))
ax = plt.subplot(1, 1, 1)

# the beef
ax.plot_date(dtnoaa, meternoaa, 'r.:', label='NOAA', alpha=0.3)
ax.plot_date(dtmesh, metermesh, 'b.:', label='MESHLAB', alpha=0.3)

ax.set_title('who cares')
ax.set_xlabel('Datetime (GMT)')
ax.set_ylabel('MLLW, meter')
ax.legend(loc=2)
ax.grid(True)
plt.tight_layout()
plt.gcf().autofmt_xdate()
#plt.savefig('haha.png', dpi=300)
plt.show()
