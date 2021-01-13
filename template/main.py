def get_list(type=int):
    return list(map(type, input().split()))

def get_int():
    return int(input())

def get_str():
    return input()


def main():
    X, Y = get_list(int)
    print( "Yes" if abs(X-Y) < 3 else "No")

if __name__ == "__main__":
    main()
