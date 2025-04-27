from tkinter import *
import time
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(time_label,text= "00:00")
    canvas.itemconfig(state,text= "Timer")
    check_pic.config(text = " ")
    global reps
    reps= 0
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():

    global reps
    reps +=1
    work_sec = WORK_MIN*60
    short_sec = SHORT_BREAK_MIN*60
    long_sec = LONG_BREAK_MIN*60

    match reps:
            case 1|  3 | 5 | 7 :
                countdown(work_sec)
                state.config(text = "Work", fg = GREEN)
            case 8:
                countdown(long_sec)
                state.config(text = "Long break", fg = RED)
            case 2|4|6:
                countdown(short_sec)
                state.config(text = "Short break", fg = PINK)
            case _ :
                pass



# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def countdown(seconds):
    global timer
    count_min = math.floor(seconds/ 60)
    count_seconds= seconds % 60

    if count_seconds < 10:
        count_seconds = f"0{count_seconds}"
        
    canvas.itemconfig(time_label,text =f"{count_min}: {count_seconds}")
    if seconds > 0:
        timer = window.after(1000,countdown , seconds-1)
    else:
        start_timer()
        marks = " "
        for _ in range(math.floor(reps/2)):
            marks += "✅"
        check_pic.config(text = marks)

# ---------------------------- UI SETUP ------------------------------- 

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50 , bg=YELLOW)
window.after(1000)

#setting image
canvas = Canvas(width = 200 , height = 224, bg = YELLOW, highlightthickness = 0)
tomato_pic = PhotoImage(file= "tomato.png")
canvas.create_image(100, 112, image = tomato_pic)
time_label = canvas.create_text(100,130, text = "00:00", fill = "white", font= (FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

check_pic = Label(text=" ",fg= GREEN , bg = YELLOW , font= (FONT_NAME, 20, "bold") )
check_pic.grid(column=1 , row= 3 )
#Label

state = Label(text= "Timer", fg = GREEN , font= (FONT_NAME,30,"bold"), bg = YELLOW)
#setting buttons in overlay
state.grid(column= 1, row = 0)

start= Button(text = "Start", command = start_timer)
start.grid(column=0, row=2)
reset = Button(text="Reset", command = reset_timer)
reset.grid( column=2, row= 2)



window.mainloop()
