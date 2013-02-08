class Person:
	def __init__(self, args):
		args = args.split(',')
		if len(args) != 4:
			raise Exception("Invalid line")
		self.name = args[0] + " " + args[1]
		self.work_hours = int(args[2])
		self.done = False
		sched = args[3].split(' ')
		ran = list(range(9, 17))
		for j in range(len(sched)):
			if sched[j]:
				t = [int(i) if int(i) > 6 else int(i) + 12 for i in sched[j].split('-')]
				if t[1] - t[0] < 0 or t[1] - t[0] > 9:
					raise Exception("Invalid work hour range")
				for i in range(t[0], t[1]):
					try:
						ran.remove(i)
					except:
						pass
		self.schedule = ran

# p = Person("k,j,7,1-2 3-4")
