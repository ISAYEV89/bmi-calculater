import tkinter

window = tkinter.Tk()
window.title("BMI calculator")
window.minsize(width=450, height=450)
window.config(pady=20, padx=20)


label_kg = tkinter.Label(text="Enter Your weight (kg)", font=('Arial', 16, "normal"))
label_kg.config(pady=10, padx=10)
label_kg.pack()

entry_kg = tkinter.Entry(width=20)
entry_kg.focus()
entry_kg.pack()

label_cm = tkinter.Label(text="Enter Your height (cm)", font=('Arial', 16, "normal"))
label_cm.config(pady=10, padx=10)
label_cm.pack()

entry_cm = tkinter.Entry(width=20)
entry_cm.pack()


def show_results(bmi):
    if (bmi < 18.5):
        label_message.configure(text=f"Your BMI is {bmi}. Under Weight ")
    elif (bmi >= 18.5 and bmi < 25):
        label_message.configure(text=f"Your BMI is {bmi}. Normal ")
    elif (bmi >= 25 and bmi < 30):
        label_message.configure(text=f"Your BMI is {bmi}. Over Weight ")
    elif (bmi >= 30 and bmi < 35):
        label_message.configure(text=f"Your BMI is {bmi}. Obesity ( Class I ) ")
    elif (bmi >= 35 and bmi < 40):
        label_message.configure(text=f"Your BMI is {bmi}. Obesity ( Class II ) ")
    elif (bmi >= 40):
        label_message.configure(text=f"Your BMI is {bmi}. Extreme Obesity ")

def bmi_calculater():



    kg = entry_kg.get().strip()
    cm = entry_cm.get().strip()


    if (kg == "" or cm == ""):
        label_message.configure(text="Enter both weight and height!")
    else:

        try:
            kg = float(entry_kg.get())
            cm = float(entry_cm.get())

            kg = float(kg)
            cm = float(cm)
            sqr_cm = (cm / 100) * (cm / 100)
            bmi = kg / sqr_cm
            bmi = round(bmi, 2)
            show_results(bmi)
        except:
            label_message.configure(text="Enter a valid number")








calculater_button = tkinter.Button(text="this is a button", command=bmi_calculater)
calculater_button.pack()


label_message = tkinter.Label(text="", font=('Arial', 16, "normal"))
label_message.pack()

window.mainloop()