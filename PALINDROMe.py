 #3. Palindrome
#✅ Easy Logic (reverse string with slicing)
def palindrome(s):
     return s == s[::-1]
print(palindrome("madam"))

#✅ Alternative (loop with two pointers)
def palindrome(s):
    i,j=0,len(s)-1
    while i<j:
        if s[i]!= s[j]:
            return False
        i=i+1
        j=j-1
    return True
print(palindrome("nazim"))