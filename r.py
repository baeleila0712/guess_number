import random

start = input('請輸入您的數字範圍起始值:')
end = input('請輸入您的數字範圍結束值:')
start = int(start)
end = int(end)

r = random.randint(start, end)
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
		print('這是你猜的第', count, '次')
		break
	print('這是你猜的第', count, '次')