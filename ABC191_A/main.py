def get_list(type=int):
    return list(map(type, input().split()))

def get_int():
    return int(input())

def get_str():
    return input()


def main():
    V, T, S, D = get_list(int)
    x = V*T
    y = V*S
    if (x <= D) and (D <= y):
        print("No")
    else:
        print("Yes")

if __name__ == "__main__":
    main()
