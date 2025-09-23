# from collections import Counter
# def find_idx(s: str):
#     counter = Counter(s)
#     for i in range(len(s)):
#         if counter.get(s[i]) == 1:
#             return i
#     return -1

# print(find_idx("bubsasuhb"))


#------------------------------------------------------------------------------------------------
# from typing import List
# def find_consec(nums: List):
#     _1s = 0
#     max_1s = 0
#     for i in nums:
#         if i == 1:
#             _1s += 1
#             return max(max_1s, _1s)
#         else:
#             _1s = 0
#     return _1s


# print(find_consec([1,1,1,0,0,1,1,0]))

#------------------------------------------------------------------------------------------------


def find_miss(n):
    act_sum = sum(n)
    exp_sum = sum([i for i in range(0, len(n)+1)])
    return exp_sum - act_sum