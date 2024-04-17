#Write a program to accept a 4 digit number and
#            a. Display face value of each decimal digit
#            b. Display place value of each decimal digit
#            c. Display no in reverse order by changing decimal place values If user enters 
#             a 4 digit number 9361 output should be
#            a. 9 3 6 1
#            b. 9361 = 9 000 + 300 + 60 + 9
#            c. 1639

num = int(input("Enter 4 digit number : "))
print(num)

a = int(num/1000)
b = int((num%1000)/100)
c = int((num%100)/10)
d = int(num%10)
print(f"face value = {a} {b} {c} {d}")

e = int(num/1000)*1000
f = int((num%1000)/100)*100
g = int((num%100)/10)*10
h = int(num%10)
print(f"place value = {e} + {f} + {g} + {h}")

print(f"reverse order = {d} {c} {b} {a}")