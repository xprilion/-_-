def sol(s):
	chars = [0 for i in range(26)]

	odds = 0

	for i in s:

		if i != " ":
			pos = -1
			if ord(i) in range(ord('A'), ord('Z')+1):
				pos = ord(i) - ord('A')
			else:
				pos = ord(i) - ord('a')

			chars[pos] += 1

			if chars[pos] % 2:
				odds += 1
			else:
				odds -= 1

	if odds <= 1:
		print("True")
	else:
		print("False")

sol("abacc")