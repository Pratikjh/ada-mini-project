def main():    
    a =  [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
       [11, 12, 13, 14, 15, 16, 17, 18, 19, 20],
       [21, 22, 23, 24, 25, 26, 27, 28, 29, 30],
       [31, 32, 33, 34, 35, 36, 37, 38, 39, 40]] 
    for row in a:
        for elem in row:
            print(elem, end=' ')
        print()
    for a in range(1,10):
        cost=20
    if __name__ == "__main__":
        main()