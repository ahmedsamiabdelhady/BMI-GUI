from tkinter import *

window = Tk()
window.title("BMI")
window.minsize(500, 300)
window.config(padx=115, pady=75)

#Button
def clicked_button():
    weight = float(input_w.get())
    height = float(input_h.get())
    BMI = weight / height ** 2
    result.config(text= f"Your BMI is {round(BMI, 1)}")
    if BMI < 18.5:
        condition.config(text= "Underweight")
    elif BMI >= 18.5 or BMI <= 24.9:
        condition.config(text= "Normal weight")
    elif BMI >= 25 or BMI <= 29.9:
        condition.config(text= "Overweight")
    elif BMI >= 30 or BMI <= 39.9:
        condition.config(text= "Obese")
    elif BMI > 40:
        condition.config(text= "Morbidly Obese")

button = Button(text="Calculate", command=clicked_button)
button.grid(column=0, row=5)

#Weight
weight = Label(text= "Weight", font=("Arial", 15, "bold"))
weight.grid(column=0, row=1)

#Entry
input_w = Entry(width=5)
input_w.grid(column=1, row=1)

#kg
kg = Label(text= "kg", font=("Arial", 10))
kg.grid(column=2, row=1)

#Height
height = Label(text= "Height", font=("Arial", 15, "bold"))
height.grid(column=0, row=2)

#Entry
input_h = Entry(width=5)
input_h.grid(column=1, row=2)

#m
m = Label(text= "m", font=("Arial", 10))
m.grid(column=2, row=2)

#result label
result = Label(text= "Your BMI is 0", font=("Arial", 15, "bold"))
result.grid(column=0, row=3)

#Body Condition
condition =  Label(text= " ", font=("Arial", 10, "bold"))
condition.grid(column=0, row=4)







window.mainloop()

