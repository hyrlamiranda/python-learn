#Write a program that computes 4⋅∑k=1106(−1)k+12k−1=4⋅(1−1/3+1/5−1/7+1/9−1/11…).
#Exercise 11 https://adriann.github.io/programming_problems.html

from math import pow

sum = 0
for k in range(0, int(pow(10,6)+1)):
	sum = sum + pow(-1,k+1)/(2*k - 1)

sum = sum * 4
print sum