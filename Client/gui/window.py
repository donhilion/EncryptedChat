'''
	The main window of the client.
'''

import Tkinter
from contacts import Contacts
from notebook import notebook
from log import Log

class Window(Tkinter.Tk):
	''' The main window class.

	This class represents the main window of the client.

	Attributes:
		_parent: The parent of this window.
		_menu: The menu container.
		_file_menu: The 'File' menu.
		_notebook: The notebook containing the tabs.
		_log: The log tab.
		_contacts: The contacts tab.
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
		self._notebook = notebook(self, Tkinter.TOP)

		self._log = Log(self._notebook())
		self._notebook.add_screen(self._log, "Log")

		self._contacts = Contacts(self._notebook())
		self._notebook.add_screen(self._contacts, "Contacts")

	def _exit(self):
		''' Closes this window.
		'''
		self.destroy()
