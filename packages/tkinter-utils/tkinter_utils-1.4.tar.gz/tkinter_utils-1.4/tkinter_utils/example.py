from tkinter_utils.core import *

class ExampleApp(App):
	def __init__(self):
		super().__init__("A", 400, 300)
	def UI(self):
		button = Button(self.app, text='Okay', command=self.a)
		place(button, 100, 100, 0, 0)
	def a(self):
		print(1)

if __name__ == "__main__":
	ExampleApp()
