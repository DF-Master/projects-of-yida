import tkinter as tk
import tkinter.messagebox as mb
window = tk.Tk()
window.title('Title  here')
window.geometry('720x440')


info = tk.StringVar()
label=tk.Label(textvariable=info) #可变变量必须是SringVar类型
label.place(x=100,y=50)

# label = tk.Label(text='hello world')
# label.pack()


bt1 = tk.Button(window, text='click me', command=lambda: bt1_clicked())
bt1.pack() #pack默认从上往下排


def bt1_clicked():
    mb.showinfo("message", "showinfo")
    info.set('Change ==')
    


window.mainloop()
