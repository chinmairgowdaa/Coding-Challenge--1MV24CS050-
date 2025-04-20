#solution 1
n= int(input("Enter the value of n: "))
a, b = 0, 1
for i in range(n):
    print(a)
   a,b=b,a+b
   print ("First n fibonacci number is:",a)
#solution 2
n = int(input("Enter value of n: "))
for i in range(2, n + 1):
    for j in range(2, i):
        if i % j == 0:
            break
    else:
        print("Prime number less than or equal to n is",i)
#solution 3
word=input("Enter a word: ")

vow = 0
con = 0

for ch in word:
    if ch.isalpha():
        if ch.lower() in 'aeiou':
            vow += 1
        else:
            con += 1

print("Vowels:", vow)
print("Consonants:",con)    

#solution 4
rows= int(input("Enter number of rows: "))

for i in range(rows):
    for j in range(rows - i - 1):
        print(" ", end="")
    for j in range(2 * i + 1):
        print("*", end="")
print()
