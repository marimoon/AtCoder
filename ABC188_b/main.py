def main():
	N = int(input())
	As = list(map(int, input().split()))
	Bs = list(map(int, input().split()))
	ans = 0
	for (a,b) in zip(As,Bs):
	    ans += a*b
	print("Yes" if ans == 0 else "No")

if __name__ == "__main__":
    main()
