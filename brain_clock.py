

from time import sleep




container = [
    ['O' for i in range(1)],
    ['O' for i in range(4)],
    ['O' for i in range(4)],
    ['O' for i in range(11)],
    ['O' for i in range(4)]
]



input_time = '12:56:02'


hours,minutes,secconds = int(input_time.split(':')[0]),int(input_time.split(':')[1]),int(input_time.split(':')[2])

if int(secconds) % 2 == 0:
    container[0] = 'Y'
else:container[0] = 'O'


ostatok_hours = hours - hours//5*5
ostatok_minutes = minutes - minutes//5*5


for i in range(hours//5):
    container[1][i] = 'R'

for i in range(ostatok_hours):
    container[2][i] = 'R'


for i in range(minutes//5):
    # print((i+1) % 3,i)
    if (i+1) % 3 == 0:
        container[3][i] = 'R'
    else:
        container[3][i] = 'Y'

for i in range(ostatok_minutes):
    container[4][i] = 'y'

for i in container:
    for j in i:
        print(j,end='')
    print()





