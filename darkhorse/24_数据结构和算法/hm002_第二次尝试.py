"""
如果 a+b+c=1000，且 a^2+b^2=c^2（a,b,c 为自然数），如何求出所有a、b、c可能的组合?
"""

import time

start_time = time.time()

for a in range(1001):
    for b in range(1001):
        c = 1000 - a - b
        if a ** 2 + b ** 2 == c ** 2:
            print('a, b, c: %d, %d, %d' % (a, b, c))

end_time = time.time()

print('times: %d' % (end_time - start_time))
print('finished')
"""
a, b, c: 0, 500, 500
a, b, c: 200, 375, 425
a, b, c: 375, 200, 425
a, b, c: 500, 0, 500
times: 1
finished
"""
