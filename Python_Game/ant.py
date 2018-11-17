from random import *
from turtle import *

from base import vector

ant = vector(0, 0)
aim = vector(2, 0)

def wrap(value):
  return value

def draw():
  ant.move(aim)
  ant.x = wrap(ant.x)
  ant.y = wrap(ant.y)
  aim.move(random() - 0.5)

  aim.rotate(random() * 10 - 5)
  clear()
  
  goto(ant.x, ant.y)
  dot(4)
  if runing:
    ontimer(draw, 100)

setup(420, 420, 370, 0)
hideturtle()
tracer(False)
up()
runing = True
draw()
done()
