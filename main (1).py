a = [[1,  2,  3,  4,  5,  6,  7,  8,  9, 10],
   [11, 12, 13, 14, 15, 16, 17, 18, 19, 20],
   [21, 22, 23, 24, 25, 26, 27, 28, 29, 30],
   [31, 32, 33, 34, 35, 36, 37, 38, 39, 40]] 
for row in a:
    for elem in row:
        print(elem, end=' ')
    print()

print('cost per seat in rows:')
print('first row=300')
print('second row=200')
print('third row=100')
print('fourth row=100')
n=int(input('enter the number of seats:'))
for i in range(n):
    seatn=int(input('enter the seat number: '))
if(seatn<11):
    cost=300
elif(seatn>10 and seatn<21):
    cost=200
elif(seatn>20 and seatn<31):
    cost=100
elif(seatn>30 and seatn<41):
    cost=100
print('cost of seat=' '',cost)