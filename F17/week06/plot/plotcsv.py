# Plot a CSV file.
#
# See also:
# The read_csv() function in the pandas library
# https://pandas.pydata.org/pandas-docs/stable/generated/pandas.read_csv.html
# Stanley H.I. Lio
# hlio@hawaii.edu
import matplotlib.pyplot as plt

t = []
s = []
for line in open('data.csv','r'):
    line = line.strip().split(',')
    t.append(float(line[0]))
    s.append(float(line[1]))

    
print(t)
print()
print(s)


plt.plot(t,s)

plt.xlabel('take the cannoli')
plt.ylabel('leave the gun')
plt.title('why eagles can\'t swim')
plt.grid(True)
#plt.savefig('bourgeoisie.png')
plt.show()
