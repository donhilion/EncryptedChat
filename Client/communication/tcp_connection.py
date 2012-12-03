'''
	A low level TCP connection.
'''

import socket
from threading import Lock

BUFFER_SIZE = 1024

class TCPConnection(object):
	''' A low level TCP connection.

	Attributes:

	'''
	def __init__(self):
		''' The constructor.
		'''
		self._server = None
		self._server_port = None
		self._socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

		self._is_receiving = False
		self._lock = Lock()
		
		self._buffer = []
		self._connected = False

	def is_connected(self):
		''' Determines if this connection is open.

		Returns:
			True if this connection is open.
		'''
		return self._connected

	# TCP
	def configure(self, server = None, port = None):
		''' Configures the connection.

		Args:
			server: The address of the server to connect to.
			port: The port to connect to.
		'''
		self._server = server
		self._server_port = port

	def connect(self):
		''' Connects to the server.

		Returns:
			True if the connection was successfully established,
			False otherwise.
		'''
		if self._server is not None and self._server_port is not None:
			self._socket.connect((self._server, self._server_port))
			self._connected = True
			return True
		return False
		
	def disconnect(self):
		''' Closes the connection.
		'''
		self._socket.close()
		self._connected = False
		
	# Messages
	def send(self, msg):
		self._socket.sendall(msg)
	
	def receive(self):
		self._lock.acquire()
		copy = self._buffer[:]
		self._buffer = []
		self._lock.release()
		return copy
	
	def _listen(self):
		while self._is_receiving:
			data = self._socket.recv(BUFFER_SIZE)
			self._lock.acquire()
			self._buffer.append(data)
			self._lock.release()
	
	# Listener
	def _start_listener(self):
		pass
	
	def _stop_listener(self):
		pass
