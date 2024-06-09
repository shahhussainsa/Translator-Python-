from tkinter import *
from tkinter import ttk
from googletrans import Translator, LANGUAGES

def change(text= "type", src = "English", dest = "Hindi"):
  text1 =text
  source1 = src
  dest1 = dest
  trans = Translator()
  transe = trans.translate(text, src=source1, dest=dest1)
  return transe.text

def data():
  s = source_combo.get()
  d = dest_combo.get()
  msg = source_txt.get(1.0, END)
  text_get = change(text= msg, src=s, dest= d)
  dest_txt.delete(1.0,END)
  dest_txt.insert(END, text_get)
  
root = Tk()
root.title("Translator")
root.geometry("500x700")
root.config(bg="grey")

lab_txt = Label(root, text="Translator", font=("Time new Roman", 40, "bold"))
lab_txt.place(x=100,y=40, height=50,width=300)

frame = Frame(root).pack(side=BOTTOM)

lab_txt = Label(root, text="Source Text", font=("Time new Roman", 20, "bold"))
lab_txt.place(x=100,y=100, height=20,width=300)

source_txt = Text(frame, font=("Time new Roman", 20, "bold"), wrap=WORD)
source_txt.place(x=10,y=130,height=100, width=480)
 
list_text = list(LANGUAGES.values())
 
source_combo = ttk.Combobox(frame, value= list_text)
source_combo.place(x=10,y=300,height=40, width=150)
source_combo.set("English")

button_change = Button(frame, text="Translate", relief=RAISED, command=data)
button_change.place(x=170,y=300,height=40, width=150)

dest_combo = ttk.Combobox(frame, value= list_text)
dest_combo.place(x=330,y=300,height=40, width=150)
dest_combo.set("English")

lab_txt = Label(root, text="Translated Text", font=("Time new Roman", 20, "bold"))
lab_txt.place(x=100,y=360, height=30,width=280)

dest_txt = Text(frame, font=("Time new Roman", 20, "bold"), wrap=WORD)
dest_txt.place(x=10,y=400,height=150, width=480)
root.mainloop()