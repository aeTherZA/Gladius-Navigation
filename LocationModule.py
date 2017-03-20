class Locations:

	location_list = [Location]	#List of location objects

	def addLocation(inLoc):

		#Check if location already exists
			



	def modifyLocation(inLoc):




	def removeLocation(inLoc):


	class Location:
	'Class that defines all locations used for navigating to'

	def __init__(self,name,locationID,coords):
		self.name = name
		self.locationID = locationID
		self.coordinates = GPSObject(coords)




class GPSObject:
	'Class that holds the GPS co-ordinates used to identify a location'

	def __init__(self,coords):
		self.coordinates = coords