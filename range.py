# range 範圍
# python 內建功能: 清單產生器
import random

range(5) # [0, 1, 2, 3, 4]
range(3) #[0, 1, 2]

for i in range(5):
	r = random.randint(1,1000)
	print('這是第', i + 1, '次產生隨機數: ', r)

for i in range(3):
	r = random.randint(1,100)
	num = input('請猜數字: ')
	num = int(num)
	print(num)
	if num == r:
		print('猜中了')
		print('這是你猜的第', i +1, '次')
		break
	elif num > r:
		print('比答案大')
	elif num < r:
		print('比答案小')
	print('這是你猜的第', i +1, '次')
	if i == 2:
		print('密碼上鎖,請洽程式管理員')
