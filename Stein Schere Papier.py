from tkinter import *
from random import *

root = Tk()
root.title('Stein Schere Papier')
root.geometry('600x400')
root.resizable(width=False, height=False)
root['bg'] = 'black'

def pressp():
    ssp = ['Stein', 'Schere', 'Papier']
    value = choice(ssp)
    labelText.configure(text=value)



labelText = Label(root, text='', fg='white', font=('Comic Sans MS', 20), bg='black' )
labelText.place(y = 200, x = 240)

stone = Button (root, 
                text='Stein',
                font=('Comic Sans MS', 20),
                bg= 'white',
                command=pressp
                )

stone.place(x = 50, y= 300)

scissors = Button (root, 
                text='Schere',
                font=('Comic Sans MS', 20),
                bg= 'white',
                command=pressp
                )

scissors.place(x = 220, y= 300)


paper = Button (root, 
                text='Papier',
                font=('Comic Sans MS', 20),
                bg= 'white',
                command=pressp
                )

paper.place(x = 420, y= 300)

root.mainloop()