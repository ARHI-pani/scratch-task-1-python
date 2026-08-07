total = int(input("Total parts: "))
size = int(input("Box size: "))

boxes = total // size
loose = total % size

print("Full boxes:", boxes)
print("Loose parts:", loose)
print("Audit:", boxes * size + loose == total)