'''Pranav is back with again with an interesting problem. He gives you a number N and wants you to find two distinct positive natural numbers such that their bitwise XOR is N and bitwise AND is 0. If such numbers exist, print True, else print False.
For example, if he gives the number N as 6, then the possible numbers that satisfy the above conditions are 2 and 4 because 2&4==0 and 2^4==6.`'''


n=int(input())
flag=False
for i in range(n):
    for j in range(n):
        if flag==False:
            if i^j==n:
                if i&j==0:
                    flag=True
                    print(True)
                    break
if flag==False:
    print(False)
