print("hello my name is Abraham, and i will be your personal bot")
import time

time.sleep(1)
print("Now you know my name, but i dont. Please write your name below: ")
name = input("")
print(name, "my ex had this name")

print("lets go to more private information) if you AGREE privacy policy please WRITE YES else WRITE NO")
privpolicy = str(input())
if privpolicy == "yes" or "YES" or "Yes":
    print("nice lets go:")
else:
    print("mi ne mojem obshyatsya dalshe")
print("What is your year of birth?")
year_of_birth = int(input())
#year = int(print(2020 - year_of_birth))
#if year >= 18:
#    print(name, "xux its good, because our chat 18+")
#else:
#    print(",sorry ti ne podhodish mne dlya obsheniya po vozrastu")

time.sleep(1)
print("we are the same age)) to surprise you more, I can deduce from two numbers at once their difference product and sum: (write two numbers)")
a = int(input("First number: "))
b = int(input("Second number: "))
print("hmmm let me calculate....")
time.sleep(2)
print("sum of them: ", a + b)
print("difference of them: ", a - b)
print("product of them: ", a * b)
