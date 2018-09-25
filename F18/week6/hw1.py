import requests
import matplotlib.pyplot as plt
from matplotlib.dates import DateFormatter
from datetime import datetime

# https://tidesandcurrents.noaa.gov/map/index.shtml?region=Hawaii
# https://tidesandcurrents.noaa.gov/waterlevels.html?id=1612480&units=standard&bdate=20180601&edate=20180602&timezone=GMT&datum=MLLW&interval=6&action=

# 1 day
noaa_wl_url = 'https://tidesandcurrents.noaa.gov/api/datagetter?product=water_level&application=NOS.COOPS.TAC.WL&begin_date=20180601&end_date=20180602&datum=MLLW&station=1612480&time_zone=GMT&units=english&format=json'
meshlab_d2w_url = 'https://grogdata.soest.hawaii.edu/data/2/node-046/ReceptionTime,Timestamp,d2w.json?time_col=ReceptionTime&begin=1527811200&end=1527984000'

# 1 month
#noaa_wl_url = 'https://tidesandcurrents.noaa.gov/api/datagetter?product=water_level&application=NOS.COOPS.TAC.WL&begin_date=20180601&end_date=20180630&datum=MLLW&station=1612480&time_zone=GMT&units=english&format=json'
#meshlab_d2w_url = 'https://grogdata.soest.hawaii.edu/data/2/node-046/ReceptionTime,Timestamp,d2w.json?time_col=ReceptionTime&begin=1527811200&end=1530403200'


# To convert a POSIX timestamp t to a Python datetime:
datetime.utcfromtimestamp(t)
