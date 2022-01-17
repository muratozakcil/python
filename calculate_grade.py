first_exam = int(input("Vize "))
second_exam = int(input("Vize2 "))
final = int(input("final "))

total = first_exam * 3 / 10 + second_exam * 3 / 10 + final * 4 / 10

print(total)

if total >= 90:
    print("AA")
elif total >= 85:
    print("BA")
elif total >= 80:
    print("BB")
elif total >= 75:
    print("CB")
elif total >= 70:
    print("CC")
elif total >= 65:
    print("DC")
elif total >= 60:
    print("DD")
elif total >= 55:
    print("FD")
elif total < 50:
    print("FF")
