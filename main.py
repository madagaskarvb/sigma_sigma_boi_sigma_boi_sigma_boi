a = [1, 2, [3, 4, [5, 6]]]
b = a.copy()
c = a[:]
print(f"a = {a}")
print(f"b = {b}")
print(f"c = {c}")
a[2][2].append(7)
print("after appending 7 to a")
print(f"a = {a}")
print(f"b = {b}")
print(f"c = {c}")