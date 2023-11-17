import sys


def kmp(str_, pattern)-> str:
    ans=[]
    pi=[0]*len(pattern)
    i=0
    for j in range(1, len(pattern)):
        while i>0 and pattern[i] != pattern[j]:
            i=pi[j-1]
        if pattern[i]==pattern[j]:
            i+=1
            pattern[j]=i


    i=0
    while j<len(str_):
        while i>0 and pattern[i]!=str_[j]:
            i=pi[i-1]
        if pattern[i] == str_[j]:
            i+=1
            if i==len(pattern):
                str_=str_[:j-i+1]+str_[j+1:]
                j-=(i+1)
                i=pi[i-1]
        if (str_)==pattern:
            return "FRULA"
        j+=1

    return str_ if str_ else "FRULA"


def main():
    str_=sys.stdin.readline().strip()
    pattern=sys.stdin.readline().strip()

    print(kmp(str_, pattern))


if __name__=="__main__":
    main()