import sys


def sol(S, pattern):
    lenP=len(pattern)
    stack=[]
    for i in range(len(S)):
        stack.append(S[i])
        if ''.join(stack[-lenP:]) == pattern:
            for _ in range(lenP):
                stack.pop()

    return "".join(stack) if stack else "FRULA"


def main():
    str_=sys.stdin.readline().strip()
    pattern=sys.stdin.readline().strip()

    print(sol(str_, pattern))


if __name__=="__main__":
    main()