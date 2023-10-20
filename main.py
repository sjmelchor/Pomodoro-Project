from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
#formatting constants below!
PINK_1 = "#FF9494"
CREAM = "#Fbf9f3"
GREEN="#90bb48"
BUTTON_FONT=("Futura", 16)


#constant values
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

#global variables
reps = 0
timer=None

# ---------------------------- TIMER RESET ------------------------------- #

def reset():
    global reps
    reps = 0
    timer_label.config(text="Buon giorno, pomodoro!", font=("Futura", 42, "normal"), bg=CREAM, fg=GREEN, padx=20, pady=20)
    canvas.itemconfig(timer_text, text="00:00")
    checkmark_label["text"]=""
    window.after_cancel(timer)

# ---------------------------- TIMER MECHANISM ------------------------------- #

def start_timer():

    global reps

    reps +=1
    print(reps)

    if reps % 8 == 0:
        count_down(LONG_BREAK_MIN *60)
        timer_label.config(text="Time for a long break!", fg=PINK_1)

    elif reps % 2 == 0:
        count_down(SHORT_BREAK_MIN *60)
        timer_label.config(text="Take 5!", fg=PINK_1)

    else:
        count_down(WORK_MIN*60)
        timer_label.config(text="WORK", fg=GREEN)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def count_down(count):
    global reps
    global timer
    minutes = math.floor(count/60)
    seconds = count % 60

    if seconds < 10:
        seconds=f"0{seconds}"
    
    if count > 0:
        timer = window.after(1000, count_down, count-1)
        canvas.itemconfig(timer_text, text=f"{minutes}:{seconds}")
    else:
        start_timer()
        if reps > 8:
            window.after_cancel(timer)
        if reps % 2 !=  0:
            checkmark_label["text"]+="✔"




# ---------------------------- UI SETUP ------------------------------- #

#window config
window=Tk()
window.title("Pomodoro")
window.config(padx=20, pady=20, bg=CREAM)

#canvas config

canvas=Canvas(width=220, height=250, bg=CREAM, highlightthickness=0)

tomato_img=PhotoImage(file="tomato.png")
#image needs x and y positions on the canvas
canvas.create_image(110, 125, image=tomato_img)

timer_text = canvas.create_text(110, 150, font=("Futura", 40, "normal"), text="00:00", fill="white")
canvas.grid(column=1, row=1)


start_button=Button(text="START", font=BUTTON_FONT, highlightthickness=0, fg="#0e1700", command=start_timer)
start_button.grid(column=0, row=2)

reset_button=Button(text="RESET", font=BUTTON_FONT, highlightthickness=0, fg="#0e1700", command=reset)
reset_button.grid(column=2, row=2)

timer_label=Label(text="Buon giorno, pomodoro!", font=("Futura", 42, "normal"), bg=CREAM, fg=GREEN, padx=20, pady=20)
timer_label.grid(row=0, column=1)

checkmark_label=Label(text = "", font=(90), bg=CREAM, fg=GREEN)
checkmark_label.grid(column=1, row=2)


window.mainloop()
