class worker(object):
	"""docstring for worker"""
	def __init__(self):
		super(worker, self).__init__()
		self.job = []
		self.salary = 1500
		self.status = 'active'


john = worker()
#john.salary = 1200
john.status = 'passive'


smith = worker()
#smith.salary = 800
smith.status = 'half-active'
print (john.salary, john.status,"john & smith", smith.salary,smith.status)
		