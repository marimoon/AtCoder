def get_list(type=int):
    return list(map(type, input().split()))

def get_int():
    return int(input())

def get_str():
    return input()


def main():
    N = get_int()
    As = get_list(int)
    max_cnt = 0
    max_l = 0
    max_r = 0
    max_x = 0
    for l in range(1, N+1):
        for r in range(l,N+1):
            x = min(As[l-1:r])
            cnt = (r-l+1)*x
            if max_cnt < cnt:
                max_cnt = cnt
                max_l = l
                max_r = r
                max_x = x
    print(max_cnt)
if __name__ == "__main__":
    main()
