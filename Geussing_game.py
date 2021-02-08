from tkinter import *
from PIL import Image, ImageTk
import random

answer = random.randint(20, 50)
attempts = 0
answer1 = answer - 10
answer2 = answer + 10


def check_answer():
    global attempts
    global text

    attempts += 1
    try:
        guess = int(entry_window.get())

    except ValueError:
        text.set ("Please enter a Number that is in the range of 20-50")
        attempts -= 1

    if answer == guess:
        text.set("| Congratulations! You WON!!! | You took " + str(attempts) + " attempts |")
        btn_check.pack_forget()

    elif guess > 50:
        text.set("Please enter a Number that is in the range of 20-50")
        attempts -= 1

    elif guess < 20:
        text.set("Please enter a Number that is in the range of 20-50")
        attempts -= 1

    elif guess == str:
        text.set("Please enter a Number that is in the range of 20-50")
        attempts -= 1

    elif guess == float:
        text.set("Please enter a Number that is in the range of 20-50")
        attempts -= 1


    elif guess < answer1:
        text.set("Your guess is too low. Try again.")

    elif guess < answer:
        text.set("Your guess is low. Try again")

    elif guess > answer2:
        text.set("Your guess is too high. Try again")

    elif guess > answer:
        text.set("Your guess is high. Try again")


    else:
        text.set("ERROR")
        attempts -= 1




    return

root = Tk()

root.title("PRANAV'S GUESSING GAME")

root.geometry("500x150")

load = Image.open ('C:\\Users\Pranav\\Desktop\\GUESSING GAME!!!\\Python Pictures\\X.jpg')

render = ImageTk.PhotoImage(load)
img = Label(root,image = render)
img.place(x = 0, y = -200)
#img1 = PhotoImage(file="C:\\Users\\Pranav\\Desktop\\GUESSING GAME!!!\\Python Pictures\\Button.png")

label = Label(root, text="Guess the number between 20 and 50!", bg = "white")
label.pack()

#label.wm_attributes("-transparentcolor", 'grey')

entry_window = Entry(root,width=40, borderwidth=4)
entry_window.pack()

btn_check = Button(root, text="Check", command=check_answer, bg="white")
btn_check.pack()

btn_quit = Button(root, text="Quit", command=root.destroy, bg="white")
btn_quit.pack()

text = StringVar()
text.set("Guess a Number in the Box!")

guess_attempts=Label(root, textvariable=text, bg="white")
guess_attempts.pack()

root.resizable(False, False)


root.mainloop()









