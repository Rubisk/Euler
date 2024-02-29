total = 0
n = 0
t = 0
smaller = True
max_len = 0
while True:
	if len(str(n)) > max_len:
		max_len += 1
		print(max_len)
	n += 1
	before = total > 0
	total -= 1
	# print(total)
	for c in str(n):
		if c == "3":
			total += 1
	# if before is not (total > 0):
	# 	print "+" if total > 0 else "-"
	# if total > 0 and n % 100 == 11:
	# 	if "1" not in str(n)[:-2]:
	# 		total += 8
	# 		n += 89
	if total == 0:
		t += n
		print("E", n, t)