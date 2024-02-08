from tkinter import *
from tkinter import ttk

class Todo:
    def __init__(self, root):
        self.root = root
        self.root.title('To-do-list')
        self.root.geometry('650x410+300+150')

        self.label = Label(self.root, text='To-Do-List-App',
                           font='ariel, 25 bold', width=10, bd=5, bg='orange', fg='black')
        self.label.pack(side='top', fill=BOTH)

        self.label2 = Label(self.root, text='Add Task',
                            font='ariel, 18 bold', width=10, bd=5, bg='orange', fg='black')
        self.label2.place(x=40, y=54)

        self.label3 = Label(self.root, text='Tasks',
                            font='ariel, 25 bold', width=10, bd=5, bg='orange', fg='black')
        self.label3.place(x=320, y=54)

        self.main__text = Listbox(self.root, height=9, bd=5, width=23, font="ariel, 20 italic bold")
        self.main__text.place(x=280, y=100)

        self.text = Text(self.root, bd=5, height=2, width=30, font="ariel, 10 bold")
        self.text.place(x=20, y=120)

        def add():
            content = self.text.get(1.0, END).strip()  # Get the content and remove leading/trailing whitespaces
            if content:  # Check if there's any content
                self.main__text.insert(END, content.split('\n')[0])  # Insert the first line of content
                with open("data.txt", 'a') as file:  # Append to the file
                    file.write(content + '\n')
                self.text.delete(1.0, END)

        def delete():
            delete_ = self.main__text.curselection()
            if delete_:
                look = self.main__text.get(delete_)
                with open('data.txt', 'r+') as f:
                    new_f = f.readlines()
                    f.seek(0)
                    for line in new_f:
                        item = str(look)
                        if item not in line:
                            f.write(line)
                    f.truncate()
                self.main__text.delete(delete_)

        try:
            with open('data.txt', 'r') as file:
                read = file.readlines()
                for i in read:
                    ready = i.strip()
                    if ready:  # Check if there's any content
                        self.main__text.insert(END, ready.split('\n')[0])
        except FileNotFoundError:
            pass

        self.button = Button(self.root, text="Add", font='sarif, 20 bold italic',
                             width=10, bd=5, bg='orange', fg='black', command=add)
        self.button.place(x=30, y=180)

        self.button2 = Button(self.root, text="Delete", font='sarif, 20 bold italic',
                              width=10, bd=5, bg='orange', fg='black', command=delete)
        self.button2.place(x=30, y=280)


def main():
    root = Tk()
    ui = Todo(root)
    root.mainloop()

if __name__ == "__main__":
    main()
