a = [11, 15, 6, 13, 13, 25, 32, 11, 20, 5, 31, 16, 32, 29, 11, 13, 3, 29, 28, 24]
b = [5, 19, 16, 4, 12, 7, 2, 28, 34, 29, 29, 36, 6, 8, 28, 18, 31, 7, 1, 7]
#1
print ("Same numbers", set(a)&set(b))
#2
maxA = (max(a))
maxB = (max(b))

list1 = [maxA, maxB]

maxAll = (max(list1))
print ("Max number",maxAll)
#3
minA = (min(a))
minB = (min(b))

list2 = [minA, minB]

minAll = (min(list2))
print ("Min number",minAll)
#4
aAmount = (21)
aSum = (sum(a))
aKeskmine = (aSum / 21)
print ("Keskmine on ", aKeskmine)

bAmount = (20)
bSum = (sum(b))
bKeskmine = (bSum / 21)
print ("Keskmine on ", bKeskmine)
#5
abAmount = (41)
abSum = (aSum + bSum)
abKeskmine = (
