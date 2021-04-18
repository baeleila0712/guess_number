import random

r = random.randint(1, 100)
while True:
	num = input('>>請猜一個數字')
	num = int(num)
	if num > r:
		print('再猜一次 數字小點')
	elif num < r:
		print('再猜一次 數字大點')
	else:
		print('BINGO')
		break