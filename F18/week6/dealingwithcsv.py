from datetime import datetime
import matplotlib.pyplot as plt


filename = 'CO-OPS__1612480__hr.csv'

D = []
with open(filename) as fin:
    for line in fin:
        r = line.strip().split(',')
        try:
            #print(r)
            #print(datetime.strptime(r[0], '%Y-%m-%d %H:%M'))
            #print(float(r[1]))
            D.append([datetime.strptime(r[0], '%Y-%m-%d %H:%M'), float(r[1])])
        except ValueError:
            pass

# plotting
# matplotlib wants an X and a Y, not a list of [x1, y1], [x2, y2]...
D = list(zip(*D))
plt.plot_date(D[0], D[1], ':.')
plt.show()
