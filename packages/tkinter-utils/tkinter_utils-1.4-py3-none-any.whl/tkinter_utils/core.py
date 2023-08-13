from tkinter import *

def place(obj: Widget, width, height, left, top):
	obj.place(width=width, height=height, x=left, y=top)

class App:
	def __init__(self, title, width, height):
		#
		app = self.app = Tk()
		# title
		app.title(title)
		# size and position
		screen_width = app.winfo_screenwidth()
		screen_height = app.winfo_screenheight()
		x = (screen_width - width) // 2
		y = (screen_height - height) // 2
		app.geometry('{}x{}+{}+{}'.format(width, height, x, y))
		# 是否可调整大小
		app.resizable(False, False)
		# 自定义内容
		self.UI()
		#
		app.mainloop()
	def UI(self):
		pass
