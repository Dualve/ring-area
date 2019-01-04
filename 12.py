from math import sqrt
s,r1 = map(float,input().split())
pi = 3.1415926535897932384626433832795
res = sqrt((pi * r1 * r1 - s)/pi)
print('%.3f' %res)
