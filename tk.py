import tkinter as tk

def countup():
    global number
    number+=1
    print(number)
    numberlabel.config(text=number)

def reset():
    global number
    number = 0
    print("Reset!")
    numberlabel.config(text=number)


number = 0


root = tk.Tk()
print("Route set!")
root.geometry("300x100")
print("Geometry set!")
root.configure(bg="light blue")
print("BG color set!")
root.title("Couter")
print("Title set!")

label = tk.Label(text="Click the button below to count!")
label.pack()
print("label made sucsessfully!")

button = tk.Button(text = "Click here to count!", command = countup)
button.pack()

numberlabel = tk.Label(text=number)
numberlabel.pack()

resetbutton=tk.Button(text="Click me to reset counter", command = reset)
resetbutton.pack()








print("Sucsessful run")
root.mainloop()
