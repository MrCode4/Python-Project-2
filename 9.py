persons = {}

n = int(input())

for i in range(n):
	person = {}
	title = input()
	name  = input()
	age = int(input())
	major = input()

	name = name.lower()
	new_name = ""
	flag = True
	for c in name:
		if c == " ":
			flag = True
		elif flag == True:
			c = chr(ord(c) + ord('A')-ord('a'))
			flag = False
		new_name += c

	person["name"] = new_name
	person["age"] = age
	person["major"] = major

	persons[title] = person

persons = dict(sorted(persons.items(),key=lambda x:x[1]['major'][1]))

print(persons)