import math
from gameVec import Vec
class Wire:
	def __init__(self,nmc, nhand):

		self.mc = nmc
		self.pts = []

		self.xmouse=0.95
		self.ymouse=0.85

		i = 0
		while(i < 10):
		
			self.pts.push(Vec(0,i))
			i = i + 1
		
		i = 0
		while(i < self.pts.length - 1):
		
			self.pts[i].addLink(self.pts[i + 1])
			i = i + 1
		
		self.hand = nhand
		self.size = 0.1
		self.xtarget = 0
		self.ytarget = 0
		self.hit = 0
		self.fired = 0
		self.maxsize = 0.1

	def handpos(self):

		return self.pts[0]

	def top(self):

		return self.pts[self.pts.length - 1]

	def fire(self):

		# self.fired is a cooldown I imagine
		if(self.fired > 0):
			return
		
		mouse_dx = self.xmouse - self.pts[self.pts.length - 1].x
		mouse_dy = self.ymouse - self.pts[self.pts.length - 1].y
		mouse_d = math.sqrt(mouse_dx * mouse_dx + mouse_dy * mouse_dy)
		mouse_dx /= mouse_d
		mouse_dy /= mouse_d
		self.xtarget = mouse_dx * 18
		self.ytarget = mouse_dy * 18
		self.size = 1
		self.fired = 15
		self.hit = 0

	def update(self):

		if(self.size <= 0):
		
			self.size = 0.0001
		
		i = 0
		while(i < self.pts.length):
		
			self.pts[i].update(0.9)
			i = i + 1
		
		mouse_d = self.pts[self.pts.length - 1].x
		_loc5_ = self.pts[self.pts.length - 1].y
		i = 0
		while(i < self.pts.length):
		
			self.pts[i].adjustLinks2(self.size)
			i = i + 1
		
		self.pts[self.pts.length - 1].x = mouse_d
		self.pts[self.pts.length - 1].y = _loc5_
		_loc3_ = True

		# if the wire was recently fired
		if(self.fired > 0):
		
			self.fired = self.fired - 1

			
			if(self.hit > 0):
			
				self.pts[self.pts.length - 1].x = self.xtarget
				self.pts[self.pts.length - 1].y = self.ytarget
				self.size = self.maxsize * 0.5
				self.hit = self.hit - 1
				if(self.hit == 0):
				
					self.fired = 0
				
				self.hand.adjustUnit(self.pts[0],0.1)
				self.hand.x = self.pts[0].x
				self.hand.y = self.pts[0].y
				_loc3_ = False
			
			else:
			
				self.size += 1
				if(self.size > 10):
				
					self.size = 10
				
				self.pts[self.pts.length - 1].x += self.xtarget
				self.pts[self.pts.length - 1].y += self.ytarget
				self.pts[self.pts.length - 1].px = self.pts[self.pts.length - 1].x
				self.pts[self.pts.length - 1].py = self.pts[self.pts.length - 1].y
			
		
		else:
		
			self.size = 0.01
			self.pts[self.pts.length - 1].x = self.pts[self.pts.length - 1].x * 0.95 + self.pts[0].x * 0.05
			self.pts[self.pts.length - 1].y = self.pts[self.pts.length - 1].y * 0.95 + self.pts[0].y * 0.05
		
		if(_loc3_):
		
			self.pts[0].x = self.hand.x
			self.pts[0].y = self.hand.y
		
		self.hand.adjustUnitRate(self.handpos(),0.1,0.51)

	def draw(self):

		self.mc.lineStyle(1,16777215,100)
		self.mc.moveTo(self.hand.x,self.hand.y)
		i = 0
		while(i < self.pts.length):
		
			self.mc.lineTo(self.pts[i].x,self.pts[i].y)
			i = i + 1
		

	def hitTest(self,field):

		if(self.hit > 0 or self.fired == 0 or self.fired > 14):
		
			return
		
		last_point = self.pts.length - 1
		if(field.hitTest(self.pts[last_point].x,self.pts[last_point].y,True)):
		
			self.hit = 30
			self.fired = 999
			self.xtarget = self.pts[last_point].x
			self.ytarget = self.pts[last_point].y
			self.maxsize = self.size
		

	def trans(self,v):

		i = 0
		while(i < self.pts.length):
		
			self.pts[i].x += v.x
			self.pts[i].y += v.y
			self.pts[i].px += v.x
			self.pts[i].py += v.y
			i = i + 1
		

	def addForce(self,v):

		i = 0
		while(i < self.pts.length):
		
			self.pts[i].x += v.x
			self.pts[i].y += v.y
			i = i + 1
		

