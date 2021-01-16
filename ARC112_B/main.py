def get_list(type=int):
    return list(map(type, input().split()))

def get_int():
    return int(input())

def get_str():
    return input()

def counter(A):
   d = dict()
   for val in A:
       if val not in d:
           d[val] = 1
       else:
           d[val] += 1
   return d

def get_max_cnt(cnt):
    max_ = -1
    keys = sorted(cnt.keys())
    for i in range(len(keys)):
        if i in keys:
            max_ = i
        else:
            break
    #print("**", max_)
    list_del = []
    for key in keys:
        if key > max_:
           list_del.append(key)
    #print("++", list_del)
    if max_ >= 0:
        for key in range(max_+1):
            cnt[key] += -1
            if cnt[key] == 0:
                list_del.append(key)
    #print("@@", list_del)
    for val in list_del:
        cnt.pop(val)

    return max_, cnt

def main():
    N, K = get_list(int)
    A = get_list(int)
    cnt = counter(A)
    #print(cnt)
    ans = 0
    for _ in range(K):
        max_, cnt = get_max_cnt(cnt)
        #print(max_, cnt)
        ans += max_+1
        if len(cnt.keys()) == 0:
            break
    print(ans)

if __name__ == "__main__":
    main()
