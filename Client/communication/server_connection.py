'''
	The high level server connection.
'''

from tcp_connection import TCPConnection

MSG_GET_SERVER_KEY = 'plain:getServerKey\n'

class ServerConnection(object):
	''' A high level connection with the server.

	Attributes:
		_tcp_connection: The low level connection to the server.
		_next_id: The id of the next message
	'''
	def __init__(self):
		self._tcp_connection = TCPConnection()
		self._next_id = 0

	def getServerKey(self):
		# TODO check connection
		send_msg = str(self._next_id) + ':' + MSG_GET_SERVER_KEY
		self._next_id += 1

		self._tcp_connection.send(send_msg)
