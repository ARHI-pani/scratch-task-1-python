
import random

accepted = 0
rejected = 0


for i in range(10):
    part = random.randint(1, 100)

    if part >= 50:     
        accepted += 1
    else:
        rejected += 1


boxes = accepted // 4
loose = accepted % 4


print("----- End of Shift Report -----")
print("Total Parts Inspected :", 10)
print("Accepted Parts        :", accepted)
print("Rejected Parts        :", rejected)
print("Boxes Packed (4 each) :", boxes)
print("Loose Parts           :", loose)