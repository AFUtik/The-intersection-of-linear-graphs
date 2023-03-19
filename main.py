from sympy import symbols, solve
import matplotlib.pyplot as plt

figure, ax = plt.subplots()

_x = range(-10, 10)

k1, b1 = 3, 4
y1 = tuple(map(lambda x: k1 * x + b1, _x))

k2, b2 = 6, 6
y2 = tuple(map(lambda x: k2 * x + b2, _x))

def getIntersection():
  if k1 == k2: 
    return "The directs don't cross"
  
  x = symbols('x')
  f1 = k1 * x + b1
  f2 = k2 * x + b2
  f3 = f1 - f2

  sol_x = solve(f3, x)
  sol_x = sol_x[0]
  sol_y = k1 * sol_x + b1
  return sol_x, sol_y

def main():
  ax.plot(_x, y1, color="green", label='y = kx + b')
  ax.plot(_x, y2, color="blue", label='y = kx + b')

  ax.set_title("Title", fontsize=20)

  ax.legend(loc="upper left")

  ax.grid(color="black", alpha=0.2)

  plt.show()

print(getIntersection())

if __name__ == "__main__":
  main()
  
