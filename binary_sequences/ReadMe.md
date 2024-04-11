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

After some time I learned that what I used in fact is Zackendorf's Theorem: https://en.wikipedia.org/wiki/Zeckendorf%27s_theorem
Theorem states that any positive integer can be uniquely represented as a sum of distinct fibonnaci numbers in such way that any two elements of the sum are not consecutive Fibonacci numbers.
Which can be 1:1 transfered to our problem! We will just consider any sequence to be binary Zackendorf representation. Therefore sequences will transfer accordingly to numbers ($F_1 = 1$, $F_2 = 2$):
$$(0100101)_2 \rightarrow F_2 + F_5 + F_7 = 2 + 8 + 21 = 31$$
$$(1010000)_2 \rightarrow F_1 + F_3= 1 + 3 = 4$$
And because of properties of Fibonacci ordered representations will be growing series! Therefore (least bit last):
$$a_0 = (0000000)_2 \rightarrow 0$$
$$a_1 = (0000001)_2 \rightarrow 1$$
$$a_2 = (0000010)_2 \rightarrow 2$$
$$a_3 = (0000100)_2 \rightarrow 3$$
$$a_4 = (0000101)_2 \rightarrow 4$$
$$a_5 = (0001000)_2 \rightarrow 5$$
$$a_6 = (0001001)_2 \rightarrow 6$$
$$a_6 = (0001010)_2 \rightarrow 7$$
$$ \cdots $$

Therefore our problem is simplified to finding Zackendorf representation of the number $K$. To check if its representation is no longer than $N$ bits we only need to check if $K < F_{N+1}$ as smallest number with representation of length $N+1$ will be $F_{N+1}.

### Algorithm
```

```

## Acknowlegments

* Idea and implementation of fibonnaci solution was created by me
