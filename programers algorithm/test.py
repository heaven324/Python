li = ['a', 'a', 'b', 'b', 'a', 'c', 'c', 'c', '']
cnt = 1
ans = ''
for i in range(len(li) - 1):
    if li[i] == li[i + 1]:
        cnt += 1
    else:
        if cnt != 1:
            ans = ans + str(cnt) + li[i]
            cnt = 1
        else:
            ans = ans + li[i]
print(ans)

