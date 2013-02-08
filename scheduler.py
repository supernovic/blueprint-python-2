import sys
from person import Person

# global list of people
people = []

schedule = open(sys.argv[1]).read().split('\n')
for line in schedule:
	if line:
		people.append(Person(line))

# sort the people
for p in people:
	print p
	sorted(people, key=lambda person:len(p.schedule))
#sorted(test, key=lambda person:len(person[1]))
# run scheduling algorithm to an array[17]

final_schedule = [""] * 8
def make_schedule ():
	for i in range(8):
		for p in people:
			if (i+9) in p.schedule and not p.done:
				final_schedule[i] = p.name
				p.work_hours = p.work_hours - 1
				if p.work_hours == 0:
					p.done = True
				break

def make_string (list):
    return "09-10 " + final_schedule[0] + "\n" + "10-11 " + final_schedule[1] + "\n" + "11-12 " + final_schedule[2] + "\n" + "12-01 " + final_schedule[3] + "\n" + "01-02 " + final_schedule[4] + "\n" + "02-03 " + final_schedule[5] + "\n" + "03-04 " + final_schedule[6] + "\n" + "04-05 " + final_schedule[7] + "\n"

make_schedule() 
schedule_return = make_string(final_schedule)
print schedule_return
# schedule.seek(0, 2)    
# schedule.write(schedule_return)
