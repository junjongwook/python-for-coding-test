#-*- coding: utf-8 -*-
N = int(input())
result = 0
for h in range(0, N+1):
    _h = str(h)
    if '3' in _h:
        result += 3600
        continue

    result += 1575
    # for m1 in range(0, 6):
    #     if m1 == 3:
    #         result += 600
    #         continue
    #
    #     result += 195
        # for m2 in range(0, 10):
        #     if m2 == 3:
        #         result += 60
        #         continue
        #
        #     result += 15

            # for s1 in range(0, 6):
            #     if s1 == 3:
            #         result += 10
            #         continue
            #
            #     result += 1

print(result)

