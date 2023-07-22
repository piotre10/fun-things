## Problem

For any natural numbers N and K. Consider all N-element binary sequences such that there are no neighbouring 1's. Find K-th sequence such sequence.

Originally as a programming exercise boundary's for N and K was: 1 <= N <= 63 and 1 <= K <= 100000

### Example

For N=3 all possible sequences are:
a_1 = 000
a_2 = 001
a_3 = 010
011 is illegal
a_4 = 100
a_5 = 101
110 is illegal
111 is illegal

So for N=3 and K=4 correct answear is 100
Similarly for N=7 and K=10 correct answear would be 0010001

## "Easy" solution

Let's think of binary sequences as binary representations of integers then:

for each integer i starting from 0 we can check if it's binary representation is legal. If it is legal we increment some variable k, when k = K we break out and binary representation of i is our sequence. Algorithmically:
```
N = ...
K = ...

i = 0 
k = 0
while i < 2^N:
    if is_legal(i):
        k++
    if k == K:
        break

if i < 2^N:
    print(f'Found {K}-th sequence: {i}')
else:
    print('There is no {K}-th sequence for given N (K is to big)')
```

## Solution using fibonnaci sequence

TODO

## Acknowlegments

...
