x = int(input("크리스마스 트리의 높이를 설정하세요: "))

for i in range(x):
    for j in range(x - i):
        print(" ", end="")

    for k in range(i * 2 + 1):
        print("*", end="")
    print()
