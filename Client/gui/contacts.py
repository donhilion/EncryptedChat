'''
	The contacts gui of this application.
'''

import Tkinter

class Contacts(Tkinter.Frame):
	''' The contacts tab.

	This class represents the contacts tab.

	Attributes:
		_all_contacts: The complete list of contacts.
		_search_field: The text field for filtering the contacts.
		_contacts_scroll: The scrollbar of the contacts view.
		_contacts_list: The list of contacts.
	'''
	def __init__(self, master):
		Tkinter.Frame.__init__(self, master)
		self._all_contacts = []
		# gui
		self._search_field = Tkinter.Entry(self)
		self._search_field.pack(side=Tkinter.BOTTOM, fill=Tkinter.X)
		self._contacts_scroll = Tkinter.Scrollbar(self)
		self._contacts_scroll.pack(side=Tkinter.RIGHT, fill=Tkinter.Y)
		self._contacts_list = Tkinter.Listbox(self, yscrollcommand=self._contacts_scroll.set)
		self._contacts_list.pack(side=Tkinter.LEFT, fill=Tkinter.BOTH)
		self._contacts_scroll.config(command=self._contacts_list.yview)
		self._search_field.bind("<KeyRelease>", self.search_handler)


	def load_list(self, contact_list):
		''' Loads the list of contacts.

		Args:
			contact_list: The list of contacts.
		'''
		self._all_contacts = contact_list
		self.refresh_list()

	def refresh_list(self):
		''' Refreshes the displayed list.
		'''
		self._contacts_list.delete(0,Tkinter.END)
		search_string = self._search_field.get().lower()
		for contact in self._all_contacts:
			if search_string in contact.lower():
				self._contacts_list.insert(Tkinter.END, contact)

	def search_handler(self, object):
		''' The event handler for key releases in the search field.

		Args:
			object: The event object.
		'''
		self.refresh_list()