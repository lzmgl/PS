import os, sys
sys.stdin = open('tmp.txt'.format(os.path.dirname(os.path.realpath(__file__))))
sys.stdout = open('output.txt','w')
w=open('tmp2.txt', 'w', encoding='utf-8')
words = sys.stdin.readlines()
cnt=0
for sentence in words:
    if sentence == '\n' or sentence == ' \n' or sentence == '' or sentence == ' ':
        continue
    line = sentence.strip()
    if len(sentence) < 10:
        print(sentence)
        line = line.replace('\n', ' ')
        w.write(line)
    else:
        w.write(line)
        w.write('\n')
    # for c in sentence:
    #     if c != ' ' and c != '\n':
    #         cnt+=1

# print(cnt-57)