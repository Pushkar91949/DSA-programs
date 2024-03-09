def longest_common_prefix(strs):
    ans = ''
    strs = sorted(strs)
    first = strs[0]
    last = strs[-1]
    for i in range(min(len(first), len(last))):
        if first[i] != last[i]:
            return ans
        ans += first[i]

    return ans


strs = ["flower", "flow", "flight", "flicker", "flip", "flop"]
print(longest_common_prefix(strs))
