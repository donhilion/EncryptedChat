'''
	The main window of the client.
'''

import Tkinter
import tabs

class Window(Tkinter.Tk):
	''' The main window class.

	This class represents the main window of the client.

	Attributes:
		_parent: The parent of this window.
		_menu: The menu container.
		_file_menu: The 'File' menu.
		_tabs: The tab bar of this window.
		_log: The log tab.
		_log_scroll: The scrollbar of the log view.
		_log_text: The text field of the log view.
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
		self._tabs = tabs.TabBar(self)

		self._log = tabs.Tab(self, 'Log')
		self._log_scroll = Tkinter.Scrollbar(self._log)
		self._log_scroll.pack(side=Tkinter.RIGHT, fill=Tkinter.Y)
		self._log_text = Tkinter.Text(self._log, yscrollcommand=self._log_scroll)
		self._log_text.pack(side=Tkinter.LEFT, fill=Tkinter.BOTH)
		self._tabs.add(self._log)

		self._tabs.show()

	def _exit(self):
		''' Closes this window.
		'''
		self.destroy()
