def get_list(type=int):
    return list(map(type, input().split()))

def get_int():
    return int(input())

def get_str():
    return input()


def main():
    N, X = get_list(int)
    A =  get_list(int)
    print(" ".join([ str(val) for val in A if val != X ]) )

if __name__ == "__main__":
    main()
