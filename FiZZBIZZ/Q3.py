#Question code : MKGPLNKS
for i in range(int(input())):
    n=int(input())
    s=input()
    c=s.count("WB")
    c1=s.count("BW")
    print(max(c,c1))