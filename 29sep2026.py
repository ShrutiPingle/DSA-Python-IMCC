# num=int(input("Enter an num: "))
# sum=0
# n=num
# while num>0 :
#   sum=sum*10+(num%10)
#   num=num//10
# if(n==sum):
#   print(f"{n} is palindrome")
# else :
#   print(f"{n} is not a palindrome")

#Armstrong
# num=int(input("Enter an num: "))
# n=num
# sum=0
# leng=len(str(num))
# while num>0:
#   sum+= (num%10)**leng
#   num//=10
# if(n==sum):
#   print(f"{n} is a amrstrong")
# else:
#   print(f"{n} is not a amrstrong")

# #cube of n natural numbers
# # sum=(num*(num+1)//2)**2
# num=int(input("Enter an num: "))
# sum=0
# for i in range (1,num+1):
#   sum+=i**3
# print(sum)

# number pattern
# for i in range(1,5):
#   for j in range (1, i+1):
#     print(j, end="")
#   print()

# for i in range(5,0,-1):
#   for j in range (i, 0,-1):
#     print(j, end="")
#   print()

for i in range(1,6):
  for j in range (6,i-1,-1):
    print(j, end="")
  print()