s = set()

s.add(1)
s.add(2)

print(s)

s1 = {1, 2, 3, 4, 5, 6}
s2 = {4, 5, 6, 7}
s3 = s1 | s2

print(s3) # print only uniq number

s4 = s1 & s2
print(s4)

s5 = s1 - s2

print(s5)