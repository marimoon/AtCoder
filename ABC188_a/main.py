def main():
    X, Y = list(map(int, input().split()))
    print( "Yes" if abs(X-Y) < 3 else "No")

if __name__ == "__main__":
    main()
