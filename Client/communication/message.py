'''
	Tools for messages.
'''

import json

class Message(object):
	''' Class for a message.

	Attributes:
		_id: The id of this message.
		_encoded: Determines if this message is encoded.
		_msg: The content of this message.
	'''
	def __init__(self, encoded=False, msg_id=-1, msg=None, json_string=None):
		''' The constructor.
		'''
		if json_string is not None:
			self.parse_json(json_string)
		else:
			self._encoded = encoded
			self._id = msg_id
			self._msg = msg

	def parse_json(self, json_string):
		''' Parses a message from json format.

		Args:
			json_string: The message in json format.
		'''
		tree = json.loads(json_string)
		self._id = tree['id']
		self._encoded = tree['encoded']
		# TODO: check encoded
		self._msg = tree['msg']

	def get_json_string(self):
		''' Returns this message in json format.

		Returns:
			The json formatted message.
		'''
		# TODO: check encoded
		tree = { 'id':self._id, 'encoded':self._encoded, 'msg':self._msg }
		return json.dumps(tree)
