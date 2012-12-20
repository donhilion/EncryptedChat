'''
	The high level server connection.
'''

from tcp_connection import TCPConnection
from message import Message
import logging

MSG_GET_SERVER_KEY = 'plain:getServerKey'

class ServerConnection(object):
	''' A high level connection with the server.

	Attributes:
		_tcp_connection: The low level connection to the server.
		_next_id: The id of the next message
		_id_to_respond: The dictionary of respondes associated with their id.
		_id_to_handler: The dictionary of handlers for respondes with a special id.
	'''
	def __init__(self):
		''' The constructor.
		'''
		self._tcp_connection = TCPConnection()
		self._next_id = 0
		self._id_to_respond = {}
		self._id_to_handler = {}

	def get_server_key(self):
		''' Gets the server rsa key.
		'''
		if self._tcp_connection is None or \
			not self._tcp_connection.is_connected:
			return None
		send_msg = Message(msg_id=self._next_id, encoded=False,
                           msg=MSG_GET_SERVER_KEY)
		self._next_id += 1

		self._tcp_connection.send(send_msg.get_json_string())
		return None

	def poll_for_msgs(self):
		''' Polls for new messages.
		'''
		msgs = self._tcp_connection.receive()
		for msg in msgs:
			try:
				parsed = Message(json_string=msg)
				self._id_to_respond[parsed.get_id()] = parsed
			except Exception:
				logging.error('Returned message in unknown format: ' + str(msg))
