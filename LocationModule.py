class Locations:

	#Locations Class implementation here






	class Location:
	'Class that defines all locations used for navigating to'

	def __init__(self,name = "",locationID,coords = None):
		self.name = name
		self.locationID = locationID
		self.coordinates = GPSObject(coords)




class GPSObject:
	'Class that holds the GPS co-ordinates used to identify a location'

	def __init__(self,coords):
		self.coordinates = coords