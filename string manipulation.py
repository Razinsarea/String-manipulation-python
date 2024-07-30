s = input('Enter string')
print('Length of the string : '+str(len(s)))
print('String in capital letters : '+s.upper())
print('String in small letters : '+s.lower())
count=0
vowels='aeiouAEIOU'
for char in s:
    if char in vowels:
        count+=1

if count==0 :
            print('No vowels found')

else:
            print('Vowels are : '+str(count))

print('Reversed string :'+s[::-1])


