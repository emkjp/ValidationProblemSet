# generator for bipartite matching

import sys
import random

random.seed(1)

def testcase(N, density) :
    edges = []
    for i in range(N):
        for j in range(N):
            if random.random() < density and i != j: 
                edges.append((i + 1, j + 1))
    M = len(edges)
    S = random.randint(1, N)
    T = random.randint(1, N)
    if S == T : T = (T + 1)
    if T == N + 1 : T = 1
    print N, M, S, T
    for edge in edges :
        print edge[0], edge[1], random.randint(1, 1000) + 1


for _ in range(200) :
    testcase(random.randint(2, 20), 0.8)
    testcase(random.randint(2, 20), 0.4)
    testcase(random.randint(2, 20), 0.2)
    testcase(random.randint(2, 20), 0.1)
    testcase(random.randint(2, 20), 0.05)
    testcase(random.randint(2, 20), 0.025)

for _ in range(10) :
    testcase(random.randint(2, 100), 0.001)
    testcase(random.randint(2, 100), 0.002)
    testcase(random.randint(2, 100), 0.004)
    testcase(random.randint(2, 100), 0.008)
    testcase(random.randint(2, 100), 0.016)
    testcase(random.randint(2, 100), 0.032)
    testcase(random.randint(2, 100), 0.064)
    testcase(random.randint(2, 100), 0.128)

print -1,-1,-1,-1
