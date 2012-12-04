'''
	The main window of the client.
'''

import Tkinter

class Window(Tkinter.Tk):
	''' The main window class.

	This class represents the main window of the client.

	Attributes:
		_parent: The parent of this window.
		_menu: The menu container.
		_file_menu: The 'File' menu.
	'''
	def __init__(self, parent=None):
		''' The constructor.
		'''
		Tkinter.Tk.__init__(self, parent)
		self._parent = parent
		self.title('Client')

		# building menu
		self._menu = Tkinter.Menu(self)
		self.config(menu=self._menu)

		self._file_menu = Tkinter.Menu(self._menu)
		self._menu.add_cascade(label='File', menu=self._file_menu)
		self._file_menu.add_command(label='Exit', command=self._exit)

		# building content
		self.grid()

	def _exit(self):
		''' Closes this window.
		'''
		self.destroy()
