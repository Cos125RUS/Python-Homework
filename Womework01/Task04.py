#Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).

quarter = int(input("Enter the quarter: "))

if quarter < 1 or quarter > 4:
    print("Input error!")
else:
    if quarter == 1:
        print("x = 0 - +∞\ny = 0 - +∞")
    elif quarter == 2:
        print("x = 0 - +∞\ny = 0 - -∞")
    elif quarter == 3:
        print("x = 0 - -∞\ny = 0 - -∞")
    else:
        print("x = 0 - -∞\ny = 0 - +∞")