from tkinter import Tk,Button,Entry,StringVar

class calculator:
    def __init__(self,master):
        master.title("Calculator")
        master.geometry('250x300+0+0')
        master.configure(bg="black")
        master.resizable(False,False)

        self.equation = StringVar()
        self.entry_value = ""
        Entry(width=17,bg='#ccddff',font=('Arial Bold',28),textvariable=self.equation).place(x=0,y=0)

        Button(text='1',width=5,height=2,command=lambda:self.show(1)).place(x=10,y=70)
        Button(text='2',width=5,height=2,command=lambda:self.show(2)).place(x=70,y=70)
        Button(text='3',width=5,height=2,command=lambda:self.show(3)).place(x=130,y=70)
        Button(text='4',width=5,height=2,command=lambda:self.show(4)).place(x=10,y=130)
        Button(text='5',width=5,height=2,command=lambda:self.show(5)).place(x=70,y=130)
        Button(text='6',width=5,height=2,command=lambda:self.show(6)).place(x=130,y=130)
        Button(text='7',width=5,height=2,command=lambda:self.show(7)).place(x=10,y=190)
        Button(text='8',width=5,height=2,command=lambda:self.show(8)).place(x=70,y=190)
        Button(text='9',width=5,height=2,command=lambda:self.show(9)).place(x=130,y=190)
        Button(text='0',width=5,height=2,command=lambda:self.show(0)).place(x=70,y=250)
        Button(text='+',width=5,height=2,bg='orange',command=lambda:self.show('+')).place(x=190,y=70)
        Button(text='-',width=5,height=2,bg='orange',command=lambda:self.show('-')).place(x=190,y=130)
        Button(text='*',width=5,height=2,bg='orange',command=lambda:self.show('*')).place(x=190,y=190)
        Button(text='/',width=5,height=2,bg='orange',command=lambda:self.show('/')).place(x=190,y=250)
        Button(text='C',width=5,height=2,bg='orange',command=self.clear).place(x=10,y=250)
        Button(text='=',width=5,height=2,bg='orange',command=self.solve).place(x=130,y=250)


    def show(self,value):
        self.entry_value += str(value)
        self.equation.set(self.entry_value)

    def clear(self):
        self.entry_value = ''
        self.equation.set(self.entry_value)

    def solve(self):
        result = eval(self.entry_value)
        self.equation.set(result)        




root = Tk()
calculator = calculator(root)
root.mainloop()



