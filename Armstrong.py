#5. Armstrong Number

#Trick: Sum of (digit ^ number of digits) = number
n=153
sum = 0
order = len(str(n))
copy_n = n
while (n>0):
    digit = n%10
    sum += digit ** order
    n = n//10
if sum == copy_n:
    print(f"{copy_n} num is armstrong")
else:
    print(f"{copy_n} num is not armstrong")