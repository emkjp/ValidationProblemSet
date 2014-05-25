# generator for bipartite matching

import sys
import random

random.seed(1)

def testcase(N, M, density) :
    edges = []
    for i in range(N):
        for j in range(M):
            if random.random() < density : 
                edges.append((i + 1, j + 1))
    K = len(edges)
    
    print N, M, K
    for edge in edges :
        print edge[0], edge[1]




testcase(1, 1, 1)
testcase(1, 100, 1)

for _ in range(2000) :
    testcase(random.randint(1, 10), random.randint(1, 10), 0.4)
    testcase(random.randint(1, 10), random.randint(1, 10), 0.2)
    testcase(random.randint(1, 10), random.randint(1, 10), 0.1)
    testcase(random.randint(1, 10), random.randint(1, 10), 0.05)
    testcase(random.randint(1, 10), random.randint(1, 10), 0.01)

for _ in range(50) :
    testcase(random.randint(1, 100), random.randint(1, 100), 0.001)
    testcase(random.randint(1, 100), random.randint(1, 100), 0.002)
    testcase(random.randint(1, 100), random.randint(1, 100), 0.004)
    testcase(random.randint(1, 100), random.randint(1, 100), 0.008)
    testcase(random.randint(1, 100), random.randint(1, 100), 0.016)
    testcase(random.randint(1, 100), random.randint(1, 100), 0.032)
    testcase(random.randint(1, 100), random.randint(1, 100), 0.064)
    testcase(random.randint(1, 100), random.randint(1, 100), 0.128)

print -1,-1,-1
