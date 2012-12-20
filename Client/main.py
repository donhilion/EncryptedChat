'''
The start point of the client.
'''

from gui.window import Window

if __name__ == '__main__':
	window = Window()
	# testing
	for i in range(100):
		window._log.add_to_log("line"+str(i))
	window._contacts.load_list(("foo", "bar"))
	# end testing
	window.mainloop()
