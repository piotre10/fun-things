## Problem

For any natural numbers N and K. Consider all N-element binary sequences such that there are no neighbouring 1's. Find K-th sequence such sequence.

Originally as a programming exercise boundary's for N and K was: $1 \leq N \leq 63$ and $1 \leq K \leq 100000$

### Example

For $N=3$ all possible sequences are:
* 000
* 001
* 010
* 011 is illegal
* 100
* 101
* 110 is illegal
* 111 is illegal

So for $N=3$ and $K=4$ correct answear is $100$
Similarly for $N=7$ and $K=10$ correct answear would be $0010001$

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

### Idea

If we list possible sequences sorted alphabetically and group them by their length we see that we have:

* 1 "0" length sequence - "0"   Or $[0...0]$   
* 1 "1" length sequence - 1 Or $[0...0]1$
* 1 "2" length sequences - 10 Or $[0...0]10$
* 2 "3" length sequences - 100 and 101 Or $[0...0]100$, $[0...0]101$ 

and etc. As we can see each sequence of length exactly 3 is created by appending sequence of length less than 2 to a "10":

* 100 is created by appending $[0...0]$ to "10" (in this case 0)
* 101 is created by appending $[0...0]1$ to "10" (in this case 1)

similarly for sequences of length exactly 5 we would get

* 10000 is created by appennding $[0...0]$ to "10" (in this case 000) 
* 10001 is created by appennding $[0...0]1$ to "10" (in this case 001) 
* 10010 is created by appennding $[0...0]10$ to "10" (in this case 010) 
* 10100 is created by appennding $[0...0]100$ to "10" (in this case 100) 
* 10101 is created by appennding $[0...0]101$ to "10" (in this case 101) 

So if we as $a_{n}$ - number of legal sequences of length **n or less** we can see that:

$$a_{0} = 1$$
$$a_{1} = 1$$
$$a_{n+2} = a_{n+1} + a_{n}$$ 

So know for each $K$ and $N$ we get we can determine that:

1. If $K > a_{N}$ then solution does not exist
2. Otherwise we can find $i$ such that $a_{i} >= K > a_{i-1}$, then we know that sequence is in form of [0...0]10[S] where S sequence is of length lesser or equal to i-2 and should be represented as i-2 length string 
3. S in above point can be found recursively for any $N, K$ if $solution(N, K) = [0...0]10[S]$ - from point 2 then $S = solution(i-2, K-a_{i-1})$

Third point is derived from observation that if we are looking exactly i-length sequence that is K-th sequence alphabetically than $K = a_{i-1} + t$ where $t$ is positive integer and therefore is represented as $[0...0]10[S]$ where $S$ is $t$-th sequence (of course $t = K - a_{i-1}$ so $0 < t <= a_{i} - a_{i-1} = a_{i-2}$, and S should be represented by $i-2$ length sequence)

### Algorithm

...

## Acknowlegments

* Idea and implementation of fibonnaci solution was created by me
