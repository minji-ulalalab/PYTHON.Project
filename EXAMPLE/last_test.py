목록 = [1, 52, 273, 32, 99, 101]
최대값 = 목록[0]
최소값 = list(reversed(목록))[0]

#(0, 1), (1, 52), (2, 273)...
for i, value in enumerate(목록):
    if 목록[0] < value:
        목록.insert(0, value)
        del 목록[i]
        print(목록)

    else:
        continue


print(목록)
print(최대값)
print(최소값)