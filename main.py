from tkinter import *
from tkinter.tix import Tk, Control, ComboBox  # 升级的组合控件包
from tkinter.messagebox import showinfo, showwarning, showerror
from menu.menubar import Menubar

class FridaTool(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.init_menu()



    def init_menu(self):
        menubar = Menu(self)
        self.config(menu=menubar)
        filemenu = Menu(menubar, tearoff=0)
        menubar.add_cascade(label='配置', menu=filemenu)
        filemenu.add_command(label='新建...')
        filemenu.add_command(label='关闭', command=self.quit)


if __name__ == '__main__':
    tool=FridaTool()
    tool.title("FridaTool")  # 设置窗口标题
    tool.geometry("800x400")  # 设置窗口大小 注意：是x 不是*
    tool.resizable()  # 设置窗口是否可以变化长/宽，False不可变，True可变，默认为True
    tool.tk.eval('package require Tix')  # 引入升级包，这样才能使用升级的组合控件
    tool.mainloop()