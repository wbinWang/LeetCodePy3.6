# 5 最长回文子串

# 中心扩展法
def m1(s: str) -> str:
    if not isinstance(s, str) or len(s) == 0:
        return s
    start = 0
    end = 0
    for i in range(0,len(s)):
        len1 = m1_xx(s, i, i)
        len2 = m1_xx(s, i, i + 1)
        _len = max(len1, len2)
        if _len > end - start:
            start = i - int((_len - 1) / 2)
            end = i + int(_len / 2)
    return s[start:end + 1]


def m1_xx(s: str, start : int, end : int) -> int:
    while start >= 0 and end < len(s) and s[start] == s[end]:
        start -= 1
        end += 1
    return end - start - 1


# 动态规划法
def m2(s: str) -> str:
    if not isinstance(s, str) or len(s) == 0:
        return s
    # 先把字符串倒置
    s1 = list(s)
    s1.reverse()
    s1 = "".join(s1)
    # print(s)
    # print(s1)
    # 画表格递归
    qr = []
    _max = 1
    _max_i = 0
    _max_j = 0
    _len_s = len(s)
    for i in range(0, _len_s):
        i_v = s[i]
        qr.append([])
        for j in range(0, _len_s):
            qr[i].append(0)
            j_v = s1[j]
            if i_v == j_v:
                if i > 0 and j > 0:
                    left_top_v = qr[i - 1][j - 1]
                    qr[i][j] = left_top_v + 1
                    if qr[i][j] > _max:
                        if _len_s - 1 - j + (qr[i][j] - 1) == i:
                            _max = qr[i][j]
                            _max_i = i
                            _max_j = j
                else:
                    qr[i][j] = 1
    # print(qr)
    # print(_max, _max_i, _max_j)
    return s[_max_i - _max + 1:_max_i + 1]


if __name__ == "__main__":
    s = "321012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210123210012321001232100123210123"
    # s1 = m1(s)
    s1 = m2(s)
    print(s1)