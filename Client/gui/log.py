'''
	The log gui of this application.
'''

import Tkinter

class Log(Tkinter.Frame):
	''' The log tab.

	This class represents the log tab.

	Attributes:
		_log_scroll: The scrollbar of the log view.
		_log_text: The text field of the log view.
	'''
	def __init__(self, master):
		Tkinter.Frame.__init__(self, master)
		self._log_scroll = Tkinter.Scrollbar(self)
		self._log_scroll.pack(side=Tkinter.RIGHT, fill=Tkinter.Y)
		self._log_text = Tkinter.Text(self, yscrollcommand=self._log_scroll.set)
		self._log_text.pack(side=Tkinter.LEFT, fill=Tkinter.BOTH)
		self._log_scroll.config(command=self._log_text.yview)

	def add_to_log(self, text):
		''' Appends text to the log.

		Args:
			text: The text to append.
		'''
		self._log_text.insert(Tkinter.END, text+'\n')
