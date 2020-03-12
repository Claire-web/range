#印出'hi'一百次
for i in range(100):
	print('hi')

#把range 5的清單列印出來: 兩種寫法
data = []
range(5) # [0, 1, 2, 3, 4]
for a in range(5):
	data.append(a)
print(data)

#List Comprehension清單快寫法
data = [a for a in range(5)]
print(data)

#把b, c, d, e的範圍列印出來

b = range(3) # [0, 1, 2]
print(b)

c = range(2, 5) #[2, 3, 4]
print(c)

d = range(2, 10, 3) #[2, 5, 8]
print(d)

e = range(10, 3, -2) #[10, 8, 6, 4]
