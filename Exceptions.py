class NotRegistered(Exception):
	"""User is not registered, Access Denied"""

class IncompleteInformation(Exception):
	"""User did not provide required information to complete request"""

class FailedValidation(Exception):
	"""Information is invalid or does not meet system validation protocols"""
class RouteNotFound(Exception):
	"""Not such route between locations could be found"""