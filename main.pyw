import table
from tkinter import *
import tkinter.messagebox


    
class Window(table.Table):
    def __init__(self):
        super().__init__()
        self.table = self.get_table()

        self.root = Tk() 
        self.root.geometry('400x500+0+0')
        self.root.title('SIMPLE MASS CALCULATOR')
        self.root.configure(bg='light blue')

        self.res_frame = Frame(self.root,bg='white')
        self.res_frame.pack(side=RIGHT)

        self.canvas = Canvas(self.root,height=500,width=200)
        self.canvas.bind('<Button-1>',self.add_element)
        self.canvas.pack(side=LEFT)

        self.sum = []
        self.labels = []
        self.buttons = {}

    def main(self):
        keys = tuple(self.table.keys())
        x = 10
        y = 10

        for i in range(0,len(keys)):
            self.canvas.create_text(x,y,text=keys[i])

            x+=30
            if x > 190:
                y+=25
                x = 10
        delButton = Button(self.root,text='delete',command=lambda : self.remove_element()).pack()
        delAll = Button(self.root,text='delete all',command = self.delete_all).pack()
        showSum = Button(self.root,text='sum',command=self.SUM).pack()

    def SUM(self):
        SUM = sum(self.sum)
        print(SUM)
        tkinter.messagebox.showinfo('SUM',f'SUM --> {SUM}')
    
    def delete_all(self):
        del self.sum[:]
        for i in self.labels:
            i.pack_forget()
        del self.labels[:]

    def add_element(self,event): 
        x = event.x
        y = event.y
        x = int(x/30)
        y = int(y/25)
        
        loc = 0
        loc += x
        if y>0:
            loc += 7*y
        print(loc)

        symbols = tuple(self.table.keys())
        masses = tuple(self.table.values())

        element = symbols[loc]
        mass = masses[loc]

        label = Label(self.res_frame,text =f'{element}:{mass}')
        self.labels.append(label)
        self.sum.append(mass)
        label.pack()
  
    def remove_element(self):
        self.sum.pop()
        self.labels[-1].pack_forget()
        self.labels.pop()
       
app = Window()
app.main()
app.root.mainloop()

