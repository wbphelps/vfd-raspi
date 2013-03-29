class Test(object):
	def __init__(self, time):
		self.time = time
	@property
	def time(self):
		return self.__dict__['time']
	@property
	def hour(self):
		return int(self.__dict__['time']/60)
	@property
	def minute(self):
		return self.__dict__['time']%60
	@time.setter
	def time(self, value):
		self.__dict__['time'] = value
	@hour.setter
	def hour(self, value):
		self.__dict__['time'] = value*60 + self.time%60
	@minute.setter
	def minute(self, value):
		self.__dict__['time'] = value%60 + int(self.time/60)*60
	def __str__(self):
		return '{:02}{:02}'.format(self.hour, self.minute)

t = Test(600)
#print "t.hour " + str(t.hour) + " t.minute " + str(t.minute)
print "time " + str(t.time) + " fmt " + str(t)
t.time = 4*60+13
print "time " + str(t.time) + " fmt " + str(t)
t.hour = 11
t.minute = 00
print "time " + str(t.time) + " fmt " + str(t)
t.time += 27
print "time " + str(t.time) + " fmt " + str(t)

#print dir(Test)