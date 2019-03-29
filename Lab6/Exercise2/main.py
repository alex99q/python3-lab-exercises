import turtle
from draw import Draw

window = turtle.Screen()
canvas = Draw()

canvas.draw_triangle()

canvas.clear()

canvas.draw_rectangle()

canvas.clear()

canvas.draw_pixel("red")

canvas.clear()

canvas.draw_centered_line(400)

canvas.clear()

canvas.draw_centered_circle(100)

window.mainloop()