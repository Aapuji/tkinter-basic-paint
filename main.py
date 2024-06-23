import tkinter as tk
from tkinter import ttk

def draw_color(color):
    def draw(e):
        x = e.x
        y = e.y

        canvas.create_oval(
            (x - brush_size / 2, y - brush_size / 2, x + brush_size / 2, y + brush_size / 2),
            fill=color,
            outline=color
        )
    
    return draw

def change_size(e):
    global brush_size

    if e.delta > 0:
        brush_size += 2
    else:
        brush_size -= 2
    
    brush_size = min(brush_size, MAX_SIZE)
    brush_size = max(MIN_SIZE, brush_size)

# window
window = tk.Tk()
window.title('Very Basic Paint')
window.geometry('500x500')

# canvas
canvas = tk.Canvas(master=window, bg='white')
canvas.pack()

brush_size = 4
MAX_SIZE = 24
MIN_SIZE = 4
canvas.bind('<Motion>', draw_color('black'))
canvas.bind('<Shift-Motion>', draw_color('white'))
canvas.bind('<MouseWheel>', change_size)

# run
window.mainloop()
