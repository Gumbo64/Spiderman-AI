import math
class Vec:

   def __init__(self,xx, yy):
   
      self.x = xx
      self.y = yy
      self.px = xx
      self.py = yy
      self.vx = 0
      self.vy = 0
      self.links = []
      self.distances = []
   
   def addLink(self,other):
    #    



    #   if(math.random() < 0.5):

    self.links.push(other)
    self.distances.push(self.distance(other))
      
    #   else:
    #      self.links.unshift(other)
    #      self.distances.unshift(self.distance(other))
      
   
   def clearLinks(self):
   
      self.links = []
      self.distances = []
   
   def update(self,o):
   
      self.vx = self.x - self.px
      self.vy = self.y - self.py
      self.px = self.x
      self.py = self.y
      self.vx *= o
      self.vy *= o
      self.x += self.vx
      self.y += self.vy
   
   def distance(self,other):
   
      dx = self.x - other.x
      dy = self.y - other.y
      return math.sqrt(dx*dx + dy*dy)
   
   def adjustUnit(self,other, goal_distance):
       
    #  move nodes like the 2d rope tutorial
      dx = other.x - self.x
      dy = other.y - self.y
      d = math.sqrt(dx * dx + dy * dy)
      delta_d = goal_distance - d
      if(d == 0):
         return
      
      dx = dx / d * (delta_d * 0.5)
      dy = dy / d * (delta_d * 0.5)

    #   move the nodes from both sides towards their centre
      self.x -= dx
      self.y -= dy
      other.x += dx
      other.y += dy
   
#    unused
#    def adjustUnitRate(self,other, goal_distance, alpha):
   
#       dx = other.x - self.x
#       dy = other.y - self.y
#       d = math.sqrt(dx * dx + dy * dy)
#       delta_d = goal_distance - d
#       if(d == 0):
      
#          return
      
#       dx /= d
#       dy /= d

#       self.x -= dx * (delta_d * alpha)
#       self.y -= dy * (delta_d * alpha)
#       other.x += dx * (delta_d * (1 - alpha))
#       other.y += dy * (delta_d * (1 - alpha))
   
   def adjustLinks(self):
   
      i = 0
      while(i < self.links.length):
      
         self.adjustUnit(self.links[i],self.distances[i])
         i = i + 1
      
   
   def adjustLinks2(self,scale):
   
      i = 0
      while(i < self.links.length):
      
         self.adjustUnit(self.links[i],self.distances[i] * scale)
         i = i + 1
      
   

