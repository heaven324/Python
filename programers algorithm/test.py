p = "(()())()"


def trans_u(u):
    u = u[1:-1]
    ans = ''
    for i in u:
        if i == '(':
            ans += ')'
        else:
            ans += '('
    return ans

print(trans_u(p))