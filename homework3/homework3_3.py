
x = [1.1, 1.2, 3.1, 5, 10.01]
x1 = []
for i in range(len(x)):
    if x[i] % 1 != 0:
        x1.append(x[i])
x2 = [round(x1[i] % 1, 2) for i in range(len(x1))]
print(f"{x2} => {max(x2) - min(x2)}")
x = [1.1, 1.2, 3.1, 5, 10.01]
x1 = []
for i in range(len(x)):
    if x[i] % 1 != 0:
        x1.append(x[i])
x2 = [round(x1[i] % 1, 2) for i in range(len(x1))]
print(f"{x2} => {max(x2) - min(x2)}")