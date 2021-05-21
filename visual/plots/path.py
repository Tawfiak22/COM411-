import matplotlib.pyplot as plt

def coordinate():
  print("Please enter x value")
  x = int(input())
  print("Please insert y value")
  y = int(input())
  plt.plot(x,y, "r:o")

def path():
  print("Retrieving path...")
  x_values = []
  y_values = []
  for i in range(4):
    data = coordinate()
    x_values.append(data[0])
    y_values.append(data[1])
  return[x_values, y_values]

def run():
  values = path()
  plt.plot(values[0, values[1]], "r--o")
  plt.xlabel("x values")
  plt.ylabel("y values")
  plt.show()

run()     