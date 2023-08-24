num = int(input("Enter Any Number To Check Palindrome Number :- "))
temp = num
rev = 0
while(num>0):
    rem = num%10
    rev = (rev*10)+rem
    num = num//10
print(rev)
if(temp==rev):
    print(temp,"is a Palindrome Number")
else:
    print(temp,"is Not a Palindrome Number")