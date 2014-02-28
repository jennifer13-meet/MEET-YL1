class Integer(object):
	def __init__(self, the_number=0, neg="-"):
		self.num = the_number
		self.neg = neg
	def display(self):
		return (self.neg + str(self.num))


class NegativeInteger(Integer):
	def __init__(self, the_number=0):
		super(NegativeInteger, self).__init__(the_number, "-")

if __name__=="__main__":
	test = Integer(123, "-")
	print test.display()
		

