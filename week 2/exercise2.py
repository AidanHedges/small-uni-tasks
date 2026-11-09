# Produce a table for the values of the parabola (2x^2 - 7x + 3) in the range x = -7 to +9
print(f"{'x':>6} {'y':>12}")
print('-' * 20)

for step in range(-28, 37):
    x = step / 4
    y = 2 * (x ** 2) - 7 * x + 3
    print(f"{x:>6g} {y:>12.2f}")