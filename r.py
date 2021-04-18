import random

r = random.randint(1, 100)
count = 0 
while True:
	count += 1
	num = input('>>請猜一個數字')
	num = int(num)
	if num > r:
		print('再猜一次 數字小點')
	elif num < r:
		print('再猜一次 數字大點')
	else:
		print('BINGO')
		print('這是你的第', count, '次')
		break
	print('這是你的第', count, '次')