# Time: 2021/11/22  23:49
import tkinter
import tkinter.font


class Calculator:
    def __init__(self):
        self.all_press_lst = []
        self.is_press = False
        self.is_press_num = False
        self.root = tkinter.Tk()
        self.result = tkinter.StringVar()
        self.record = tkinter.StringVar()

    def press_compute(self, sign):
        num = self.result.get()
        self.all_press_lst.append(num)
        self.all_press_lst.append(sign)
        self.is_press = True
        if sign == 'AC':
            self.all_press_lst.clear()
            self.result.set(0)
        elif sign == 'B':
            a = num[0:-1]
            self.all_press_lst.clear()
            self.result.set(a)

    def press_num(self, num):
        if self.is_press is False:
            pass
        else:
            self.result.set(0)
            self.is_press = False
        old_num = self.result.get()
        if old_num == '0':
            self.result.set(num)
        else:
            new_num = old_num + num
            self.result.set(new_num)

    def press_equal(self):
        cur_num = self.result.get()
        self.all_press_lst.append(cur_num)
        compute_str = ''.join(self.all_press_lst)
        try:
            calculate_result = eval(compute_str)
        except:
            calculate_result = 'bad parameter'
        self.result.set(calculate_result)  # 显示结果
        self.record.set(compute_str + "=")  # 显示运算过程
        self.all_press_lst.clear()  # 清空列表内容

    def main(self):
        self.root.minsize(300, 550)
        self.root.title('Calculator')
        input_bg = "#393943"
        num_fg = "#DCDCDC"
        btn_fg = "#909194"
        btn_bg = "#22222C"
        btn_w = 75
        btn_h = 70

        my_font = tkinter.font.Font(font='微软雅黑', size=20)  # Set font

        self.result.set(0)
        self.record.set('')

        # Screen
        label1 = tkinter.Label(master=self.root, font=my_font, bg=input_bg, fg=num_fg, bd='9', anchor='se',
                               textvariable=self.record)
        label1.place(width=300, height=120)
        label2 = tkinter.Label(master=self.root, font=my_font, bg=input_bg, fg=num_fg, bd='9', anchor='se',
                               textvariable=self.record)
        label2.place(y=120, width=300, height=80)

        # First line
        btn_ac = tkinter.Button(master=self.root, text='C', bg=btn_bg, fg=btn_fg, bd=0,
                                command=lambda: self.press_compute('AC'))
        btn_ac.place(x=btn_w * 0, y=200 + btn_h * 0, width=btn_w, height=btn_h)
        btn_ac = tkinter.Button(master=self.root, text='←', bg=btn_bg, fg=btn_fg, bd=0,
                                command=lambda: self.press_compute('B'))
        btn_ac.place(x=btn_w * 1, y=200 + btn_h * 0, width=btn_w, height=btn_h)
        btn_ac = tkinter.Button(master=self.root, text='%', bg=btn_bg, fg=btn_fg, bd=0,
                                command=lambda: self.press_compute('%'))
        btn_ac.place(x=btn_w * 2, y=200 + btn_h * 0, width=btn_w, height=btn_h)
        btn_ac = tkinter.Button(master=self.root, text='÷', bg=btn_bg, fg=btn_fg, bd=0,
                                command=lambda: self.press_compute('/'))
        btn_ac.place(x=btn_w * 3, y=200 + btn_h * 0, width=btn_w, height=btn_h)

        # Second line
        btn_ac = tkinter.Button(master=self.root, text='7', bg=btn_bg, fg=num_fg, bd=0,
                                command=lambda: self.press_num('7'))
        btn_ac.place(x=btn_w * 0, y=200 + btn_h * 1, width=btn_w, height=btn_h)
        btn_ac = tkinter.Button(master=self.root, text='8', bg=btn_bg, fg=num_fg, bd=0,
                                command=lambda: self.press_num('8'))
        btn_ac.place(x=btn_w * 1, y=200 + btn_h * 1, width=btn_w, height=btn_h)
        btn_ac = tkinter.Button(master=self.root, text='9', bg=btn_bg, fg=num_fg, bd=0,
                                command=lambda: self.press_num('9'))
        btn_ac.place(x=btn_w * 2, y=200 + btn_h * 1, width=btn_w, height=btn_h)
        btn_ac = tkinter.Button(master=self.root, text='+', bg=btn_bg, fg=btn_fg, bd=0,
                                command=lambda: self.press_compute('×'))
        btn_ac.place(x=btn_w * 3, y=200 + btn_h * 1, width=btn_w, height=btn_h)

        # Third line
        btn_ac = tkinter.Button(master=self.root, text='4', bg=btn_bg, fg=num_fg, bd=0,
                                command=lambda: self.press_num('4'))
        btn_ac.place(x=btn_w * 0, y=200 + btn_h * 2, width=btn_w, height=btn_h)
        btn_ac = tkinter.Button(master=self.root, text='5', bg=btn_bg, fg=num_fg, bd=0,
                                command=lambda: self.press_num('5'))
        btn_ac.place(x=btn_w * 1, y=200 + btn_h * 2, width=btn_w, height=btn_h)
        btn_ac = tkinter.Button(master=self.root, text='6', bg=btn_bg, fg=num_fg, bd=0,
                                command=lambda: self.press_num('6'))
        btn_ac.place(x=btn_w * 2, y=200 + btn_h * 2, width=btn_w, height=btn_h)
        btn_ac = tkinter.Button(master=self.root, text='-', bg=btn_bg, fg=btn_fg, bd=0,
                                command=lambda: self.press_compute('-'))
        btn_ac.place(x=btn_w * 3, y=200 + btn_h * 2, width=btn_w, height=btn_h)

        # Forth line
        btn_ac = tkinter.Button(master=self.root, text='1', bg=btn_bg, fg=num_fg, bd=0,
                                command=lambda: self.press_num('1'))
        btn_ac.place(x=btn_w * 0, y=200 + btn_h * 3, width=btn_w, height=btn_h)
        btn_ac = tkinter.Button(master=self.root, text='2', bg=btn_bg, fg=num_fg, bd=0,
                                command=lambda: self.press_num('2'))
        btn_ac.place(x=btn_w * 1, y=200 + btn_h * 3, width=btn_w, height=btn_h)
        btn_ac = tkinter.Button(master=self.root, text='3', bg=btn_bg, fg=num_fg, bd=0,
                                command=lambda: self.press_num('3'))
        btn_ac.place(x=btn_w * 2, y=200 + btn_h * 3, width=btn_w, height=btn_h)
        btn_ac = tkinter.Button(master=self.root, text='+', bg=btn_bg, fg=btn_fg, bd=0,
                                command=lambda: self.press_compute('+'))
        btn_ac.place(x=btn_w * 3, y=200 + btn_h * 3, width=btn_w, height=btn_h)

        # Fifth line
        btn_ac = tkinter.Button(master=self.root, text='0', bg=btn_bg, fg=num_fg, bd=0,
                                command=lambda: self.press_num('0'))
        btn_ac.place(x=btn_w * 0, y=200 + btn_h * 4, width=btn_w * 2, height=btn_h)
        btn_ac = tkinter.Button(master=self.root, text='.', bg=btn_bg, fg=num_fg, bd=0,
                                command=lambda: self.press_num('.'))
        btn_ac.place(x=btn_w * 2, y=200 + btn_h * 4, width=btn_w, height=btn_h)
        btn_ac = tkinter.Button(master=self.root, text='=', bg='#982425', fg=btn_fg, bd=0,
                                command=lambda: self.press_equal())
        btn_ac.place(x=btn_w * 3, y=200 + btn_h * 4, width=btn_w, height=btn_h)

        self.root.mainloop()


if __name__ == '__main__':
    my_calculator = Calculator()
    my_calculator.main()
