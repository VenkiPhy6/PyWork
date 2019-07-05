#for loops

"""
x = 7
if x==3:
    print(x)
    print('nyu')
else:
    print(x**2)
print('end')

for j in range(10):
    print(j)

sum = 0
for j in range(1,11):
    sum += j
    print(sum)

sum = 0
for j in range(1,11):
    sum += j
print(sum)

s= ''
for j in range(20):
    if j < 10:
        s = s + f'{j}'
print(s)
s= ''
for j in range(20):
    n = j % 10
    s = s + str(n)
print(s)

c = 'asd1'
n = 0
for s in c:
    n = n + 1
print('# of characters ', n, len(c))

x = 5
if x == 3:
    print('X equals 3')
elif x == 2:
    print('X equals 2')
else:
    print('X equals something else')
print('This is outside the if')
"""
#THE ORDERING IN DICT IS ARBITRARY! https://stackoverflow.com/questions/5455606/how-to-reverse-order-of-keys-in-python-dict
ages = {"Sam":3,"Bill":4}
for name in ages.keys():
    print(name, ages[name])