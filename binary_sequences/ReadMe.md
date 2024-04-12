## Problem

For any natural numbers N and K. Consider all N-element binary sequences such that there are no neighbouring 1's. Find K-th sequence such sequence (alphabetically).
If there is no such sequence (K is to large) return empty string

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

### Idea and algorithm
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
### Time complexity
Time complexity of this solution is limitted by number of all binary sequences smaller than K'th legal sequence. As we will see if $K = F_n$ than $K$'tk legal sequence is exactly $2^n$ sequence. From following identity for fibonacci numbers ($\varphi \approx 1.618$):
$$ F_n = \frac{\varphi^n - (-\varphi)^{-n}}{\sqrt{5}}$$
we see that $F_n = O(\varphi^n)$ and time complexity for $K = F_n$ is $O(2^n)$ Therefore:
$$K \approx \varphi^n \Rightarrow \log_{\varphi}{K} \approx n \Rightarrow \frac{\log_2{K}}{log_2{\varphi}} = C\log_2{K} \approx n$$
Where $C > 1$ therefore for $K = F_n$ time complexity is $O(2^n) = O(2^CK) = O(K)$

And if $K$ is to big to fit in $N$ digit sequence time complexity for discovering it is $O(2^N)$

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

Therefore our problem is simplified to finding Zackendorf representation of the number $K$. To check if its representation is no longer than $N$ bits we only need to check if $K < F_{N+1}$ as smallest number with representation of length $N+1$ will be $F_{N+1}$.

### Algorithm
```
fib_numbers = generate_fibonnacci_sequence(N+1)

if K-1 >= fib_numbers[-1]:
    number_is_to_big()
else:
    find_zackendorf_decomposition(K-1)
```
Where finding zackendorf decomposition looks like this:
```
res = ""
rem = K-1
skip_next = False
for fib in fibonnacci_sequence_reversed:
    if skip_next:
        res += "0"
        skip_next = False
    if fib <= rem:
        rem -= fib
        res += "1"
        skip_next = True
    else:
        res += "0"
```

### Time Complexity

Time complexity of generating fibonacci sequence is $O(N)$ finding zackendorf decomposition is also $O(N)$ so whole algorithm is $O(N)$.


## Notes

* Improvement from $O(K)$ to $O(N)$ can be significant as usually $N << K$. In fact as we have seen above theoretical upper bound for $K$ with given $N$ is $O(\varphi^N)$. So for large K and N it is practically exponential to linear.

## Acknowlegments

* Problem was originally sent to me by one of my friends, it was part of one of the programming classes at AGH university
* Idea and implementation of fibonnaci solution was created by me
