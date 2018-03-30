print('\t\t\t\t\tWELCOME TO SEAT BOOKING SYSTEM')
from array import *
a = [[1,  2,  3,  4,  5,  6,  7,  8,  9, 10],
   [11, 12, 13, 14, 15, 16, 17, 18, 19, 20],
   [21, 22, 23, 24, 25, 26, 27, 28, 29, 30],
   [31, 32, 33, 34, 35, 36, 37, 38, 39, 40]] 
for row in a:
    for elem in row:
        print(elem, end=' ')
    print()
def totalcost(arr,i,n):
    
    if(i>=n):
       return 0 
    else: 
        
        if(arr[i]<11):
            cost=300
        elif(arr[i]>10 and arr[i]<21):
            cost=200
        elif(arr[i]>20 and arr[i]<31):
            cost=100
        elif(arr[i]>30 and arr[i]<41):
            cost=100
        
        return cost+totalcost(arr,i+1,n)
    

print('cost per seat in rows:')
print('first row=300')
print('second row=200')
print('third row=100')
print('fourth row=100')
n=int(input('enter the number of seats:'))
import array
arr = []
for i in range(0,n):
    seatn=int(input('enter the seat number: '))
    if(seatn>40):
        print('sorry! no such seat available')
    else:
        arr.append(seatn)
r=totalcost(arr,0,n)

print('selected seats are:')
for i in range(n):
    print(' ',arr[i])
print('total cost of selected seats:' '',r)
            