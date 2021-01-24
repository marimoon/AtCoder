def get_list(type=int):
    return list(map(type, input().split()))

def get_int():
    return int(input())

def get_str():
    return input()

def main():
    N, X = get_list(int)
    amount = 0
    for i in range(N):
        v,p = get_list(int)
        amount += v*p
        if amount > X*100:
            print(i+1)
            exit()
    print("-1")

if __name__ == "__main__":
    main()
