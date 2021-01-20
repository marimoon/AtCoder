def get_list(type=int):
    return list(map(type, input().split()))

def get_int():
    return int(input())

def get_str():
    return input()


def main():
    A,B,C=list(map(int, input().split()))
    if (A==B) and (not A == C):
      print("Yes")
    elif (B==C) and (not B == A):
      print("Yes")
    elif (C==A) and (not C == B):
      print("Yes")
    else:
      print("No")
if __name__ == "__main__":
    main()
