from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#fde7c3"
WHITE = "#ffeaea"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

label = Label(text="Timer", fg=GREEN, font=(FONT_NAME, 35, "bold"), bg=YELLOW)
label.grid(column=1, row=0)

canvas = Canvas(width=200, height=223, bg=YELLOW, highlightthickness=0)
image = PhotoImage(file="tomato.png")
canvas.create_image(100, 110, image=image)
canvas.create_text(100, 130, text="00:00", fill=WHITE, font=(FONT_NAME, 28, "bold"))
canvas.grid(column=1, row=1)

button_start = Button(text="Start", font=(FONT_NAME, 10, "normal"))
button_start.grid(column=0, row=2)

button_stop = Button(text="Stop", font=(FONT_NAME, 10, "normal"))
button_stop.grid(column=2, row=2)

check = Label(text="✓", fg=GREEN, font=(FONT_NAME, 20, "bold"), bg=YELLOW)
check.grid(column=1, row=3)

window.mainloop()
