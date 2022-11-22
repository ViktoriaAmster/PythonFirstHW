# Напишите программу для. проверки истинности утверждения
#  ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

print("¬(X V Y V Z) = ¬X ⋀ ¬Y ⋀ ¬Z")
print("X  Y  Z  =")
boolList = [False,True]
for i in boolList:
    for k in boolList:
        for l in boolList:
            result = not(i or k or l) == (not(i) and not(k) and not(l))
            print(f'{int(i)}  {int(k)}  {int(l)}  {int(result)}')