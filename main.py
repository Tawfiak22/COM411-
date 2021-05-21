import matplotlib.pyplot as plt
import matplotlib.animation as animation 

<<<<<<< HEAD
def animate(frame):
 print(f"Frame number is {frame}")

def run():
 fig, ax = plt.subplots()
 some_animation = animation.FuncAnimation(fig, animate, frames = 10, interval = 100)  

plt.show()
=======
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
>>>>>>> 428de3e23c1b88849c2beea7998783e480546fc8

run ()