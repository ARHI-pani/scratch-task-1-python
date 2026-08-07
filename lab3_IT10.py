accept = 0
rework = 0
scrap = 0

for i in range(10):
    diameter = float(input("Diameter {i + 1}: "))

    if 9.9 <= diameter <= 10.1:
        print("ACCEPT")
        accept += 1
    elif 9.7 <= diameter < 9.9 or 10.1 < diameter <= 10.3:
        print("REWORK")
        rework += 1
    else:
        print("SCRAP")
        scrap += 1

print("\nFinal Report")
print("ACCEPT:", accept)
print("REWORK:", rework)
print("SCRAP:", scrap)