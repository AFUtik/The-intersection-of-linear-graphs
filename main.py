from sympy import symbols, solve
import matplotlib.pyplot as plt

figure, ax = plt.subplots()

_x = range(-10, 10)

k1, b1 = 2, 5
y1 = tuple(map(lambda x: k1 * x + b1, _x))

k2, b2 = 3, 2
y2 = tuple(map(lambda x: k2 * x + b2, _x))

def getIntersection():
  x = symbols('x')
  if k1 == k2: 
    print("The directs don't cross")
    return
  f1 = k1 * x + b1
  f2 = k2 * x + b2
  f3 = f1 - f2

  sol_x = solve(f3, x)
  sol_x = sol_x[0]
  sol_y = k1 * sol_x + b1
  return sol_x, sol_y

print(getIntersection())

ax.plot(_x, y1, color="green", label='y = kx + b')
ax.plot(_x, y2, color="blue", label='y = kx + b')

ax.set_title("Title", fontsize=20)

ax.legend(loc="upper left")

ax.grid(color="black", alpha=0.2)

plt.show()