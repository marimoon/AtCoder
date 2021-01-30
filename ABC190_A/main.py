def get_list(type=int):
    return list(map(type, input().split()))

def get_int():
    return int(input())

def get_str():
    return input()


def main():
    A, B, C = get_list(int)
    if C==0:
        if A > B:
            print("Takahashi")
        else:
            print("Aoki")
    else:
        if A >= B:
            print("Takahashi")
        else:
            print("Aoki")

if __name__ == "__main__":
    main()
