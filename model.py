from sqlalchemy import Column, Integer, String, Boolean, Enum, Date, Time, ForeignKey, DateTime, Text, ForeignKeyConstraint
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

class Station(Base):
	__tablename__ = 'station'

	code = Column(String(length=3), primary_key=True)
	name = Column(String(length=60))
	
	def __init__(self, **kwargs):
		for k, v in kwargs.iteritems():
			setattr(self, k, v)

	def __repr__(self):
		return '%s' % (self.name, )


class Line(Base):
	__tablename__ = 'line'

	id = Column(String(length=1), primary_key=True)
	name = Column(String(length=25))
	colour = Column(String(length=6))
	fore_colour = Column(String(length=6))
	xml_code = Column(String(length=3))

	def __init__(self, **kwargs):
		for k, v in kwargs.iteritems():
			setattr(self, k, v)

	def __repr__(self):
		return '%s' % (self.name, )


class JourneyPatternSection(Base):
	# This models JourneyPatternTimingLink too.

	__tablename__ = 'journeypatternsection'

	section = Column(String(length=40), index=True)
	id = Column(String(length=40), primary_key=True)
	from_station_id = Column(String, ForeignKey('station.code'), index=True)
	from_station = relationship('Station', foreign_keys=[from_station_id])
	from_sequence = Column(Integer())
	to_station_id = Column(String, ForeignKey('station.code'), index=True)
	to_station = relationship('Station', foreign_keys=[to_station_id])
	to_sequence = Column(Integer())
	length = Column(Integer())
	wait_time = Column(Integer())
	nonstop_next = Column(Boolean())

	def __init__(self, **kwargs):
		for k, v in kwargs.iteritems():
			setattr(self, k, v)

	def __repr__(self):
		return '%s - %s, %d seconds' % (self.from_station, self.to_station, self.length)


class Route(Base):
	__tablename__ = 'route'

	id = Column(String(length=40), primary_key=True)
	description = Column(String(length=100))
	section = Column(String(length=40), index=True)
	
	def __init__(self, **kwargs):
		for k, v in kwargs.iteritems():
			setattr(self, k, v)

	def __repr__(self):
		return '%s' % (self.description, )


class RouteSection(Base):
	__tablename__ = 'routesection'

	route_id = Column(String, ForeignKey('route.id'))
	route = relationship('Route', foreign_keys=[route_id])
	id = Column(String(length=40), primary_key=True)
	from_station_id = Column(String, ForeignKey('station.code'))
	from_station = relationship('Station', foreign_keys=[from_station_id])
	to_station_id = Column(String, ForeignKey('station.code'))
	to_station = relationship('Station', foreign_keys=[to_station_id])
	direction = Column(Enum('I', 'O', name='direction_choices'))

	def __init__(self, **kwargs):
		for k, v in kwargs.iteritems():
			setattr(self, k, v)

	def __repr__(self):
		return '%s - %s' % (self.from_station, self.to_station)


class Service(Base):
	__tablename__ = 'service'

	id = Column(String(length=40), primary_key=True)
	
	line_id = Column(String, ForeignKey('line.id'))
	line = relationship('Line', foreign_keys=[line_id])

	start_date = Column(Date())
	end_date = Column(Date())
	runs_monday = Column(Boolean())
	runs_tuesday = Column(Boolean())
	runs_wednesday = Column(Boolean())
	runs_thursday = Column(Boolean())
	runs_friday = Column(Boolean())
	runs_saturday = Column(Boolean())
	runs_sunday = Column(Boolean())

	def __init__(self, **kwargs):
		for k, v in kwargs.iteritems():
			setattr(self, k, v)

	def __repr__(self):
		return '%s (%s)' % (self.line, self.id) 


class JourneyPattern(Base):
	__tablename__ = 'journeypattern'

	id = Column(String(length=40), primary_key=True)
	direction = Column(Enum('I', 'O', name='direction_choices'))
	section = Column(String(length=40))

	route_id = Column(String, ForeignKey('route.id'))
	route = relationship('Route', foreign_keys=[route_id])
	
	service_id = Column(String, ForeignKey('service.id'))
	service = relationship('Service', foreign_keys=[service_id])

	def __init__(self, **kwargs):
		for k, v in kwargs.iteritems():
			setattr(self, k, v)

	def __repr__(self):
		return "<JourneyPattern('%s','%s')>" % (self.direction, self.route)


class VehicleJourney(Base):
	__tablename__ = 'vehiclejourney'

	id = Column(String(length=40), primary_key=True)
	time = Column(Time(), index=True)
	runs_monday = Column(Boolean())
	runs_tuesday = Column(Boolean())
	runs_wednesday = Column(Boolean())
	runs_thursday = Column(Boolean())
	runs_friday = Column(Boolean())
	runs_saturday = Column(Boolean())
	runs_sunday = Column(Boolean())

	pattern_id = Column(String, ForeignKey('journeypattern.id'), index=True)
	pattern = relationship('JourneyPattern', foreign_keys=[pattern_id])

	service_id = Column(String, ForeignKey('service.id'))
	service = relationship('Service', foreign_keys=[service_id])

	def __init__(self, **kwargs):
		for k, v in kwargs.iteritems():
			setattr(self, k, v)

	def __repr__(self):
		return '%s (%s)' % (self.service, self.time) 


class ServicePoint(Base):
	__tablename__ = 'servicepoint'

	id = Column(Integer(), primary_key=True)

	station_id = Column(String, ForeignKey('station.code'), index=True)
	station = relationship('Station', foreign_keys=[station_id])
	
	line_id = Column(String, ForeignKey('line.id'))
	line = relationship('Line', foreign_keys=[line_id])

	direction = Column(Enum('N', 'S', 'E', 'W', 'I', 'O', name='servicepoint_direction_choices'))
	traveline_direction = Column(Enum('I', 'O', name='traveline_direction_choices'))

	def __init__(self, **kwargs):
		for k, v in kwargs.iteritems():
			setattr(self, k, v)

	def __repr__(self):
		return '%s - %s Line, %s' % (self.station, self.line, self.direction)


class FixedTimeLink(Base):
	__tablename__ = 'fixedtimelink'

	id = Column(Integer(), primary_key=True)

	from_point_id = Column(Integer, ForeignKey('servicepoint.id'))
	from_point = relationship('ServicePoint', foreign_keys=[from_point_id])

	to_point_id = Column(Integer, ForeignKey('servicepoint.id'))
	to_point = relationship('ServicePoint', foreign_keys=[to_point_id])

	length = Column(Integer())

	def __init__(self, **kwargs):
		for k, v in kwargs.iteritems():
			setattr(self, k, v)

	def __repr__(self):
		return str(self.from_point) + ' - ' + str(self.to_point) + ' (' + str(self.length / 60) + ' mins)'


class StationCode(Base):
	__tablename__ = 'stationcode'

	station_id = Column(String, ForeignKey('station.code'))
	station = relationship('Station', foreign_keys=[station_id])
	traveline = Column(String(length=12), primary_key=True)
	
	def __init__(self, **kwargs):
		for k, v in kwargs.iteritems():
			setattr(self, k, v)

	def __repr__(self):
		return '%s (%s)' % (self.station, self.traveline)


class TimetablePlan(Base):
	__tablename__ = 'timetableplan'

	id = Column(Integer(), primary_key=True)

	csv = Column(Text())
	result = Column(Text(), nullable=True)
	message = Column(Text(), nullable=True)
	owner = Column(String(length=30))
	total_rows = Column(Integer())
	completed_rows = Column(Integer())
	start_time = Column(DateTime())
	name = Column(String(length=100), nullable=True)
	processing_started = Column(DateTime())
	length = Column(DateTime(), nullable=True)

	def __init__(self, **kwargs):
		self.processing_started = datetime.now()
		
		for k, v in kwargs.iteritems():
			setattr(self, k, v)


class TimetableSection(Base):
	__tablename__ = 'timetablesection'

	id = Column(Integer(), primary_key=True)

	csv = Column(Text())
	name = Column(String(length=100), nullable=True)

	plan_id = Column(Integer(), ForeignKey('timetableplan.id'))
	plan = relationship('TimetablePlan', foreign_keys=[plan_id])

	stations = Column(Text())

	start_id = Column(String, ForeignKey('station.code'))
	start = relationship('Station', foreign_keys=[start_id])

	end_id = Column(String, ForeignKey('station.code'))
	end = relationship('Station', foreign_keys=[end_id])

	approx_length = Column(DateTime(), nullable=True)

	def __init__(self, **kwargs):
		for k, v in kwargs.iteritems():
			setattr(self, k, v)

class NewRoute(Base):
	__tablename__ = 'newroute'

	id = Column(Integer(), primary_key=True)
	route_id = Column(String(length=40))
	station_id = Column(String, ForeignKey('station.code'), index=True)
	station = relationship('Station', foreign_keys=[station_id])

	def __init__(self, **kwargs):
		for k, v in kwargs.iteritems():
			setattr(self, k, v)


class NewTimePoint(Base):
	__tablename__ = 'newtimepoint'
	
	id = Column(Integer(), primary_key=True)

	trip = Column(Integer())

	order = Column(Integer())

	route = Column(String(length=40), index=True)

	servicepoint_id = Column(Integer, ForeignKey('servicepoint.id'), index=True)
	servicepoint = relationship('ServicePoint', foreign_keys=[servicepoint_id])

	arrival = Column(Time(), nullable=True, index=True)
	departure = Column(Time(), nullable=True, index=True)

	runs_monday = Column(Boolean(), index=True)
	runs_tuesday = Column(Boolean(), index=True)
	runs_wednesday = Column(Boolean(), index=True)
	runs_thursday = Column(Boolean(), index=True)
	runs_friday = Column(Boolean(), index=True)
	runs_saturday = Column(Boolean(), index=True)
	runs_sunday = Column(Boolean(), index=True)

	set_no = Column(Integer())
	trip_no = Column(Integer())


	def __init__(self, **kwargs):
		for k, v in kwargs.iteritems():
			setattr(self, k, v)

	def __repr__(self):
		if self.arrival is None:
			return 'Start of Journey - %s (%s)' % (self.servicepoint, self.departure)
		elif self.departure is None:
			return '%s (%s) - End of Journey' % (self.servicepoint, self.arrival)
		else:
			return '%s (A: %s) (D: %s)' % (self.servicepoint, self.arrival, self.departure)


class LiveTrain(Base):
	# A live train
	__tablename__ = 'livetrain'

	#id = Column(Integer(), primary_key=True)

	lcid = Column(String(length=9), index=True)
	setno = Column(String(length=3), primary_key=True)
	tripno = Column(Integer(), primary_key=True)
	service_date = Column(Date(), primary_key=True)

	line_id = Column(String, ForeignKey('line.id'), primary_key=True)
	line = relationship('Line', foreign_keys=[line_id])

	location_text = Column(Text())
	location_track_code = Column(String(length=20))
	
	location_last_station_id = Column(String, ForeignKey('station.code'))
	location_last_station = relationship('Station', foreign_keys=[location_last_station_id]) 
	
	destination_text = Column(Text())
	destination_code = Column(Integer())

	destination_station_id = Column(String, ForeignKey('station.code'))
	destination_station = relationship('Station', foreign_keys=[destination_station_id]) 

	destination_routing_station_id = Column(String, ForeignKey('station.code'))
	destination_routing_station = relationship('Station', foreign_keys=[destination_routing_station_id])

	at_destination = Column(Boolean(), default=False)

	trip = Column(Integer())

	last_updated = Column(DateTime())

	def __init__(self, **kwargs):
		for k, v in kwargs.iteritems():
			setattr(self, k, v)

class LiveTrainPoint(Base):
	__tablename__ = 'livetrainpoint'

	#id = Column(Integer(), primary_key=True)

	setno = Column(String(length=3), primary_key=True)
	tripno = Column(Integer(), primary_key=True)
	service_date = Column(Date(), primary_key=True)

	line_id = Column(String, ForeignKey('line.id'), primary_key=True)
	line = relationship('Line', foreign_keys=[line_id])

	station_id = Column(String, ForeignKey('station.code'), primary_key=True, index = True)
	station = relationship('Station', foreign_keys=[station_id])

	linked_timepoint_id = Column(Integer, ForeignKey('newtimepoint.id'))
	linked_timepoint = relationship('NewTimePoint', foreign_keys=[linked_timepoint_id])

	expected_arrival = Column(DateTime(), index = True)	

	expected_departure = Column(DateTime(), index = True)

	actual_departure = Column(DateTime())

	__table_args__ = (ForeignKeyConstraint([setno, tripno, service_date, line_id],
                                           [LiveTrain.setno, LiveTrain.tripno, LiveTrain.service_date, LiveTrain.line_id]),
                      {})

	live_train = relationship('LiveTrain', foreign_keys=[setno, tripno, service_date, line_id])


	def __init__(self, **kwargs):
		for k, v in kwargs.iteritems():
			setattr(self, k, v)


class TrackernetLine(Base):
	__tablename__ = 'trackernetline'

	id = Column(Integer(), primary_key=True)

	trackernet_line = Column(String(length=1))

	line_id = Column(String, ForeignKey('line.id'), index=True)
	line = relationship('Line', foreign_keys=[line_id])

	last_updated = Column(DateTime())

	def __init__(self, **kwargs):
		for k, v in kwargs.iteritems():
			setattr(self, k, v)


class TrackernetStation(Base):
	__tablename__ = 'trackernetstation'

	id = Column(Integer(), primary_key=True)

	trackernet_station = Column(String(length=3))
	trackernet_line = Column(String(length=1))

	station_id = Column(String, ForeignKey('station.code'), index=True)
	station = relationship('Station', foreign_keys=[station_id])

	line_id = Column(String, ForeignKey('line.id'), index=True)
	line = relationship('Line', foreign_keys=[line_id])

	last_updated = Column(DateTime())

	def __init__(self, **kwargs):
		for k, v in kwargs.iteritems():
			setattr(self, k, v)

