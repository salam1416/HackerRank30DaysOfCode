# Enter your code here. Read input from STDIN. Print output to STDOUT

T = int(input())
for i in range(T):
    word = input()
    n = len(word)

    for even in word[0:n+1:2]:
        print(even, end="")
    print(" ", end="")

    for odd in word[1:n+1:2]:
        print(odd, end="")
    print()