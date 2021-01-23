def get_list(type=int):
    return list(map(type, input().split()))

def get_int():
    return int(input())

def get_str():
    return input()


def main():
    C = input()
    if (C[0] == C[1]) and (C[1] == C[2]):
        print("Won")
    else:
        print("Lost")

if __name__ == "__main__":
    main()
