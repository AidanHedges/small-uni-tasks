#Produce a table for the values of parabola (2x^2 -7x +3) in range of x= -7 to +9​ 
for x in [i for i in range(-7, 10)]:
    y = 2 * (x ** 2) - 7 * x + 3
    print(f"x: {x}, y: {y}")
