import os

class storage:

	def __init__(self, max_capacity, margin):
		self.max_capacity=max_capacity
		self.margin=margin #percent of max_capacity
		self.qoc=0
		self.voc=0
		self.isFilled=False
		
	def __str__(self):
		return "max_capacity: "+ str(self.max_capacity)+", margin: "+str(self.margin)


	def get_isFilled(self):
		if self.qoc>=self.max_capacity*self.margin:
			self.isFilled=True
		else:
			self.isFilled=False
		return self.isFilled

	def add_money(self, q2add,v2add):
		if not self.isFilled:
			self.qoc+=q2add
			self.voc+=v2add*q2add
		else: 	
			print("No se acepta mas")
	
	def get_qoc(self):
		return self.qoc

	def get_voc(self):
		return self.voc

	def get_margin(self):
		return self.margin

	def capacity2fill(self):
		return self.margin*self.max_capacity-self.qoc

	def get_maxcap(self):
		return  self.max_capacity


class billsrecycler: 
	def __init__(self, max_capacity, p100,p50,p20,p10,pmax, pmin):
		self.max_capacity=max_capacity
		self.p100=p100
		self.p50=p50
		self.p20=p20
		self.p10=p10
		self.pmax=pmax #percent of max_capacity in wich the user consider the recycler full. Tipical value=1 or 0.8
		self.pmin=pmin #percent of max_capacity in wich the user consider the recycler empty. Tipical value=0 or 0.1
		self.poqnormal=(self.p100+self.p50+self.p20+self.p10)/self.max_capacity
				 #porcent of bills that defines the normal quantity of bills in every process.
		self.q100=self.p100
		self.q50=self.p50
		self.q20=self.p20
		self.q10=self.p10
		self.qob=self.q100+self.q50+self.q20+self.q10
		self.isFilled=False
		self.isEmpty=False

	def __str__(self):
		return "max_capacity: "+ str(self.max_capacity)+", pmax:  "+str(self.pmax)+", pmin:  "+str(self.pmin)+", qob100_normal: "+str(self.p100)+", qob50_normal: "+str(self.p50)+", qob20_normal: "+str(self.p20)+", qob10_normal: "+str(self.p10)

	def add_100(self,q2add):
		self.q100+=q2add	

	def subs_100(self,q2subs):
		self.q100-=q2subs
	
	def get_q100(self):
		return self.q100

	def add_50(self,q2add):
		self.q50+=q2add	

	def subs_50(self,q2subs):
		self.q50-=q2subs
	
	def get_q50(self):
		return self.q50

	def add_20(self,q2add):
		self.q20+=q2add	

	def subs_20(self,q2subs):
		self.q20-=q2subs
	
	def get_q20(self):
		return self.q20

	def add_10(self,q2add):
		self.q10+=q2add	

	def subs_10(self,q2subs):
		self.q10-=q2subs
	
	def get_q10(self):
		return self.q10

##new part - condensed form
	def add_bills(self, q2add, vb2add):
		if vb2add==200:
			pass
			## recycler dont accept bills of 200. they are directly lead to the stacker.
		elif vb2add==100:
			self.q100+=q2add
		elif vb2add==50:
			self.q50+=q2add
		elif vb2add==20:
			self.q20+=q2add
		elif vb2add==10:
			self.q10+=q2add
		else:
			print("something wrong happened")

## --- -


#normal values 
	def get_p100(self):
		return self.p100
	
	def get_p50(self):
		return self.p50

	def get_p20(self):
		return self.p20
	
	def get_p10(self):
		return self.p10

	def pay(self,q2p):
		#lob list of bills 10,20,50,100 - in order 
		lob=[0,0,0,0]
		if self.q100>0:
			t100=q2p//100
			if t100>self.q100:
				t100=self.q100
			lob[3]=t100
			q2p-=t100*100
			self.subs_100(t100)
			
		
		if self.q50>0 and q2p>0:
			t50=q2p//50
			if t50>self.q50:
				t50=self.q50
			lob[2]=t50
			q2p-=t50*50
			self.subs_50(t50)
			
		if self.q20>0 and q2p>0:
			t20=q2p//20
			if t20>self.q20:
				t20=self.q20
			lob[1]=t20
			q2p-=t20*20
			self.subs_20(t20)
			
		if self.q10>0 and q2p>0:
			t10=q2p//10
			if t10>self.q10:
				t10=self.q10
			lob[0]=t10
			q2p-=t10*10
			self.subs_10(t10)
			

		return [lob,q2p]	
	

	def get_qob(self):
		self.qob=self.q100+self.q50+self.q20+self.q10
		return self.qob

	def get_qom(self):
		qom=self.q100*100+self.q50*50+self.q20*20+self.q10*10
		return qom

	def get_isFilled(self):
		if self.qob>=self.max_capacity*self.pmax:
			self.isFilled=True
		else:
			self.isFilled=False
		return self.isFilled

	def get_isEmpty(self):
		if self.qob<=self.max_capacity*self.pmin:
			self.isEmpty=True
		else:
			self.isEmpty=False
		return self.isEmpty


class hoppers:
	#reserve. percent that defines the min quantity of coins to consider the hoppers empty. tip. [0.1]
	#qom quantity of money
	#voc value of coin
	#qoc quantity of coins
	def __init__(self, voc, max_capacity,reserve):
		self.max_capacity=max_capacity
		self.reserve=reserve
		self.voc=voc
		self.qoc=self.max_capacity
		self.qom=self.qoc*self.voc
		self.isEmpty=False

	def __str__(self):
		return "voc: "+str(self.voc)+ ", max_capacity: "+ str(self.max_capacity)+", reserve: "+str(self.reserve)

	def decrease_coins(self, q2subs):
		self.qoc-=q2subs
	
	def get_qoc(self):
		return self.qoc

	def get_qom(self):
		self.qom=self.qoc*self.voc
		return self.qom

	def get_voc(self):
		return self.voc

	def get_isEmpty(self):
		if self.qoc<=self.max_capacity*self.reserve:
			self.isEmpty=True
		else:
			self.isEmpty=False
		return self.isEmpty

	def pay(self,q2p):
		if self.qoc>0:
			temp=q2p//self.voc
			if temp>self.qoc:
				temp=self.qoc
			else:
				pass
			
		
		else:
			temp=0

		q2p-=temp*self.voc
		self.decrease_coins(temp)

		return [temp,q2p]
	
	def get_maxcap(self):
		return 	self.max_capacity
	


