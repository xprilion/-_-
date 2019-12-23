# def rep(s):
#     sa = s.split(" ")
#     print("%20".join(sa))

def rep(s):
	l = len(s)

	spaces = 0

	for i in range(l):
		if s[i] == " ":
			spaces += 1

	extend = spaces*2

	sb = list(s + " " * extend)

	m = l + extend - 1

	for i in range(l-1, 0, -1):
		print(s[i])

		if s[i] == " ":
			sb[extend + i] = "0"
			sb[extend + i-1] = "2"
			sb[extend + i-2] = "%"
			extend -= 2
		else:
			sb[i+extend] = s[i]

		print(sb)

	print(''.join(sb))

rep("I am a good person")