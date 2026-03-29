<!-- Slide number: 1 -->
# K. S. Institute of TechnologyDepartment of Computer Science and Engineering
Analysis and Design and of Algorithm - BCS401

Faculty Name: Vijayalaxmi Mekali
Professor, Dept of CSE
KSIT, Bangalore

22-03-2026
Dr. Vijayalaxmi Mekali, Professor, Dept of CSE, KSIT
1

### Notes:

<!-- Slide number: 2 -->
# MODULE 2 : Exhaustive Search
Exhaustive Search (Brute Force) – Definition:
Exhaustive search is a problem-solving technique in which all possible solutions are systematically generated and checked, and the best or correct solution is selected.
Simple definition:
Exhaustive search is an algorithmic method that tries every possible solution to find the correct or optimal one.
Key points:
It checks each and every possible combination of the problem. Also called brute-force method or generate-and-test approach. Guarantees finding the correct/optimal solution if one exists. Usually time-consuming for large problems (high complexity).
Example:
Trying all subsets in Knapsack problem
Checking all routes in Travelling Salesman Problem (TSP)

![Picture 3](Picture3.jpg)

![logo](Picture2.jpg)
Dr. Vijayalaxmi Mekali, Professor, Dept of CSE, KSIT
2
21-03-2026

### Notes:

<!-- Slide number: 3 -->
# MODULE 2 : Exhaustive Search
Exhaustive Search (Brute Force) – Definition:
The Knapsack problem is a problem of selecting a subset of items, each with a given weight and value, to maximize the total value (profit) without exceeding the capacity of the knapsack.
Formal Definition
Given:
A set of n items
Each item has:
Weight wi​
Value (profit) vi
A knapsack with capacity M
Goal:Select a subset of items such that:
Total selected weight ≤ M

![Picture 3](Picture3.jpg)

![logo](Picture2.jpg)
Dr. Vijayalaxmi Mekali, Professor, Dept of CSE, KSIT
3
21-03-2026

### Notes:

<!-- Slide number: 4 -->
# MODULE 2 : Exhaustive Search
Exhaustive Search (Brute Force) – Definition:
Solve Knapsack problem using Exhaustive Search for the following
 Knapsack Capacity m=10 and number of items n=4

![Picture 3](Picture3.jpg)

![logo](Picture2.jpg)
Dr. Vijayalaxmi Mekali, Professor, Dept of CSE, KSIT
4
22-03-2026

| Item | Weight | Value/Profit |
| --- | --- | --- |
| 1 | 7 | 42 |
| 2 | 3 | 12 |
| 3 | 4 | 40 |
| 4 | 5 | 25 |

### Notes:

<!-- Slide number: 5 -->
# MODULE 2 : Exhaustive Search
Solve Knapsack problem using Exhaustive Search for the following
 Knapsack Capacity m=10 and number of items n=4

![Picture 3](Picture3.jpg)

![logo](Picture2.jpg)
Dr. Vijayalaxmi Mekali, Professor, Dept of CSE, KSIT
5
22-03-2026

| Item | Weight | Value/Profit |
| --- | --- | --- |
| 1 | 7 | 42 |
| 2 | 3 | 12 |
| 3 | 4 | 40 |
| 4 | 5 | 25 |

| Subset | Items Chosen | Total Weight | Total Value | Valid (≤10)? |
| --- | --- | --- | --- | --- |
| 1 | {} | 0 | 0 | ✔ |
| 2 | {1} | 7 | 42 | ✔ |
| 3 | {2} | 3 | 12 | ✔ |
| 4 | {3} | 4 | 40 | ✔ |
| 5 | {4} | 5 | 25 | ✔ |
| 6 | {1,2} | 10 | 54 | ✔ |
| 7 | {1,3} | 11 | 82 | ✘ |
| 8 | {1,4} | 12 | 67 | ✘ |
| 9 | {2,3} | 7 | 52 | ✔ |
| 10 | {2,4} | 8 | 37 | ✔ |
Step 1: Generate All Possible Subsets (Exhaustive Search) :2^4=16 subsets:

| Subset | Items Chosen | Total Weight | Total Value | Valid (≤10)? |
| --- | --- | --- | --- | --- |
| 11 | {3,4} | 9 | 65 | ✔ |
| 12 | {1,2,3} | 14 | 94 | ✘ |
| 13 | {1,2,4} | 15 | 79 | ✘ |
| 14 | {1,3,4} | 16 | 107 | ✘ |
| 15 | {2,3,4} | 12 | 77 | ✘ |
| 16 | {1,2,3,4} | 19 | 119 | ✘ |
Optimal solution {3,4} = 65

### Notes:

<!-- Slide number: 6 -->
# MODULE 2 : Exhaustive Search

The Travelling Salesman Problem (TSP) asks for the shortest possible tour that visits each city exactly once and returns to the starting city.
Formal Definition
Given:
A set of n cities
The distance (cost) between every pair of cities
Goal:
Find a minimum-cost Hamiltonian circuit, i.e.:
Visit each city exactly once
Return to the starting city
Minimize the total travel cost

![Picture 3](Picture3.jpg)

![logo](Picture2.jpg)
Dr. Vijayalaxmi Mekali, Professor, Dept of CSE, KSIT
6
22-03-2026

### Notes:

<!-- Slide number: 7 -->
# MODULE 2 : Exhaustive Search
TSP using Exhaustive Search
From the given graph (cities a, b, c, d), the edge weights are:
a–b = 2
b–d = 3
d–c = 1
c–a = 5
a–d = 7
b–c = 8

![Picture 3](Picture3.jpg)

![logo](Picture2.jpg)
Dr. Vijayalaxmi Mekali, Professor, Dept of CSE, KSIT
7
22-03-2026

| Tour | Path | Cost Calculation | Total Cost |
| --- | --- | --- | --- |
| 1 | a → b → c → d → a | 2 + 8 + 1 + 7 | 18 |
| 2 | a → b → d → c → a | 2 + 3 + 1 + 5 | 11 ✅ |
| 3 | a → c → b → d → a | 5 + 8 + 3 + 7 | 23 |
| 4 | a → c → d → b → a | 5 + 1 + 3 + 2 | 11 ✅ |
| 5 | a → d → b → c → a | 7 + 3 + 8 + 5 | 23 |
| 6 | a → d → c → b → a | 7 + 1 + 8 + 2 | 18 |
Step 1: List All Possible Tours
Fix starting city as a (to avoid duplicates).Total tours = (n−1)!=3!=6(n-1)! = 3! = 6(n−1)!=3!=6

Optimal solution
a → b → d → c → a = 11
a → c → d → b → a = 11

### Notes:

<!-- Slide number: 8 -->
# Analysis and Design and of Algorithm - BCS401MODULE 2 : DIVIDE AND CONQUER
Divide and Conquer is best known algorithm design technique.
Divide and Conquer algorithm works according to the following general plan
A problem instance is divided into several smaller instances of the same problem (smaller sub problems of same size)
Smaller instances are solved (recursively)
Solution obtained from smaller instances are combined to get the solution for the original problem.

![Picture 3](Picture3.jpg)

![logo](Picture2.jpg)
Dr. Vijayalaxmi Mekali, Professor, Dept of CSE, KSIT
8
22-03-2026

### Notes:

<!-- Slide number: 9 -->
# MODULE 2 : DIVIDE AND CONQUER- Introduction
Divide and Conquer Methodology-Example
Detecting Counterfeit coin problem
Collection of 16 COINS, in that one is counterfeit coin. Problem to detect counterfeit coin (Duplicate coin with light weight)
Solution:

![Picture 3](Picture3.jpg)

![logo](Picture2.jpg)
Dr. Vijayalaxmi Mekali, Professor, Dept of CSE, KSIT
9
16 COINS- one is counterfeit coin
8 COINS-Set A

8 COINS Set B

4 COINS
Set A2

4 COINS
Set A1
Check the weight
Check the weight
Let weight of A< B, so Set A contains counterfeit coin
Let weight of A1< A2, so Set A1 contains counterfeit coin
2 COINS
Set A4
2 COINS
Set A3
Let weight of A3< A4, so Set A3 contains counterfeit coin
1 COINS
Set A5
1 COINS
Set A6
Let weight of A5< A6, so Set A5 is counterfeit coin
21-03-2026

### Notes:

<!-- Slide number: 10 -->
# MODULE 2 : DIVIDE AND CONQUER- Introduction

                   Fig1.1   Divide and Conquer Technique

![Picture 3](Picture3.jpg)

![logo](Picture2.jpg)
Dr. Vijayalaxmi Mekali, Professor, Dept of CSE, KSIT
10
Problem       of size n
Sub Problem 2 of size n/2
Sub Problem 1 of size n/2
Solution to
Sub Problem 1
Solution to
Sub Problem 2
Solution to
Original Problem
21-03-2026

### Notes:

<!-- Slide number: 11 -->
# MODULE 2 : DIVIDE AND CONQUER- Introduction
Control Abstraction of Divide and Conquer
 Type  DandC (P)
{
    if small (P)
             return S(P);
    else
         {
              Divide P into smaller instances  P1, P2, …..Pn,   n≥1
              Apply DandC each of smaller instances
              Return Combine (DandC(P1), DandC(P2), ….. DandC(Pn)),
          }
}

![Picture 3](Picture3.jpg)

![logo](Picture2.jpg)
Dr. Vijayalaxmi Mekali, Professor, Dept of CSE, KSIT
11
Where P is problem,
 small (P)  Boolean valued function, returns true if P is very small.
21-03-2026

### Notes:

<!-- Slide number: 12 -->
# MODULE 2 : DIVIDE AND CONQUER- Introduction
The recurrence relation

![Picture 3](Picture3.jpg)

![logo](Picture2.jpg)
Dr. Vijayalaxmi Mekali, Professor, Dept of CSE, KSIT
12
Where,
T(n) time for DandC,
n  input size is problem,
g(n)  Time to compute answer directly from small input
f(n)  Time to divide the problem and combining the solution.
21-03-2026

### Notes:

<!-- Slide number: 13 -->
# MODULE 2 : DIVIDE AND CONQUER- Introduction
Masters theorem
 In divide and conquer technique problem instance of size n is divided into two instances of size n/2.
More generally, an instance of size n can be divided into b instances of size n/b, with a of them needing to be solved. (Here, a and b are constants; a ≥ 1 and b > 1.) Assuming that size n is a power of b to simplify our analysis, we get the following recurrence
The recurrence relation for divide and conquer

![Picture 3](Picture3.jpg)

![logo](Picture2.jpg)
Dr. Vijayalaxmi Mekali, Professor, Dept of CSE, KSIT
13
Where,
a and b    known as  constants.
T(1)  assume that its value is known,
n  power of b ie n=bk
f(n)  Time to divide the problem and combining the solution.
This recurrence relation is called general divide and conquer  recurrence relation.

The order of growth of its solution T (n) depends on the values of the constants a and b and the order of growth of the function f (n).
21-03-2026

### Notes:

<!-- Slide number: 14 -->
# MODULE 2 : DIVIDE AND CONQUER- Introduction
The efficiency analysis of many divide-and-conquer algorithms is greatly simplified by the following master theorem

Master theorem: If f(n) Є Θ(nd) where d ≥ 0 in the recurrence relation then

T(n) Є

Analogous results hold for the O and Ω  notations, too.

![Picture 3](Picture3.jpg)

![logo](Picture2.jpg)
Dr. Vijayalaxmi Mekali, Professor, Dept of CSE, KSIT
14
21-03-2026

### Notes:

<!-- Slide number: 15 -->
# MODULE 2 : DIVIDE AND CONQUER- Introduction

![Picture 3](Picture3.jpg)

![logo](Picture2.jpg)
Dr. Vijayalaxmi Mekali, Professor, Dept of CSE, KSIT
15
21-03-2026

### Notes:

<!-- Slide number: 16 -->
# MODULE 2 : DIVIDE AND CONQUER- Introduction
Example: Binary Search;
Let A is a list of elements  that are in sorted order. Problem is determining the whether the given key element present in A.
     If key = A[j],
               key present at position j+1
   else
               key not presents in the list

![Picture 3](Picture3.jpg)

![logo](Picture2.jpg)
Dr. Vijayalaxmi Mekali, Professor, Dept of CSE, KSIT
16
21-03-2026

### Notes:

<!-- Slide number: 17 -->
# MODULE 2 : DIVIDE AND CONQUER- Introduction
Binary Search;

![Picture 3](Picture3.jpg)

![logo](Picture2.jpg)
Dr. Vijayalaxmi Mekali, Professor, Dept of CSE, KSIT
17
21-03-2026

|  | best | Average | Worst |
| --- | --- | --- | --- |
| Linear search | O(1) | O(n).  when the item to be searched is in some where middle of the Array | O(n). Since the target element is present in the extremitites (first or last index), |
| Binary Search | O(1) | O(logn) | O(log n) Since the target element is present in the extremitites (first or last index), there are logn comparisons in total. |
| Merge sort | O(n logn) | O(n logn) | O(n logn) Time complexity of Merge Sort is O(n\*Log n) in all the 3 cases (worst, average and best) as merge sort always divides the array in two halves and takes linear time to merge two halves. |
| Quick sort | O(n logn) | O(n logn) | O(N2). |
|  |  |  |  |
|  |  |  |  |

### Notes:

<!-- Slide number: 18 -->
# MODULE 2 : DIVIDE AND CONQUER- Introduction

![Picture 3](Picture3.jpg)

![logo](Picture2.jpg)
Dr. Vijayalaxmi Mekali, Professor, Dept of CSE, KSIT
18

|  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
A
n
high
1
low
mid
key<A[mid]
Search in lower part
Key>A[mid]
Search in lower part

21-03-2026

### Notes:

<!-- Slide number: 19 -->
# MODULE 2 : DIVIDE AND CONQUER- Introduction
Recursive Binary search algorithm
int BinSear(Type A[ ], int low, int high, type key)
{
     if (low==high)
     {
          if (key==A[low])
                return low;
          else
                 return 0;
    }

![Picture 3](Picture3.jpg)

![logo](Picture2.jpg)
Dr. Vijayalaxmi Mekali, Professor, Dept of CSE, KSIT
19

![Picture 19](Picture19.jpg)
1
low
n
high
Key==A[mid]

![Picture 24](Picture24.jpg)
1
low
high is mid-1

![Picture 31](Picture31.jpg)
n
high
low is mid+1
21-03-2026

### Notes:

<!-- Slide number: 20 -->
# MODULE 2 : DIVIDE AND CONQUER- Introduction

Example Binary search algorithm: Consider List A with 14 elements, search for the key=151 in the list

A

Solution:

![Picture 3](Picture3.jpg)

![logo](Picture2.jpg)
Dr. Vijayalaxmi Mekali, Professor, Dept of CSE, KSIT
20

| -15 | -6 | 0 | 7 | 9 | 23 | 54 | 82 | 101 | 112 | 125 | 131 | 142 | 151 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

| 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| -15 | -6 | 0 | 7 | 9 | 23 | 54 | 82 | 101 | 112 | 125 | 131 | 142 | 151 |
Index
High=14
low=1
21-03-2026

### Notes:

<!-- Slide number: 21 -->
# MODULE 2 : DIVIDE AND CONQUER- Introduction

Example Binary search algorithm: Consider List A with 14 elements, search for the key=151 in the list

Solution:

![Picture 3](Picture3.jpg)

![logo](Picture2.jpg)
Dr. Vijayalaxmi Mekali, Professor, Dept of CSE, KSIT
21

| 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | low | High | mid | compare |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| -15 | -6 | 0 | 7 | 9 | 23 | 54 | 82 | 101 | 112 | 125 | 131 | 142 | 151 | 1 | 14 | (1+14)/2=7 | 151>54 |
Index
high=14
low=8
mid=7

| 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | low | High | mid | compare |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| -15 | -6 | 0 | 7 | 9 | 23 | 54 | 82 | 101 | 112 | 125 | 131 | 142 | 151 | 8 | 14 | (8+14)/2=11 | 151>125 |
high=14
mid=11
low=1
Index
21-03-2026

### Notes:

<!-- Slide number: 22 -->
# MODULE 2 : DIVIDE AND CONQUER- Introduction

Example Binary search algorithm: Consider List A with 14 elements, search for the key=151 in the list

Solution:

![Picture 3](Picture3.jpg)

![logo](Picture2.jpg)
Dr. Vijayalaxmi Mekali, Professor, Dept of CSE, KSIT
22
Index
low=12

| 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | low | High | mid | compare |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| -15 | -6 | 0 | 7 | 9 | 23 | 54 | 82 | 101 | 112 | 125 | 131 | 142 | 151 | 12 | 14 | (12+14)/2=13 | 151>142 |
high=14
mid=13

| 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | low | High | mid | compare |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| -15 | -6 | 0 | 7 | 9 | 23 | 54 | 82 | 101 | 112 | 125 | 131 | 142 | 151 | 14 | 14 | Low=high | 151=151 |
low=14
high=14
Key=151 is found at position 14, search is successful
21-03-2026

### Notes:

<!-- Slide number: 23 -->
# MODULE 2 : DIVIDE AND CONQUER- Introduction

Example Binary search algorithm: Consider List A with 14 elements, search for the key=-14 in the list

Solution:

![Picture 3](Picture3.jpg)

![logo](Picture2.jpg)
Dr. Vijayalaxmi Mekali, Professor, Dept of CSE, KSIT
23

| 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | low | High | mid | compare |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| -15 | -6 | 0 | 7 | 9 | 23 | 54 | 82 | 101 | 112 | 125 | 131 | 142 | 151 | 1 | 14 | (1+14)/2=7 | -14<54 |
Index
high=14
low=1
mid=7

| 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | low | High | mid | compare |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| -15 | -6 | 0 | 7 | 9 | 23 | 54 | 82 | 101 | 112 | 125 | 131 | 142 | 151 | 1 | 6 | (1+6)/2=3 | -14<0 |
high=6
mid=3
low=1
Index
21-03-2026

### Notes:

<!-- Slide number: 24 -->
# MODULE 2 : DIVIDE AND CONQUER- Introduction

Example Binary search algorithm: Consider List A with 14 elements, search for the key=151 in the list

Solution:

![Picture 3](Picture3.jpg)

![logo](Picture2.jpg)
Dr. Vijayalaxmi Mekali, Professor, Dept of CSE, KSIT
24

| 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | low | High | mid | compare |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| -15 | -6 | 0 | 7 | 9 | 23 | 54 | 82 | 101 | 112 | 125 | 131 | 142 | 151 | 1 | 2 | (1+2)/2=1 | -14>-15 |
Index
low=1
mid=1

| 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | low | High | mid | compare |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| -15 | -6 | 0 | 7 | 9 | 23 | 54 | 82 | 101 | 112 | 125 | 131 | 142 | 151 | 12 | 14 | (2+2)/2=2 | -6≠-14 |
high=2
Index
low=2
high=2
Key = -14 is not found unsuccessful
21-03-2026

### Notes:

<!-- Slide number: 25 -->
# MODULE 2 : DIVIDE AND CONQUER- Introduction

Example Binary search algorithm: Consider List A with 14 elements, search for the key=9 in the list

A

Solution:

![Picture 3](Picture3.jpg)

![logo](Picture2.jpg)
Dr. Vijayalaxmi Mekali, Professor, Dept of CSE, KSIT
25

| -15 | -6 | 0 | 7 | 9 | 23 | 54 | 82 | 101 | 112 | 125 | 131 | 142 | 151 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

| 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| -15 | -6 | 0 | 7 | 9 | 23 | 54 | 82 | 101 | 112 | 125 | 131 | 142 | 151 |
Index
High=14
low=1
21-03-2026

### Notes:

<!-- Slide number: 26 -->
# MODULE 2 : DIVIDE AND CONQUER- Introduction

Example Binary search algorithm: Consider List A with 14 elements, search for the key=9 in the list

Solution:

![Picture 3](Picture3.jpg)

![logo](Picture2.jpg)
Dr. Vijayalaxmi Mekali, Professor, Dept of CSE, KSIT
26

| 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | low | High | mid | compare |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| -15 | -6 | 0 | 7 | 9 | 23 | 54 | 82 | 101 | 112 | 125 | 131 | 142 | 151 | 1 | 14 | (1+14)/2=7 | 9<54 |
Index
high=14
low=1
mid=7

| 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | low | High | mid | compare |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| -15 | -6 | 0 | 7 | 9 | 23 | 54 | 82 | 101 | 112 | 125 | 131 | 142 | 151 | 1 | 6 | (1+6)/2=3 | 9>0 |
high=6
mid=3
low=1
Index
21-03-2026

### Notes:

<!-- Slide number: 27 -->
# MODULE 2 : DIVIDE AND CONQUER- Introduction

Example Binary search algorithm: Consider List A with 14 elements, search for the key=9 in the list

Solution:

![Picture 3](Picture3.jpg)

![logo](Picture2.jpg)
Dr. Vijayalaxmi Mekali, Professor, Dept of CSE, KSIT
27
low=4

| 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | low | High | mid | compare |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| -15 | -6 | 0 | 7 | 9 | 23 | 54 | 82 | 101 | 112 | 125 | 131 | 142 | 151 | 4 | 6 | (4+6)/2=5 | 9=9 |
high=6
mid=5
Index
Key=9 is found at position 5, search is successful
21-03-2026

### Notes:

<!-- Slide number: 28 -->
# MODULE 2 : DIVIDE AND CONQUER- Introduction
Example: Binary Search- Time complexity analysis
Time complexity analysis of binary search is done for all the three case. Let T(n) indicates time efficiency
Best case – If the input array contains the key element at the middle position, then search becomes success by performing only comparison. Thus the best case efficiency is
      t(n)best ≈ (1)
2. Worst case efficiency – The worst efficiency of binary search occurs when the algorithm takes maximum number of comparisons. The time complexity is given by recurrence relation

![Picture 3](Picture3.jpg)

![logo](Picture2.jpg)
Dr. Vijayalaxmi Mekali, Professor, Dept of CSE, KSIT
28
Time required to search key element in either upper part or lower part of array
Time required to compare key with middle  element
21-03-2026

### Notes:

<!-- Slide number: 29 -->
# MODULE 2 : DIVIDE AND CONQUER- Introduction

![Picture 3](Picture3.jpg)

![logo](Picture2.jpg)
Dr. Vijayalaxmi Mekali, Professor, Dept of CSE, KSIT
29
21-03-2026

### Notes:

<!-- Slide number: 30 -->
# MODULE 2 : DIVIDE AND CONQUER- Introduction

![Picture 3](Picture3.jpg)

![logo](Picture2.jpg)
Dr. Vijayalaxmi Mekali, Professor, Dept of CSE, KSIT
30
21-03-2026

### Notes:

<!-- Slide number: 31 -->
# MODULE 2 : DIVIDE AND CONQUER- Introduction
Example: Binary Search- Time complexity analysis
When binary search is applied on the elements, we must determine
Required number of comparisons
Average number of key comparisons for both successful search and unsuccessful search
Required number of comparisons, Average number of key comparisons for both successful search
and unsuccessful search can be determined by Decision tree.
In Decision tree
Circles are used to represent an internal nodes. internal nodes represents successful search
Rectangles are used to represent an external nodes. External nodes represents unsuccessful search
Time complexity for the average case in both successful and unsuccessful search is proportional to
      height of the tree    i e      T(n)= (log2n)

![Picture 3](Picture3.jpg)

![logo](Picture2.jpg)
Dr. Vijayalaxmi Mekali, Professor, Dept of CSE, KSIT
31
21-03-2026

### Notes:

<!-- Slide number: 32 -->
# MODULE 2 : DIVIDE AND CONQUER- Introduction
Example: Binary Search- Time complexity analysis
Theorem: If n (size of list ) is in the range (2k-1, 2k), then binary search algorithm makes at most
    k elements comparisons for a successful search and either k-1 or k comparisons for unsuccessful search.
[Time complexity for both successful and unsuccessful search is  height of the tree    i e      T(n)= (log2n)
Proof:
Consider the binary decision tree describing the action of binary search algorithm on n elements.
All successful search end at a circular node whereas all unsuccessful searches end at a Square node.
If 2k-1 ≤ n ≤ 2k, then all the circular nodes are at level 1, 2, …..k, where as all the square nodes are at
     level k and k+1 (root at the level 1).
The number of elements comparisons needed to terminate at a circular node on level i is i,
whereas  the number of element comparisons needed to terminate at a square node at level i is only i-1.
The theorem follows
        Successful searches                                                     Unsuccessful searches
    (log2n), (log2n) and  (1)                                                    (log2n), (log2n) and  (log2n)
     (Worst, average, best)                                                          (Worst, average, best)

![Picture 3](Picture3.jpg)

![logo](Picture2.jpg)
Dr. Vijayalaxmi Mekali, Professor, Dept of CSE, KSIT
32
21-03-2026

### Notes:

<!-- Slide number: 33 -->
# MODULE 2 : DIVIDE AND CONQUER- Introduction
Example: Binary Search- Time complexity analysis
Example: Write a binary decision tree for the following five elements  and also find the average number of comparisons in both successful and unsuccessful search.
List A is 10, 15, 19, 25, 96
Solution:

![Picture 3](Picture3.jpg)

![logo](Picture2.jpg)
Dr. Vijayalaxmi Mekali, Professor, Dept of CSE, KSIT
33

| Index | 1 | 2 | 3 | 4 | 5 |
| --- | --- | --- | --- | --- | --- |
| A | 10 | 15 | 19 | 25 | 96 |
| NOC | 2 | 3 | 1 | 2 | 3 |
3
4
1
5
2

L=1
H=5
L=4
L=2
L=5
L=1
H=2
H=0
H=5
H=2
H=4
L=3
H=2
L=5
L=6
H=5
L=4
H=3
L=1
H=5
H=1
L=2
19
25
10
96
15
Level -1
Level -2
Level -3
Level -4
21-03-2026

### Notes:

<!-- Slide number: 34 -->
# MODULE 2 : DIVIDE AND CONQUER- Introduction

![Picture 3](Picture3.jpg)

![logo](Picture2.jpg)
Dr. Vijayalaxmi Mekali, Professor, Dept of CSE, KSIT
34

| Number of nodes Level number\*Number of successful nodes in each level | Comparisons |
| --- | --- |
| 1\*1 | 1 |
| 2\*2 | 4 |
| 3\*2 | 6 |
| Total comparisons = 11 |  |
21-03-2026

### Notes:

<!-- Slide number: 35 -->
# MODULE 2 : DIVIDE AND CONQUER- Introduction

![Picture 3](Picture3.jpg)

![logo](Picture2.jpg)
Dr. Vijayalaxmi Mekali, Professor, Dept of CSE, KSIT
35

| Number of nodes Number of unsuccessful nodes in each level \* Level number-1 | Comparisons |
| --- | --- |
| 2\*(3-1) | 4 |
| 4\*(4-1) | 12 |
| Total comparisons = 16 |  |
21-03-2026

### Notes:

<!-- Slide number: 36 -->
# MODULE 2 : DIVIDE AND CONQUER- Introduction
Example: Binary Search- Time complexity analysis
Example: Write a binary decision tree for the following five elements  and also find the average number of comparisons in both successful and unsuccessful search.
List A is -15, -6, 0, 7, 9, 23, 24, 82, 101
Solution:

![Picture 3](Picture3.jpg)

![logo](Picture2.jpg)
Dr. Vijayalaxmi Mekali, Professor, Dept of CSE, KSIT
36

| Index | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| A | -15 | -6 | 0 | 7 | 9 | 23 | 24 | 82 | 101 |
| NOC |  |  |  |  |  |  |  |  |  |
21-03-2026

### Notes:

<!-- Slide number: 37 -->
# MODULE 2 : DIVIDE AND CONQUER- Introduction
Solution:

![Picture 3](Picture3.jpg)

![logo](Picture2.jpg)
Dr. Vijayalaxmi Mekali, Professor, Dept of CSE, KSIT
37

| Index | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| A | -15 | -6 | 0 | 7 | 9 | 23 | 24 | 82 | 101 |
| NOC | 3 | 2 | 3 | 4 | 1 | 3 | 2 | 3 | 4 |
5
3
2
4
1

L=1
H=9
L=3
L=2
L=8
L=1
H=0
H=5
H=4
H=4
L=4
H=4
L=5
L=6
H=6
L=6
H=3
L=1
H=9
H=1
9
82
-6
7
Level -1
Level -2
Level -3
Level -4
L=1
H=1
-15
H=4
0
L=3
H=2

L=4

7
24
6
L=6

L=7
23
H=6

H=9
8
L=8
H=7

L=9
H=9
9
101
L=9
H=8

H=9
L=10
Level -5
21-03-2026

### Notes:

<!-- Slide number: 38 -->
# MODULE 2 : DIVIDE AND CONQUER- Introduction

![Picture 3](Picture3.jpg)

![logo](Picture2.jpg)
Dr. Vijayalaxmi Mekali, Professor, Dept of CSE, KSIT
38

| Number of nodes Level number\*Number of successful nodes in each level | Comparisons |
| --- | --- |
| 1\*1 | 1 |
| 2\*2 | 4 |
| 3\*4 | 12 |
| 4\*2 | 8 |
| Total comparisons = 25 |  |
21-03-2026

### Notes:

<!-- Slide number: 39 -->
# MODULE 2 : DIVIDE AND CONQUER- Introduction

![Picture 3](Picture3.jpg)

![logo](Picture2.jpg)
Dr. Vijayalaxmi Mekali, Professor, Dept of CSE, KSIT
39

| Number of nodes Number of unsuccessful nodes in each level \* Level number-1 | Comparisons |
| --- | --- |
| 6\*(4-1) | 18 |
| 4\*(5-1) | 16 |
| Total comparisons = 34 |  |
21-03-2026

### Notes:

<!-- Slide number: 40 -->
# MODULE 2 : DIVIDE AND CONQUER- Introduction
Solution:

![Picture 3](Picture3.jpg)

![logo](Picture2.jpg)
Dr. Vijayalaxmi Mekali, Professor, Dept of CSE, KSIT
40

| Index | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| A | -15 | -6 | 0 | 7 | 9 | 23 | 24 | 82 | 101 |
| NOC | 3 | 2 | 3 | 4 | 1 | 3 | 2 | 3 | 4 |
7
5
3
6
1

L=1
H=14
L=4
L=2
L=12
L=1
H=0
H=8
H=6
H=6
L=6
H=6
L=7
L=8
H=10
L=8
H=5
L=1
H=14
H=2
54
142
0
23
Level -1
Level -2
Level -3
Level -4
L=1
H=2
-15
H=6
9
L=4
H=4

L=6

11
125
9
L=8
L=10
101
H=10
H=14
13
L=12
H=12
L=14
H=14
14
151
L=14
H=13

H=14
L=15
Level -5
2

L=2
H=1
H=2
L=3
4
7
-6

L=4
H=3
L=5
H=4
8
82

H=8
H=7
L=8
L=9
10
112

L=10
L=11
H=9
H=10
12
131

L=12
L=13
H=11
H=12
21-03-2026

### Notes:

<!-- Slide number: 41 -->
# MODULE 2 : DIVIDE AND CONQUER- Introduction

![Picture 3](Picture3.jpg)

![logo](Picture2.jpg)
Dr. Vijayalaxmi Mekali, Professor, Dept of CSE, KSIT
41

| Number of nodes Level number\*Number of successful nodes in each level | Comparisons |
| --- | --- |
| 1\*1 | 1 |
| 2\*2 | 4 |
| 3\*4 | 12 |
| 4\*7 | 28 |
| Total comparisons = 45 |  |
21-03-2026

### Notes:

<!-- Slide number: 42 -->
# MODULE 2 : DIVIDE AND CONQUER- Introduction

![Picture 3](Picture3.jpg)

![logo](Picture2.jpg)
Dr. Vijayalaxmi Mekali, Professor, Dept of CSE, KSIT
42

| Number of nodes Number of unsuccessful nodes in each level \* Level number-1 | Comparisons |
| --- | --- |
| 1\*(4-1) | 3 |
| 14\*(5-1) | 56 |
| Total comparisons = 59 |  |
21-03-2026

### Notes:

<!-- Slide number: 43 -->
# MODULE 2 : DIVIDE AND CONQUER- Introduction
Example: Binary Search- Time complexity analysis
Theorem: Prove that Binary search tree has more comparisons in unsuccessful search that in successful search
Proof :
Assume E=I+2n
Where
E is sum of distances of the external nodes to the root node
I is sum of distances of the internal nodes to the root node
n is number of elements

![Picture 3](Picture3.jpg)

![logo](Picture2.jpg)
Dr. Vijayalaxmi Mekali, Professor, Dept of CSE, KSIT
43

Level 2
Level 3
Level 1
Level 4
21-03-2026

### Notes:

<!-- Slide number: 44 -->
# MODULE 2 : DIVIDE AND CONQUER- Introduction

I=0+2*1+4*2=0+2+8=10
E=3*8=24
n=7
Substituting in I+2n  we get
10+2*7=24=E
S(n) is average no of comparison in successful search is   S(n)= 1+I/n
U(n) is average no of comparison in unsuccessful search is   U(n) = E/(n+1)
Thus average no of comparisons in successful case is
S(n)= 1+10/7 =17/7 = 2.43
Thus average no of comparisons in unsuccessful case is
U(n)= 24/(1+7) =24/8 = 3

![Picture 3](Picture3.jpg)

![logo](Picture2.jpg)
Dr. Vijayalaxmi Mekali, Professor, Dept of CSE, KSIT
44
21-03-2026

### Notes:

<!-- Slide number: 45 -->
# MODULE 2 : DIVIDE AND CONQUER- Introduction

![Picture 3](Picture3.jpg)

![logo](Picture2.jpg)
Dr. Vijayalaxmi Mekali, Professor, Dept of CSE, KSIT
45
21-03-2026

### Notes:

<!-- Slide number: 46 -->
# MODULE 2 : DIVIDE AND CONQUER- Merge sort

![Picture 3](Picture3.jpg)

![logo](Picture2.jpg)
Dr. Vijayalaxmi Mekali, Professor, Dept of CSE, KSIT
46
21-03-2026

### Notes:

<!-- Slide number: 47 -->
# MODULE 2 : DIVIDE AND CONQUER- Merge sort
Merge sort
ALGORITHM
Mergesort (A[0..n − 1])
//Sorts array A[0..n − 1] by recursive mergesort
//Input: An array A[0..n − 1] of orderable elements
//Output: Array A[0..n − 1] sorted in nondecreasing order
if n > 1
      copy A[0..n/2 − 1] to B[0..n/2 − 1]
      copy A[n/2..n − 1] to C[0..n/2 − 1]
      Mergesort(B[0..n/2 − 1])
     Mergesort(C[0..n/2 − 1])
      Merge(B, C, A)

![Picture 3](Picture3.jpg)

![logo](Picture2.jpg)
Dr. Vijayalaxmi Mekali, Professor, Dept of CSE, KSIT
47
ALGORITHM
Merge (B[0..p − 1], C[0..q − 1], A[0..p + q − 1])
//Merges two sorted arrays into one sorted array
//Input: Arrays B[0..p − 1] and C[0..q − 1] both sorted
//Output: Sorted array A[0..p + q − 1] of the elements of B and C
i ←0; j ←0; k←0
while i <p and j <q do
      if B[i]≤ C[j ]
              A[k]←B[i]; i ←i + 1
     else
              A[k]←C[j ]; j ←j + 1
     k←k + 1
     if i = p
               copy C[j..q − 1] to A[k..p + q − 1]
else
               copy B[i..p − 1] to A[k..p + q − 1]

21-03-2026

### Notes:

<!-- Slide number: 48 -->
# MODULE 2 : DIVIDE AND CONQUER- Merge sort
Merge sort- Example
Trace the merge sort algorithm for a given list of elements
8,  3,  2,  9,  7,  1,  5,  4
Solution:

Array size is n=8

![Picture 3](Picture3.jpg)

![logo](Picture2.jpg)
Dr. Vijayalaxmi Mekali, Professor, Dept of CSE, KSIT
48

| 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 8 | 3 | 2 | 9 | 7 | 1 | 5 | 4 |
Index

A

21-03-2026

### Notes:

<!-- Slide number: 49 -->
# MODULE 2 : DIVIDE AND CONQUER- Merge sort

![Picture 3](Picture3.jpg)

![logo](Picture2.jpg)
Dr. Vijayalaxmi Mekali, Professor, Dept of CSE, KSIT
49

| 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 8 | 3 | 2 | 9 | 7 | 1 | 5 | 4 |

| 7 | 1 | 5 | 4 |
| --- | --- | --- | --- |

| 8 | 3 | 2 | 9 |
| --- | --- | --- | --- |

| 8 | 3 |
| --- | --- |

| 2 | 9 |
| --- | --- |

| 3 |
| --- |

| 8 |
| --- |

| 9 |
| --- |

| 2 |
| --- |

| 5 | 4 |
| --- | --- |

| 7 | 1 |
| --- | --- |

| 7 |
| --- |

| 1 |
| --- |

| 5 |
| --- |

| 4 |
| --- |

| 3 | 8 |
| --- | --- |

| 2 | 9 |
| --- | --- |

| 1 | 7 |
| --- | --- |

| 4 | 5 |
| --- | --- |

| 2 | 3 | 8 | 9 |
| --- | --- | --- | --- |

| 1 | 4 | 5 | 7 |
| --- | --- | --- | --- |

| 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 2 | 3 | 4 | 5 | 7 | 8 | 9 |
Dividing

Conquering

Sorted list

This tree is called recursive tree call

21-03-2026

### Notes:

<!-- Slide number: 50 -->
# MODULE 2 : DIVIDE AND CONQUER- Merge sort
Merge sort- Example
Trace the merge sort algorithm for a given list of elements  (Dec 2019/Jan 2020)
  60, 50, 25, 10, 35, 25, 75, 30
Solution:

Array size is n=8

![Picture 3](Picture3.jpg)

![logo](Picture2.jpg)
Dr. Vijayalaxmi Mekali, Professor, Dept of CSE, KSIT
50

| 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 60 | 50 | 25 | 10 | 35 | 25 | 75 | 30 |
Index

A

21-03-2026

### Notes:

<!-- Slide number: 51 -->
# MODULE 2 : DIVIDE AND CONQUER- Merge sort

![Picture 3](Picture3.jpg)

![logo](Picture2.jpg)
Dr. Vijayalaxmi Mekali, Professor, Dept of CSE, KSIT
51

| 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 60 | 50 | 25 | 10 | 35 | 25 | 75 | 30 |

| 35 | 25 | 75 | 30 |
| --- | --- | --- | --- |

| 60 | 50 | 25 | 10 |
| --- | --- | --- | --- |

| 60 | 50 |
| --- | --- |

| 25 | 10 |
| --- | --- |

| 50 |
| --- |

| 60 |
| --- |

| 10 |
| --- |

| 25 |
| --- |

| 75 | 30 |
| --- | --- |

| 35 | 25 |
| --- | --- |

| 35 |
| --- |

| 25 |
| --- |

| 75 |
| --- |

| 30 |
| --- |

| 50 | 60 |
| --- | --- |

| 10 | 25 |
| --- | --- |

| 25 | 35 |
| --- | --- |

| 30 | 75 |
| --- | --- |

| 10 | 25 | 50 | 60 |
| --- | --- | --- | --- |

| 25 | 30 | 35 | 75 |
| --- | --- | --- | --- |

| 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 10 | 25 | 25 | 30 | 35 | 50 | 60 | 75 |
Dividing

Conquering

Sorted list

This tree is called recursive tree call

21-03-2026

### Notes:

<!-- Slide number: 52 -->
# MODULE 2 : DIVIDE AND CONQUER- Merge sort
Merge sort- Example
Trace the merge sort algorithm for a given list of elements
  5, 1, 3, 2, 100, 8, 17
Solution:

Array size is n=7

![Picture 3](Picture3.jpg)

![logo](Picture2.jpg)
Dr. Vijayalaxmi Mekali, Professor, Dept of CSE, KSIT
52

| 0 | 1 | 2 | 3 | 4 | 5 | 6 |
| --- | --- | --- | --- | --- | --- | --- |
| 5 | 1 | 3 | 2 | 100 | 8 | 17 |
Index

A

21-03-2026

### Notes:

<!-- Slide number: 53 -->
# MODULE 2 : DIVIDE AND CONQUER- Merge sort

![Picture 3](Picture3.jpg)

![logo](Picture2.jpg)
Dr. Vijayalaxmi Mekali, Professor, Dept of CSE, KSIT
53

| 0 | 1 | 2 | 3 | 4 | 5 | 6 |
| --- | --- | --- | --- | --- | --- | --- |
| 5 | 1 | 3 | 2 | 100 | 8 | 17 |

| 100 | 8 | 17 |
| --- | --- | --- |

| 5 | 1 | 3 | 2 |
| --- | --- | --- | --- |

| 5 | 1 |
| --- | --- |

| 3 | 2 |
| --- | --- |

| 1 |
| --- |

| 5 |
| --- |

| 2 |
| --- |

| 3 |
| --- |

| 17 |
| --- |

| 100 | 8 |
| --- | --- |

| 100 |
| --- |

| 8 |
| --- |

| 1 | 5 |
| --- | --- |

| 2 | 3 |
| --- | --- |

| 8 | 100 |
| --- | --- |

| 17 |
| --- |

| 1 | 2 | 3 | 5 |
| --- | --- | --- | --- |

| 8 | 17 | 100 |
| --- | --- | --- |

| 0 | 1 | 2 | 3 | 4 | 5 | 6 |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | 2 | 3 | 5 | 8 | 17 | 100 |
Dividing

Conquering

Sorted list

This tree is called recursive tree call

21-03-2026

### Notes:

<!-- Slide number: 54 -->
# MODULE 2 : DIVIDE AND CONQUER- Merge sort
Time complexity Analysis of Merge sort
Input size- n
Basic operation- Divide and merge of n elements
As basic operation depends only on input size either worst, average or best case can be computed, let os consider worst case complexity
Recurrence relation for merge sort is

![Picture 3](Picture3.jpg)

![logo](Picture2.jpg)
Dr. Vijayalaxmi Mekali, Professor, Dept of CSE, KSIT
54
Time required to sort left part of the array

Time required to sort right part of the array

Time required to divide and merge list with n elements

21-03-2026

### Notes:

<!-- Slide number: 55 -->
# MODULE 2 : DIVIDE AND CONQUER- Merge sort

![Picture 3](Picture3.jpg)

![logo](Picture2.jpg)
Dr. Vijayalaxmi Mekali, Professor, Dept of CSE, KSIT
55
T(n)worst = (n logn)
21-03-2026

### Notes:

<!-- Slide number: 56 -->
# MODULE 2 : DIVIDE AND CONQUER- Quick sort
Quick sort
Quicksort is the other important sorting algorithm that is based on the divide-and conquer approach.
Quicksort divides input elements according to their value.
A partition is an arrangement of the array’s elements so that
All the elements to the left of some element A[S] are less than or equal to A[S],
and all the elements to the right of A[S] are greater than or equal to A[S],
Specifically it rearranges the elements of a given array A[0……n-1] to achieve its partition, a situation where all the elements before some position S are less than or equal to A[S], and all the elements after position S  are greater than or equal to A[S]

After partition of A[0,1, 2,…….n-1]
                  A[0,1, 2,…….S-1]      A[S]      A[S+1, S+2, ……..n-1]

![Picture 3](Picture3.jpg)

![logo](Picture2.jpg)
Dr. Vijayalaxmi Mekali, Professor, Dept of CSE, KSIT
56

All are ≤ A[S]

All are ≥ A[S]

After partition A[S] will be in its final position in the sorted array  and continue the sorting of the two sub arrays of elements preceding A[S] i e A[0,1, 2,…….S-1]  and following A[S] i e
A[S+1, S+2, ……..n-1]

21-03-2026

### Notes:

<!-- Slide number: 57 -->
# MODULE 2 : DIVIDE AND CONQUER- Quick sort
Quick sort Algorithm
ALGORITHM Quicksort(A[l . . . . . r])
//Sorts a subarray by quicksort
//Input: Subarray of array A[0..n − 1], defined by its left indices l and right indices r
//Output: Subarray A[l . . . . . r]  sorted in nondecreasing order
if l < r
        s ←Partition(A[l. . . .r]) //s is a split position
        Quicksort(A[l. . . s − 1])
        Quicksort(A[s + 1. . . . r])

![Picture 3](Picture3.jpg)

![logo](Picture2.jpg)
Dr. Vijayalaxmi Mekali, Professor, Dept of CSE, KSIT
57
21-03-2026

### Notes:

<!-- Slide number: 58 -->
# MODULE 2 : DIVIDE AND CONQUER- Quick sort
Quick sort Algorithm
Quicksort(A[s + 1. . . . r])
ALGORITHM Partition(A[l..r])
//Partitions a subarray by Hoare’s algorithm, using the first element as a pivot
//Input: Subarray of array A[0..n − 1], defined by its left and right indices l and r (l<r)
//Output: Partition of A[l..r], with the split position returned as this function’s value
   p←A[l]
   i ←l;     j ←r + 1
  repeat
            repeat i ←i + 1 until A[i]≥ p
            repeat j ←j − 1 until A[j ]≤ p
            swap(A[i], A[j ])
until i ≥ j
swap(A[i], A[j ]) //undo last swap when i ≥ j
swap(A[l], A[j ])  // swap pivot p with A[j]
return j

![Picture 3](Picture3.jpg)

![logo](Picture2.jpg)
Dr. Vijayalaxmi Mekali, Professor, Dept of CSE, KSIT
58
21-03-2026

### Notes:

<!-- Slide number: 59 -->
# MODULE 2 : DIVIDE AND CONQUER- Quick sort
Quick sort Example
Trace the quick sort  algorithm for the following data set  and also construct tree for a recursive call
5,  3,  1,  9,  8,  2,  4,  7
Solution:
n=8

![Picture 3](Picture3.jpg)

![logo](Picture2.jpg)
Dr. Vijayalaxmi Mekali, Professor, Dept of CSE, KSIT
59

| 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 5 | 3 | 1 | 9 | 8 | 2 | 4 | 7 |
Index

Array elements

A

21-03-2026
l=0, r=7
i=l i.e i=0
j=r+1

### Notes:

<!-- Slide number: 60 -->
# MODULE 2 : DIVIDE AND CONQUER- Quick sort

![Picture 3](Picture3.jpg)

![logo](Picture2.jpg)
Dr. Vijayalaxmi Mekali, Professor, Dept of CSE, KSIT
60

|  | 3 | 1 | 9 | 8 | 2 | 4 | 7 |
| --- | --- | --- | --- | --- | --- | --- | --- |
5
i

j

|  | 3 | 1 | 9 | 8 | 2 | 4 | 7 |
| --- | --- | --- | --- | --- | --- | --- | --- |
5
3 < 5

i

7 > 5

j

|  | 3 | 1 | 9 | 8 | 2 | 4 | 7 |
| --- | --- | --- | --- | --- | --- | --- | --- |
5
1 < 5

i

4 > 5

j

|  | 3 | 1 | 9 | 8 | 2 | 4 | 7 |
| --- | --- | --- | --- | --- | --- | --- | --- |
9 < 5

i

j

5

|  | 3 | 1 | 4 | 8 | 2 | 9 | 7 |
| --- | --- | --- | --- | --- | --- | --- | --- |
5
i

j

First element is pivot
Initially i=0  and j=8 , increment i and decrement j
Now i points second element and j points to last element
3 is less than  5 (pivot), so i++
7 is great than  5 (pivot), so j--

1 is less than 5( pivot), so i++
4 is not great than 5 (pivot), so no change in j
9 is not less than  5, so no change in i ,  Increment of i and decrement of j stopped
i<j   swap A[i] and A[j] i e 9 and 4
i++  and  j--
pivot

21-03-2026

### Notes:

<!-- Slide number: 61 -->
# MODULE 2 : DIVIDE AND CONQUER- Quick sort

![Picture 3](Picture3.jpg)

![logo](Picture2.jpg)
Dr. Vijayalaxmi Mekali, Professor, Dept of CSE, KSIT
61

|  | 3 | 1 | 4 | 8 | 2 | 9 | 7 |
| --- | --- | --- | --- | --- | --- | --- | --- |
5
j

|  | 3 | 1 | 4 | 2 | 8 | 9 | 7 |
| --- | --- | --- | --- | --- | --- | --- | --- |
5
i

j

2 > 5

3 < 2

i

j

2
2
i

8 < 5

| 2 | 3 | 1 | 4 |  | 8 | 9 | 7 |
| --- | --- | --- | --- | --- | --- | --- | --- |

| 3 | 1 | 4 |
| --- | --- | --- |
4 > 2

| 3 | 1 | 4 |
| --- | --- | --- |
i

j

5
8 is not less than 5, so no change in i , 2 is not greater than 5 so no change in j
i<j   swap A[i] and A[j] i e 8 and 2
i++ and j--
 j  > i   swap A[j] and pivot.
After swap A[j] and pivot, pivot is in its final position, all the elements before pivot are lesser than it and all the elements after pivot are greater than it, thus array is partitioned into two parts
Consider first part in that 2 is pivot, 3 is not less than  pivot, so no change in i , 4 is greater than pivot so j--
1 is not greater than pivot so no change in j
21-03-2026
s=4

### Notes:

<!-- Slide number: 62 -->
# MODULE 2 : DIVIDE AND CONQUER- Quick sort

![Picture 3](Picture3.jpg)

![logo](Picture2.jpg)
62
i

j

7 > 8

3 < 2

i

j

2
2
8 < 5

| 1 | 3 | 4 |
| --- | --- | --- |
1 > 2

| 3 | 1 | 4 |
| --- | --- | --- |
i

j

| 1 | 3 | 4 |
| --- | --- | --- |
2

|  | 4 |
| --- | --- |
3
i  j

|  | 4 |
| --- | --- |
3

|  | 4 |
| --- | --- |

|  | 9 | 7 |
| --- | --- | --- |
8
i

j

 9 < 8

|  | 7 | 9 |
| --- | --- | --- |
i

j

8

| 7 |  | 9 |
| --- | --- | --- |
8
Final sorted array is
 1     2     3    4    5    7    8      9

i<j, swap A[i] and A[j] i e 3 and 1
1< 2, so i++, j>2, j++
j > i, swap A[j] and pivot.
After swapping pivot is in its final position array is divided into two parts
3 is pivot, i and j points to 4, 4 >3, j++, j>I pivot is less than A[i[ no swap
Second part of array
8 is pivot, 9 is not less
than 8 so change in i and
7 is not greater than
8 so no change in j,
swap A[i] and A[j]
j > i,
swap A[j] and pivot
21-03-2026
Dr. Vijayalaxmi Mekali, Professor, Dept of CSE, KSIT
s=1
s=2
s=6

### Notes:

<!-- Slide number: 63 -->
# MODULE 2 : DIVIDE AND CONQUER- Quick sort
Recursive tree call for the example considered in previous slide is

![Picture 3](Picture3.jpg)

![logo](Picture2.jpg)
Dr. Vijayalaxmi Mekali, Professor, Dept of CSE, KSIT
63
Initially entire array is considered thus l=0 and r=7 (l is index for first element and r is index for last element of array) and s is partition index that pivot occupies and it is it’s sorted  final index.

| l=0, r=7 |
| --- |
| s=4 |

| l=0, r=3 |
| --- |
| s=1 |

| l=2, r=3 |
| --- |
| s=2 |

| l=0, r=0 |
| --- |
|  |

| l=5, r=7 |
| --- |
| s=6 |

| l=7, r=7 |
| --- |
|  |

| l=5, r=5 |
| --- |
|  |

| l=2, r=1 |
| --- |
|  |

| l=3, r=3 |
| --- |
|  |
21-03-2026

### Notes:

<!-- Slide number: 64 -->
# MODULE 2 : DIVIDE AND CONQUER- Quick sort
Quick sort Example
Trace the quick sort  algorithm for the following data set  and also construct tree for a recursive call
65,  70,  75,  80,  85,  60,  55,  50, 45
Solution:
n=9

![Picture 3](Picture3.jpg)

![logo](Picture2.jpg)
Dr. Vijayalaxmi Mekali, Professor, Dept of CSE, KSIT
64

| 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 65 | 70 | 75 | 80 | 85 | 60 | 55 | 50 | 45 |
Index

Array elements

A

21-03-2026
l=0, r=7
i=l i.e i=0
j=r+1

### Notes:

<!-- Slide number: 65 -->
# MODULE 2 : DIVIDE AND CONQUER- Quick sort

![Picture 3](Picture3.jpg)

![logo](Picture2.jpg)
Dr. Vijayalaxmi Mekali, Professor, Dept of CSE, KSIT
65
65
i

j

70 < 65
i
j
75 < 65

i
50 > 65

j
65 First element is pivot
Increment I and decrement j. i points to second element and j to last element

70 is not less than  65, so no change in i
45 is not great than  65, so no change in j,
i<j, swap A[i] and A[j], i++ and  j--

| 70 | 75 | 80 | 85 | 60 | 55 | 50 | 45 |
| --- | --- | --- | --- | --- | --- | --- | --- |
pivot

65

| 70 | 75 | 80 | 85 | 60 | 55 | 50 | 45 |
| --- | --- | --- | --- | --- | --- | --- | --- |
45 > 65

| 45 | 75 | 80 | 85 | 60 | 55 | 50 | 70 |
| --- | --- | --- | --- | --- | --- | --- | --- |
65
50 > 65
75 is not less than  65, so no change in i
50 is not great than  65, so no change in j,
i<j, swap A[i] and A[j], i++ and  j--

65

| 45 | 50 | 80 | 85 | 60 | 55 | 75 | 70 |
| --- | --- | --- | --- | --- | --- | --- | --- |
i
j
80 < 65

55 > 65
80 is not less than  65, so no change in i
55 is not great than  65, so no change in j,
i<j, swap A[i] and A[j], i++ and j--

21-03-2026

### Notes:

<!-- Slide number: 66 -->
# MODULE 2 : DIVIDE AND CONQUER- Quick sort

![Picture 3](Picture3.jpg)

![logo](Picture2.jpg)
Dr. Vijayalaxmi Mekali, Professor, Dept of CSE, KSIT
66
65
i
j
85 < 65
i
j
85 is not less than  65, so no change in i
60 is not great than  65, so no change in j,
i<j, swap A[i] and A[j],  i++ and  j--

pivot

65
60 > 65
i ≥ j
Swap 65 (Pivot) and A[j]. all the elements before pivot are lesser than it and all the elements after pivot are greater than it, thus array is partitioned into two parts

| 45 | 50 | 55 | 85 | 60 | 80 | 75 | 70 |
| --- | --- | --- | --- | --- | --- | --- | --- |

| 45 | 50 | 55 | 60 | 85 | 80 | 75 | 70 |
| --- | --- | --- | --- | --- | --- | --- | --- |

| 60 | 45 | 50 | 55 | 85 | 80 | 75 | 70 |
| --- | --- | --- | --- | --- | --- | --- | --- |
65

65-Pivot is in final position.
21-03-2026
S=4

### Notes:

<!-- Slide number: 67 -->
# MODULE 2 : DIVIDE AND CONQUER- Quick sort

![Picture 3](Picture3.jpg)

![logo](Picture2.jpg)
Dr. Vijayalaxmi Mekali, Professor, Dept of CSE, KSIT
67
i
j
45 < 60
i
j
Consider first part apply quick sort
pivot

55 > 60
i ≥ j
Swap 60 and A[j]. all the elements before 60 are lesser than it and no elements towards right of 60

|  | 45 50 | 55 |
| --- | --- | --- |
60
60
i
j
50 is less than  60, so  i++
60
j
i
60 is pivot element
45 is less than  60, so i++
55 is not great than  60, so no change in j,

| 45 50 | 55 |
| --- | --- |
50 < 60

| 55 45 50 |
| --- |
60

| 45 50 | 55 |
| --- | --- |
60 is in final position.
21-03-2026
S=3

### Notes:

<!-- Slide number: 68 -->
# MODULE 2 : DIVIDE AND CONQUER- Quick sort

![Picture 3](Picture3.jpg)

![logo](Picture2.jpg)
Dr. Vijayalaxmi Mekali, Professor, Dept of CSE, KSIT
68
45 < 55
i
j
Consider first part apply quick sort
pivot

50 > 55
i ≥ j
Swap Pivot and A[j]. all the elements before pivot are lesser than it and no elements towards right of pivot

55
i
j
55 is pivot 45 is less than  pivot, so i++
50 is not great than  pivot, so no change in j,

| 45 |
| --- |

| 45 50 |
| --- |
55

| 45 50 |
| --- |

| 50 45 |
| --- |
55
Pivot is in final position.
50
i
i ≥ j
Swap Pivot and A[j]. all the elements before pivot are lesser than it and no elements towards right of pivot

| 45 |
| --- |
50
Pivot is in final position.
j
j
i
21-03-2026
S=2
S=1

### Notes:

<!-- Slide number: 69 -->
# MODULE 2 : DIVIDE AND CONQUER- Quick sort

![Picture 3](Picture3.jpg)

![logo](Picture2.jpg)
Dr. Vijayalaxmi Mekali, Professor, Dept of CSE, KSIT
69
i
j
Consider second part apply quick sort
pivot

i ≥ j
Swap Pivot and A[j]. all the elements before pivot are lesser than it and no elements towards right of pivot

85 is pivot 80 is less than  pivot, so i++
70 is not great than  pivot, so no change in j,

85
Pivot is in final position.

| 80 | 75 | 70 |
| --- | --- | --- |
80 < 85
70 > 85
85

| 80 | 75 | 70 |
| --- | --- | --- |
i
j
75 < 85
75 is less than  pivot, so i++
70 is not great than  pivot, so no change in j,

85

| 80 | 75 | 70 |
| --- | --- | --- |
i
j

| 70 | 80 75 |
| --- | --- |
85
21-03-2026
S=8

### Notes:

<!-- Slide number: 70 -->
# MODULE 2 : DIVIDE AND CONQUER- Quick sort

![Picture 3](Picture3.jpg)

![logo](Picture2.jpg)
Dr. Vijayalaxmi Mekali, Professor, Dept of CSE, KSIT
70
i
j
Consider second part apply quick sort
pivot

70 is pivot80 is not less than  pivot so no change in i
75 is great than  pivot, so j--,

Pivot is in final position.
80 < 70
75 > 70
70
i
j
75 < 85
j

| 80 75 |
| --- |
70

| 80 75 |
| --- |

| 75 |
| --- |
i ≥ j
Swap Pivot and A[j]. all the elements before pivot are lesser than it and no elements towards right of pivot

80 is great than  pivot, so j--,

| 80 75 |
| --- |
70

| 75 |
| --- |
80
j
i
80
Pivot is in final position.
Final sorted array is
 45, 50, 55, 60, 65, 70, 75, 80, 85
21-03-2026
S=5
S=7

### Notes:

<!-- Slide number: 71 -->
# MODULE 2 : DIVIDE AND CONQUER- Quick sort
Recursive tree call for the example considered in previous slide is

![Picture 3](Picture3.jpg)

![logo](Picture2.jpg)
Dr. Vijayalaxmi Mekali, Professor, Dept of CSE, KSIT
71
Index

Array elements

| l=0, r=8 |
| --- |
| s=4 |

| l=0, r=3 |
| --- |
| s=3 |

| l=4, r=3 |
| --- |
|  |

| l=0, r=2 |
| --- |
| s=2 |

| l=5, r=8 |
| --- |
| s=8 |

| l=9, r=8 |
| --- |
|  |

| l=5, r=7 |
| --- |
| s=5 |

| l=0, r=1 |
| --- |
| s=1 |

| l=3, r=2 |
| --- |
|  |

| l=6, r=7 |
| --- |
| s=7 |

| l=5, r=4 |
| --- |
|  |

| l=2, r=1 |
| --- |
|  |

| l=0, r=0 |
| --- |
|  |

| l=8, r=7 |
| --- |
|  |

| l=6, r=6 |
| --- |
|  |
21-03-2026

### Notes:

<!-- Slide number: 72 -->
# MODULE 2 : DIVIDE AND CONQUER- Quick sort
Quick sort Example
Trace the quick sort  algorithm for the following data set  and also construct tree for a recursive call
E     X     A      M      P      L      E
Solution:
n=7

![Picture 3](Picture3.jpg)

![logo](Picture2.jpg)
Dr. Vijayalaxmi Mekali, Professor, Dept of CSE, KSIT
72

| 0 | 1 | 2 | 3 | 4 | 5 | 6 |
| --- | --- | --- | --- | --- | --- | --- |
| E | X | A | M | P | L | E |
Index

Array elements

A

21-03-2026

### Notes:

<!-- Slide number: 73 -->
# MODULE 2 : DIVIDE AND CONQUER- Quick sort

![Picture 3](Picture3.jpg)

![logo](Picture2.jpg)
Dr. Vijayalaxmi Mekali, Professor, Dept of CSE, KSIT
73
E
i

j

i
j
L > E

i
j
First element is pivot
Initialize i to second element and j to last element

M is not less than  pivot, so no change in i
P is great than  pivot, so j--
pivot

E
E > E
E
i
j
P > E

| X | A | M | P | L | E |
| --- | --- | --- | --- | --- | --- |
X < E

| X | A | M | P | L | E |
| --- | --- | --- | --- | --- | --- |

| E | A | M | P | L | X |
| --- | --- | --- | --- | --- | --- |
E

| E | A | M | P | L | X |
| --- | --- | --- | --- | --- | --- |
A < E
M < E
X is not less than  pivot, so no change in i
E is not great than  pivot, so no change in j,
i<j, swap A[i] and A[j],
i++ and j--
A is  less than  pivot, so i++
Lis great than  pivot, so j--
21-03-2026

### Notes:

<!-- Slide number: 74 -->
# MODULE 2 : DIVIDE AND CONQUER- Quick sort

![Picture 3](Picture3.jpg)

![logo](Picture2.jpg)
Dr. Vijayalaxmi Mekali, Professor, Dept of CSE, KSIT
74
E
i

M > E

j
i
pivot

| E | A | M | P | L | X |
| --- | --- | --- | --- | --- | --- |

| A | E | M | P | L | X |
| --- | --- | --- | --- | --- | --- |
Pivot is in final position.
E

| E |
| --- |
A
A

| E |
| --- |
j
M is not less than  pivot, so no change in i
M is great than  pivot, so j–
i ≥ j, swap A[j] and pivot
j

Consider first part apply quick sort
Pivot is in final position.
21-03-2026
S=2
S=0
i

### Notes:

<!-- Slide number: 75 -->
# MODULE 2 : DIVIDE AND CONQUER- Quick sort

![Picture 3](Picture3.jpg)

![logo](Picture2.jpg)
Dr. Vijayalaxmi Mekali, Professor, Dept of CSE, KSIT
75
j
i
M
i ≥ j
Swap Pivot and A[j]. all the elements before pivot are lesser than it and no elements towards right of pivot

Pivot is in final position.

| L | P | X |
| --- | --- | --- |
j
i

| L | P | X |
| --- | --- | --- |
M

| X |
| --- |
i
j
Consider first part apply quick sort
L < M

X >  M

L is less than  pivot, so i++
X is great than  pivot, so j–

| L | P | X |
| --- | --- | --- |
M
i
j
P (A[i])  is not less than  pivot, so no change in i
 P (A[j]) is great than  pivot, so j–

| L | P | X |
| --- | --- | --- |
M

| X |
| --- |
P
i
i
X (A[i])  is not less than  pivot, so no change in i
 X (A[j]) is great than  pivot, so j–

| X |
| --- |
P
j
j
Final sorted array is
 A E E L M P X
21-03-2026
S=4
S=5

### Notes:

<!-- Slide number: 76 -->
# MODULE 2 : DIVIDE AND CONQUER- Quick sort
Recursive tree call for the example considered in previous slide is

![Picture 3](Picture3.jpg)

![logo](Picture2.jpg)
Dr. Vijayalaxmi Mekali, Professor, Dept of CSE, KSIT
76
Index

Array elements

| l=0, r=6 |
| --- |
| s=2 |

| l=0, r=1 |
| --- |
| s=0 |

| l=1, r=1 |
| --- |
|  |

| l=0, r=-1 |
| --- |
|  |

| l=3, r=6 |
| --- |
| s=4 |

| l=5, r=6 |
| --- |
| s=5 |

| l=3, r=3 |
| --- |
|  |

| l=5, r=4 |
| --- |
|  |

| l=6, r=6 |
| --- |
|  |
21-03-2026

### Notes:

<!-- Slide number: 77 -->
# MODULE 2 : DIVIDE AND CONQUER- Quick sort
Time complexity Analysis of Quick sort
Input size- n
Basic operation- Divide and merge of n elements
As basic operation depends only on input size and also values of list, thus  worst, average and best case all can be computed. let us consider
Best case complexity
This case occurs when the pivot is at the centre and divides the array into two equal parts. The recurrence relation is given as

![Picture 3](Picture3.jpg)

![logo](Picture2.jpg)
Dr. Vijayalaxmi Mekali, Professor, Dept of CSE, KSIT
77
Time required to sort left part of the array

Time required to sort right part of the array

Time required to divide and merge list with n elements

No sorting required

21-03-2026

### Notes:

<!-- Slide number: 78 -->
# MODULE 2 : DIVIDE AND CONQUER- Merge sort
Time complexity Analysis of Quick sort
Input size- n
Basic operation- Divide and merge of n elements
As basic operation depends only on input size and also values of list, thus  worst, average and best case all can be computed. let us consider
Best case complexity
This case occurs when the pivot is at the centre and divides the array into two equal parts. The recurrence relation is given as

![Picture 3](Picture3.jpg)

![logo](Picture2.jpg)
Dr. Vijayalaxmi Mekali, Professor, Dept of CSE, KSIT
78
Time required to sort left part of the array

Time required to sort right part of the array

Time required to divide and merge list with n elements

No sorting required

21-03-2026

### Notes:

<!-- Slide number: 79 -->
# MODULE 2 : DIVIDE AND CONQUER- Merge sort

![Picture 3](Picture3.jpg)

![logo](Picture2.jpg)
Dr. Vijayalaxmi Mekali, Professor, Dept of CSE, KSIT
79
The best case time complexity is   T(n)best = (n logn)
21-03-2026

### Notes:

<!-- Slide number: 80 -->
# MODULE 2 : DIVIDE AND CONQUER- Quick sort
Time complexity Analysis of Quick sort
Worst case complexity
This case occurs when at the each invocation of the quick sort, the current array is partitioned into two sub array in that one is completely empty. Another contains all the elements for sorting.
This situation occurs if all the input elements are in ascending or descending order.
Example
 22,  33,  44,  55,  66   input array

 22,  33,  44,  55,  66

22,  33,  44,  55,  66

![Picture 3](Picture3.jpg)

![logo](Picture2.jpg)
Dr. Vijayalaxmi Mekali, Professor, Dept of CSE, KSIT
80
pivot

j

i

33<22

66>22, j--

i

j

55>22, j--

21-03-2026

### Notes:

<!-- Slide number: 81 -->
# MODULE 2 : DIVIDE AND CONQUER- Merge sort
Time complexity Analysis of Quick sort

 22,  33,  44,  55,  66

22,  33,  44,  55,  66

22,  33,  44,  55,  66

![Picture 3](Picture3.jpg)

![logo](Picture2.jpg)
Dr. Vijayalaxmi Mekali, Professor, Dept of CSE, KSIT
81
j

i

44>22, j--

i

j

33>22, j--

j

i

Pivot in final position
And no elements towards left of pivot, and there are n-1 elements at right, same problem continue with other elements

In general if array has n elements, after partioning, in the worst case (n-1) elements appears towards right and 0 elements towards left (if input array is in ascending order) of pivot element.

21-03-2026

### Notes:

<!-- Slide number: 82 -->
# MODULE 2 : DIVIDE AND CONQUER- Quick sort

![Picture 3](Picture3.jpg)

![logo](Picture2.jpg)
Dr. Vijayalaxmi Mekali, Professor, Dept of CSE, KSIT
82
The worst case time complexity is   T(n)worst = (n2)

Zero number of elements left part of the array, thus T(0)=0)
divide and sort the elements
(n-1) number of elements right part of the array, thus T(n-1))
21-03-2026
i

### Notes:

<!-- Slide number: 83 -->
# MODULE 2 : DIVIDE AND CONQUER- Merge sort
Time complexity Analysis of Quick sort
Average  case complexity
This case occurs when the given array may not be exactly portioned into subarray or may not be skewed as in worst case.
The pivot appears at any arbitrary position in the array ranging from 0 to n-1
Let us consider k is partition position

![Picture 3](Picture3.jpg)

![logo](Picture2.jpg)
Dr. Vijayalaxmi Mekali, Professor, Dept of CSE, KSIT
83
left part of the array
With k-1 elements

Partition position

Right part of array
n-k elements

| A[0] | A[1] | ………….. | A[k] | A[k+1] | A[k+2] | ……. | A[n-1] |
| --- | --- | --- | --- | --- | --- | --- | --- |

21-03-2026

### Notes:

<!-- Slide number: 84 -->
# MODULE 2 : DIVIDE AND CONQUER- Quick sort
Time to sort left part of the array
In left part
Lower bound = 0
Upper bound = k-1
Thus no of elements in left part are obtained as
Upper bound - lower bound+1
k-1-0+1=k
As there k no of elements in left part, time to sort left part is T(k)     Eq 1.

2. Time to sort right part of the array
Lower bound = k+1
Upper bound = n-1
Thus no of elements in right part are obtained as
Upper bound - lower bound +1
n-1-(k+1)+1
= n – k
As there n – k  no of elements in right part, time sort right part is T(n-k)     Eq 2.

![Picture 3](Picture3.jpg)

![logo](Picture2.jpg)
Dr. Vijayalaxmi Mekali, Professor, Dept of CSE, KSIT
84
21-03-2026

### Notes:

<!-- Slide number: 85 -->
# MODULE 2 : DIVIDE AND CONQUER- Quick sort

![Picture 3](Picture3.jpg)

![logo](Picture2.jpg)
Dr. Vijayalaxmi Mekali, Professor, Dept of CSE, KSIT
85
21-03-2026

### Notes:

<!-- Slide number: 86 -->
# MODULE 2 : DIVIDE AND CONQUER- Quick sort

![Picture 3](Picture3.jpg)

![logo](Picture2.jpg)
Dr. Vijayalaxmi Mekali, Professor, Dept of CSE, KSIT
86
21-03-2026

### Notes:

<!-- Slide number: 87 -->
# MODULE 2 : DIVIDE AND CONQUER- Quick sort

![Picture 3](Picture3.jpg)

![logo](Picture2.jpg)
Dr. Vijayalaxmi Mekali, Professor, Dept of CSE, KSIT
87
21-03-2026

### Notes:

<!-- Slide number: 88 -->
# MODULE 2 : DIVIDE AND CONQUER- Quick sort

![Picture 3](Picture3.jpg)

![logo](Picture2.jpg)
Dr. Vijayalaxmi Mekali, Professor, Dept of CSE, KSIT
88
21-03-2026

### Notes:

<!-- Slide number: 89 -->
# MODULE 2 : DIVIDE AND CONQUER- Quick sort

![Picture 3](Picture3.jpg)

![logo](Picture2.jpg)
Dr. Vijayalaxmi Mekali, Professor, Dept of CSE, KSIT
89
21-03-2026

### Notes:

<!-- Slide number: 90 -->
# MODULE 2 : DIVIDE AND CONQUER- Max-Min algorithm
Max-Min algorithm
It is algorithm used to find the maximum and minimum element in the given list of elements.
Different situations are possible.
If list contains only one element, then that element itself is Max or Min element.
When there are only two elements in the list, then simple comparison is sufficient to determine the Max and min element.
     if(a[0]< a[1])
{
         min=a[0]
         max=a[1]
}
else
{
         min=a[1]
         max=a[0]
}

![Picture 3](Picture3.jpg)

![logo](Picture2.jpg)
Dr. Vijayalaxmi Mekali, Professor, Dept of CSE, KSIT
90
21-03-2026

### Notes:

<!-- Slide number: 91 -->
# MODULE 2 : DIVIDE AND CONQUER- Max-Min algorithm
3. When there are more number of elements in the list, then Maxmin( ) algorithm is applied recursively to find maximum and minimum elements in the array.
Algorithm
maxmin( int i, int j, type max, type min)
// array A[0….n-1] is input array.
// i and j are 0 ≤ i ≤ j ≤ (n-1)
// Algorithm set the maximum and minimum element of a[0…n-1] to max and min variable respectively.
{
   if (i = j) max=min=a[i];// array with only one element.
    else if (i = j-1) // array with only two element.
     {
         if(a[i]< a[j])
{
         min=a[i]
         max=a[j]
}
else
{
         min=a[j]
         max=a[i]
}}

![Picture 3](Picture3.jpg)

![logo](Picture2.jpg)
Dr. Vijayalaxmi Mekali, Professor, Dept of CSE, KSIT
91
21-03-2026

### Notes:

<!-- Slide number: 92 -->
# MODULE 2 : DIVIDE AND CONQUER- Max-Min algorithm
else
{
  // array is not small, split the array
     mid=(i+j)/2
     maxmin(i, mid, max, min);
     maxmin(mid+1, j, max1, min1)
  // combine the solution
          if(max< max1)
max= max1]
if(min> min1)
min=min1;
}
}

![Picture 3](Picture3.jpg)

![logo](Picture2.jpg)
Dr. Vijayalaxmi Mekali, Professor, Dept of CSE, KSIT
92
21-03-2026

### Notes:

<!-- Slide number: 93 -->
# MODULE 2 : DIVIDE AND CONQUER- Maxmin algorithm
Maxmin algorithm Example
Trace the Maxmin algorithm for a given list of elements and also construct the recursive calls tree
22, 13, -5, -8,  15, 60, 17, 31, 47
Solution:

Array size is n=9

![Picture 3](Picture3.jpg)

![logo](Picture2.jpg)
Dr. Vijayalaxmi Mekali, Professor, Dept of CSE, KSIT
93

| 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 22 | 13 | -5 | -8 | 15 | 60 | 17 | 31 | 47 |
Index

A

21-03-2026

### Notes:

<!-- Slide number: 94 -->
# MODULE 2 : DIVIDE AND CONQUER- Maxmin algorithm

![Picture 3](Picture3.jpg)

![logo](Picture2.jpg)
Dr. Vijayalaxmi Mekali, Professor, Dept of CSE, KSIT
94
Max=22

Dividing

Min=13

Min=-5

Max=-5

Max=-5

Min=-8

Max=60

Min=17

Min=31

Max=22

Min=-8

Max=47

Min=17

Max=60

Max=60

Merging

0, 8
0, 4
5, 8
3, 4
0, 2
7, 8
5, 6
2, 2
0, 1
Max=15

0, 2
Max=22

Max=-5

5, 8
0, 4
0, 8
Min=-8

| 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 22 | 13 | -5 | -8 | 15 | 60 | 17 | 31 | 47 |
21-03-2026

### Notes:

<!-- Slide number: 95 -->
# MODULE 2 : DIVIDE AND CONQUER- Maxmin algorithm
Maxmin algorithm Example
Trace the Maxmin algorithm for a given list of elements and also construct the recursive calls tree
65, 70, 75, 80, 85, 60, 55, 50, 45.
Solution:

Array size is n=9

![Picture 3](Picture3.jpg)

![logo](Picture2.jpg)
Dr. Vijayalaxmi Mekali, Professor, Dept of CSE, KSIT
95

| 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 65 | 70 | 75 | 80 | 85 | 60 | 55 | 50 | 45 |
Index

A

Min=-8

21-03-2026

### Notes:

<!-- Slide number: 96 -->
# MODULE 2 : DIVIDE AND CONQUER- Maxmin algorithm

![Picture 3](Picture3.jpg)

![logo](Picture2.jpg)
Dr. Vijayalaxmi Mekali, Professor, Dept of CSE, KSIT
96
Max=70

Dividing

Min=65

Min=75

Max=-5

Max=75

Min=80

Max=60

Min=55

Min=45

Max=85

Min=65

Max=50

Min=45

Max=60

Max=85

Merging

0, 8
0, 4
5, 8
3, 4
0, 2
7, 8
5, 6
2, 2
0, 1
Max=85

0, 2
Max=75

Min=65

5, 8
0, 4
0, 8
Min=45

| 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 65 | 70 | 75 | 80 | 85 | 60 | 55 | 50 | 45 |
21-03-2026

### Notes:

<!-- Slide number: 97 -->
# MODULE 2 : DIVIDE AND CONQUER- Merge sort
Time complexity Analysis of Maxmin
Input size- n
Basic operation- Divide and merge of n elements
As basic operation depends only on input size
Case 1: when list has only one element, that element itself is max and min T(1)=0
Case 2: when list has only two element, that element one is max and other is  min and only comparison is required  T(2)=1
Case 3: when list has only more number of elements n>2, that list is divided into two parts of equal size, thus recurrence relation is

![Picture 3](Picture3.jpg)

![logo](Picture2.jpg)
Dr. Vijayalaxmi Mekali, Professor, Dept of CSE, KSIT
97
Time required to sort left part of the array

Time required to sort right part of the array

21-03-2026

### Notes:

<!-- Slide number: 98 -->
# MODULE 2 : DIVIDE AND CONQUER- Quick sort
Time complexity Analysis
The above recurrence relation can be rewritten as
Apply substitution method
T(n)=2T(n/2)+2       replace T(n/2) by 2T(n/4)+2
T(n)=2[2T(n/4)+2]+2  replace T(n/4) by 2T(n/8)+2
T(n)=4[2T(n/8)+2]+4+2
T(n)=23 T(n/23)+23 +22 +2

;
;
T(n)=2i-1 T(n/2i-1)+2i-1 +2i-2 +……+23 +22 +2
Let us assume 2i = n, take log on both sides
Log22 = log2n
i=log2n

![Picture 3](Picture3.jpg)

![logo](Picture2.jpg)
Dr. Vijayalaxmi Mekali, Professor, Dept of CSE, KSIT
98
21-03-2026

### Notes:

<!-- Slide number: 99 -->
# MODULE 2 : DIVIDE AND CONQUER- Strassens Matrix Multiplication
Traditional matrix multiplication algorithm

for   i 1  to n do
   for   j 1  to n do
       C(i, j) = 0
           for   k 1  to n do
                 C(i, j) = C(i, j) + A (i, k)*B(k, j)
          repeat
     repeat
 repeat
Time complexity of above algorithm is Θ(n3) (three for loops).

![Picture 3](Picture3.jpg)

![logo](Picture2.jpg)
Dr. Vijayalaxmi Mekali, Professor, Dept of CSE, KSIT
99
21-03-2026

### Notes:

<!-- Slide number: 100 -->
# MODULE 2 : DIVIDE AND CONQUER- Strassens Matrix Multiplication

![Picture 3](Picture3.jpg)

![logo](Picture2.jpg)
Dr. Vijayalaxmi Mekali, Professor, Dept of CSE, KSIT
100
This requires eight multiplications

Apply divide and conquer method on the matrices, ie divide the matrix into small equal size matrix
21-03-2026

### Notes:

<!-- Slide number: 101 -->
# MODULE 2 : DIVIDE AND CONQUER- Strassens Matrix Multiplication
Strassens Matrix Multiplication

C11 = P + S – T + V
C12 = R + T
C21 = Q + S
C22 = P + R – Q + U
Where
P = ( A11 + A22 ) (B11 + B22)
Q = ( A21 + A22 ) (B11)
R = ( A11 ) (B12 -  B22)
S = ( A22 ) (B21 -  B11)
T = ( A11 + A12 ) (B22)
U = ( A21 – A11 ) (B11 + B12)
V = ( A12 -  A22 ) (B21 + B22)

![Picture 3](Picture3.jpg)

![logo](Picture2.jpg)
Dr. Vijayalaxmi Mekali, Professor, Dept of CSE, KSIT
101
From the Strassens matrix multiplication we need to perform only SEVEN multiplication operations
21-03-2026

### Notes:

<!-- Slide number: 102 -->
# MODULE 2 : DIVIDE AND CONQUER- Strassens Matrix Multiplication

![Picture 3](Picture3.jpg)

![logo](Picture2.jpg)
Dr. Vijayalaxmi Mekali, Professor, Dept of CSE, KSIT
102
21-03-2026

### Notes:

<!-- Slide number: 103 -->
# MODULE 2 : DIVIDE AND CONQUER- Strassens Matrix Multiplication
Strassens Matrix Multiplication

P = ( A11 + A22 ) (B11 + B22)  = (1 + 6) × (8 + 2) = 7 × 10 = 70
Q = ( A21 + A22 ) (B11) = (5 + 6) × 8 = 11 × 8 = 88
R = ( A11 ) (B12 -  B22) = 1 × (7 – 2) = 1 × 5 = 5
S = ( A22 ) (B21 -  B11) = ( 6 ) ×  (1 -  8) =6 × -7 = -42
T = ( A11 + A12 ) (B22) = ( 1 + 2 ) × (2) = 3 × 2 = 6
U = ( A21 – A11 ) (B11 + B12) = ( 5 – 1 ) × (8 + 7) = 4 × 15 = 60
V = ( A12 -  A22 ) (B21 + B22) = (2 -  6 ) × (1 + 2) = -4 ×  3 = -12
WKT
C11 = 70 – 42  – 6 – 12 = 10
C12 = 5 + 6 = 11
C21 = 88 – 42 = 46
C22 = 70 + 5 – 88 + 60 = 47

![Picture 3](Picture3.jpg)

![logo](Picture2.jpg)
Dr. Vijayalaxmi Mekali, Professor, Dept of CSE, KSIT
103
21-03-2026

### Notes:

<!-- Slide number: 104 -->
# MODULE 2 : DIVIDE AND CONQUER- Strassens Matrix Multiplication

![Picture 3](Picture3.jpg)

![logo](Picture2.jpg)
Dr. Vijayalaxmi Mekali, Professor, Dept of CSE, KSIT
104
A11
A12
A21
A22
B11
B12
B21
B22
21-03-2026

### Notes:

<!-- Slide number: 105 -->
# MODULE 2 : DIVIDE AND CONQUER- Strassens Matrix Multiplication

![Picture 3](Picture3.jpg)

![logo](Picture2.jpg)
Dr. Vijayalaxmi Mekali, Professor, Dept of CSE, KSIT
105
21-03-2026

### Notes:

<!-- Slide number: 106 -->
# MODULE 2 : DIVIDE AND CONQUER- Strassens Matrix Multiplication

![Picture 3](Picture3.jpg)

![logo](Picture2.jpg)
Dr. Vijayalaxmi Mekali, Professor, Dept of CSE, KSIT
106
21-03-2026

### Notes:

<!-- Slide number: 107 -->
# MODULE 2 : DIVIDE AND CONQUER- Strassens Matrix Multiplication

![Picture 3](Picture3.jpg)

![logo](Picture2.jpg)
Dr. Vijayalaxmi Mekali, Professor, Dept of CSE, KSIT
107
21-03-2026

### Notes:

<!-- Slide number: 108 -->
# MODULE 2 : DIVIDE AND CONQUER- Strassens Matrix Multiplication

![Picture 3](Picture3.jpg)

![logo](Picture2.jpg)
Dr. Vijayalaxmi Mekali, Professor, Dept of CSE, KSIT
108
21-03-2026

### Notes:

<!-- Slide number: 109 -->
# MODULE 2 : DIVIDE AND CONQUER- Strassens Matrix Multiplication

![Picture 3](Picture3.jpg)

![logo](Picture2.jpg)
Dr. Vijayalaxmi Mekali, Professor, Dept of CSE, KSIT
109
21-03-2026

### Notes:

<!-- Slide number: 110 -->
# MODULE 2 : DIVIDE AND CONQUER- Strassens Matrix Multiplication

![Picture 3](Picture3.jpg)

![logo](Picture2.jpg)
Dr. Vijayalaxmi Mekali, Professor, Dept of CSE, KSIT
110
21-03-2026

### Notes:

<!-- Slide number: 111 -->
# MODULE 2 : DIVIDE AND CONQUER- Strassens Matrix Multiplication

![Picture 3](Picture3.jpg)

![logo](Picture2.jpg)
Dr. Vijayalaxmi Mekali, Professor, Dept of CSE, KSIT
111
21-03-2026

### Notes:

<!-- Slide number: 112 -->
# MODULE 2 : DIVIDE AND CONQUER- Strassens Matrix Multiplication

![Picture 3](Picture3.jpg)

![logo](Picture2.jpg)
Dr. Vijayalaxmi Mekali, Professor, Dept of CSE, KSIT
112
21-03-2026

### Notes:

<!-- Slide number: 113 -->
# MODULE 2 : DIVIDE AND CONQUER- Strassens Matrix Multiplication

![Picture 3](Picture3.jpg)

![logo](Picture2.jpg)
Dr. Vijayalaxmi Mekali, Professor, Dept of CSE, KSIT
113
21-03-2026

### Notes:

<!-- Slide number: 114 -->
# MODULE 2 : DIVIDE AND CONQUER- Strassens Matrix Multiplication

![Picture 3](Picture3.jpg)

![logo](Picture2.jpg)
114
21-03-2026
Dr. Vijayalaxmi Mekali, Professor, Dept of CSE, KSIT

### Notes:

<!-- Slide number: 115 -->
# MODULE 2 : DIVIDE AND CONQUER- Strassens Matrix Multiplication
Time complexity Analysis
Strassens Matrix Multiplication algorithm is efficient for large value of n, not for small value of n.
In this algorithm, if all seven computations are performed recursively then the recurrence relation is given as follows

The above recurrence relation can be rewritten as
Apply substitution method
T(n)=7T(n/2)       replace T(n/2) by 7T(n/4)
T(n)=7[7T(n/4)]  replace T(n/2) by 7T(n/8)
T(n)=72[7T(n/8)]
T(n)=73T(n/8)]
;
;
T(n)=7iT(n/2i)
To get terminal condition Let us assume 2i = n,
T(n)=7iT(n/n) = 7iT(1) = 7i
 T(n) = 7i
We have  2i = n, take log both sides
i = log2n
T(n) = 7log2n = n log 27 = n2.087

![Picture 3](Picture3.jpg)

![logo](Picture2.jpg)
Dr. Vijayalaxmi Mekali, Professor, Dept of CSE, KSIT
115
The time complexity is   T(n) = Θ(n2.087)

21-03-2026

### Notes:

<!-- Slide number: 116 -->
# MODULE 2 : DIVIDE AND CONQUER- Strassens Matrix Multiplication
Advantages of Divide and Conquer
Easier to obtain the solution
It uses cache memory

![Picture 3](Picture3.jpg)

![logo](Picture2.jpg)
Dr. Vijayalaxmi Mekali, Professor, Dept of CSE, KSIT
116
21-03-2026

### Notes:

<!-- Slide number: 117 -->
# MODULE 2 : DIVIDE AND CONQUER- Decrease and Conquer
Decrease and Conquer Technique
The decrease and conquer technique is similar to divide and conquer, except instead of partitioning a problem into multiple subproblems of smaller size, we use some technique to reduce our problem into a single problem that is smaller than the original. The smaller problem might be:
• Decreased by some constant
• Decreased by some constant factor
• Variable decrease

![Picture 3](Picture3.jpg)

![logo](Picture2.jpg)
Dr. Vijayalaxmi Mekali, Professor, Dept of CSE, KSIT
117

![Picture 5](Picture5.jpg)
21-03-2026

### Notes:

<!-- Slide number: 118 -->
# MODULE 2 : DIVIDE AND CONQUER- Decrease and Conquer
Decrease and Conquer Technique
• Decreased by some constant
In the decrease-by-a-constant variation, the size of an instance is reduced by the same constant on each iteration of the algorithm.
Typically, this constant is equal to one although other constant size reductions do happen occasionally.
Consider, as an example, the exponentiation problem of computing an where a ≠ 0 and n is a nonnegative integer. The relationship between a solution to an instance of size n and an instance of size n − 1 is obtained by the obvious formula
an = an−1 . a. So the function f (n) = an can be computed either “top down” by using its recursive definition or “bottom up” by multiplying 1 by a n times

![Picture 3](Picture3.jpg)

![logo](Picture2.jpg)
Dr. Vijayalaxmi Mekali, Professor, Dept of CSE, KSIT
118
21-03-2026

### Notes:

<!-- Slide number: 119 -->
# MODULE 2 : DIVIDE AND CONQUER- Decrease and Conquer
Decrease and Conquer Technique
• Decreased by some constant

![Picture 3](Picture3.jpg)

![logo](Picture2.jpg)
Dr. Vijayalaxmi Mekali, Professor, Dept of CSE, KSIT
119

![Picture 5](Picture5.jpg)

![Picture 8](Picture8.jpg)
21-03-2026

### Notes:

<!-- Slide number: 120 -->
# MODULE 2 : DIVIDE AND CONQUER- Decrease and Conquer
Decrease and Conquer Technique
• Decreased by some constant factor
The decrease-by-a-constant-factor technique suggests reducing a problem instance by the same constant factor on each iteration of the algorithm.
In most applications, this constant factor is equal to two. (Can you give an example of such an algorithm?) For an example, let us revisit the exponentiation problem. If the instance of size n is to compute an, the instance of half its size is to compute an/2, with the
obvious relationship between the two: an = (an/2)2. But since we consider here instances with integer exponents only, the former does not work for odd n. If n is odd, we have to compute an−1 by using the rule for even-valued exponents and then multiply the result by a. To summarize, we have the following formula:

![Picture 3](Picture3.jpg)

![logo](Picture2.jpg)
Dr. Vijayalaxmi Mekali, Professor, Dept of CSE, KSIT
120
21-03-2026

### Notes:

<!-- Slide number: 121 -->
# MODULE 2 : DIVIDE AND CONQUER- Decrease and Conquer
Decrease and Conquer Technique
• Decreased by some constant factor

![Picture 3](Picture3.jpg)

![logo](Picture2.jpg)
Dr. Vijayalaxmi Mekali, Professor, Dept of CSE, KSIT
121

![Picture 5](Picture5.jpg)

![Picture 8](Picture8.jpg)
21-03-2026

### Notes:

<!-- Slide number: 122 -->
# MODULE 2 : DIVIDE AND CONQUER- Decrease and Conquer
Decrease and Conquer Technique
• variable-size-decrease
Finally, in the variable-size-decrease variety of decrease-and-conquer, the size-reduction pattern varies from one iteration of an algorithm to another. Euclid’s algorithm for computing the greatest common divisor provides a good example of such a situation. Recall that this algorithm is based on the formula
gcd(m, n) = gcd(n, m mod n).
Decrease and conquer problems can be solved using top town approach(recursive approach) or bottom up approach(iterative approach)

![Picture 3](Picture3.jpg)

![logo](Picture2.jpg)
Dr. Vijayalaxmi Mekali, Professor, Dept of CSE, KSIT
122
21-03-2026

### Notes:

<!-- Slide number: 123 -->
# MODULE 2 : DIVIDE AND CONQUER- Decrease and Conquer
Topological sorting
Topological sorting is applied only for Directed graphs or Digraph.
Directed graph or digraph is a graph with directions specified for all the edges. The adjacency matrix and adjacency lists are still two principal means of representing a digraph. Below shows the example of directed graph.

Directed Cycle in Digraph: A directed cycle in a digraph is a sequence of three or more of its vertices that starts and ends with the same vertex. Below graph has directed cycle aba.

![Picture 3](Picture3.jpg)

![logo](Picture2.jpg)
Dr. Vijayalaxmi Mekali, Professor, Dept of CSE, KSIT
123

![https://upload.wikimedia.org/wikipedia/commons/thumb/8/89/4-tournament.svg/90px-4-tournament.svg.png](Picture2.jpg)

![Picture 8](Picture8.jpg)
21-03-2026

### Notes:

<!-- Slide number: 124 -->
# MODULE 2 : Decrease and Conquer
Insertion sort
This is a technique to sort an array A[0…..n-1] using decrease and conquer technique
In this we assume that the smaller problem of sorting the array A[0…n-2] has already been solved to give us a sorted array of size n-1 i. e
A[0]≤A[1]…..A[n-2] has already been solved to give us a sorted array of size n-1:
A[0] ≤…. A[n-2].
Three alternatives for insertion sort
Scan the sorted subarray from left to right untill  the first element greater than or equal to A[n-1] is encountered and then insert A[n-1] right before that element.
Scan the sorted subarray from right to left untill the first element smaller than or equal to A[n-1] is encountered and then insert A[n-1] right after that element.
First and second methods are called straight insertion sort or simply insertion sort.
3. In third method use binary search to find an appropriate position for A[n-1] in the sorted portion of the array. This called binary insertion sort.

![Picture 3](Picture3.jpg)

![logo](Picture2.jpg)
Dr. Vijayalaxmi Mekali, Professor, Dept of CSE, KSIT
124
21-03-2026

### Notes:

<!-- Slide number: 125 -->
# MODULE 2 : Decrease and Conquer
Insertion sort: It can be implemented with bottom up approach i.e iteratively.
Starting with A[1] and ending with A[n-1], A[i] is inserted in its  appropriate place among the first I elements of the array that have been already sorted
A[0] ≤ … … A[j]<A[j+1]≤….. ≤A[i-1]  A[i]…..A[n-1]
Smaller than                  greater than A[i]
or equal to A[i]

![Picture 3](Picture3.jpg)

![logo](Picture2.jpg)
Dr. Vijayalaxmi Mekali, Professor, Dept of CSE, KSIT
125
21-03-2026

### Notes:

<!-- Slide number: 126 -->
# MODULE 2 : Decrease and Conquer
Insertion sort: It can be implemented with bottom up approach i.e iteratively.
Starting with A[1] and ending with A[n-1], A[i] is inserted in its  appropriate place among the first I elements of the array that have been already sorted
A[0] ≤ … … A[j]<A[j+1]≤….. ≤A[i-1]  A[i]…..A[n-1]
Smaller than                  greater than A[i]
or equal to A[i]

![Picture 3](Picture3.jpg)

![logo](Picture2.jpg)
Dr. Vijayalaxmi Mekali, Professor, Dept of CSE, KSIT
126
21-03-2026

### Notes:

<!-- Slide number: 127 -->
# MODULE 2 : Decrease and Conquer
Insertion sort example
To perform the insertion sort
Assume that first element A[0] is sorted, check weather the second element is in its proper place by comparing with sorted subarray element from left to right. And insert second element in its proper place.
Apply the same procedure for remaining elements of the unsorted list.
Ex: Apply the insertion sort for the following list of elements
89    45     68    90     29     34     17

![Picture 3](Picture3.jpg)

![logo](Picture2.jpg)
Dr. Vijayalaxmi Mekali, Professor, Dept of CSE, KSIT
127
21-03-2026

### Notes:

<!-- Slide number: 128 -->
# MODULE 2 : Decrease and Conquer
Insertion sort example
Ex: Apply the insertion sort for the following list of elements
45     68    90     29     34     17
Sol:
Assume that first element is sorted
89     45     68    90     29     34     17   check 45 is its proper place, this is done by comparing 45 with 89, as 45<89 insert 45 before 89

45     89     68    90     29     34     17   check 68 is its proper place, this is done by comparing 68 with all the sorted subarray as 68<89 and
                                                                                     68>45 proper place to insert 68 is after 68
45     68     89     90     29     34     17
45     68     89    90     29     34     17
29     45     68    89     90     34     17
17     29     34    45     68     89    90

![Picture 3](Picture3.jpg)

![logo](Picture2.jpg)
Dr. Vijayalaxmi Mekali, Professor, Dept of CSE, KSIT
128
21-03-2026
Red color elements indicate sorted subarray

### Notes:

<!-- Slide number: 129 -->
# MODULE 2 : Decrease and Conquer
Insertion Algorithm
InsertionSort(A[0…..n-1])
//input an array A[0….n-1]
//Output sorted array A[0….n-1]
for i 1 to n-1 do
     vA[i]
     ji-1
     while  j ≥ 0 and A[j]>v do
              A[j+1]A[j]
              jj-1
     A[j+1]v

![Picture 3](Picture3.jpg)

![logo](Picture2.jpg)
Dr. Vijayalaxmi Mekali, Professor, Dept of CSE, KSIT
129
21-03-2026

### Notes:

<!-- Slide number: 130 -->
# MODULE 2 : DIVIDE AND CONQUER- Decrease and Conquer               						(Topological sorting)
Topological sorting
Directed Acyclic Graph (DAG) is a directed graph with no directed cycles. That is, it consists of vertices and edges with each edge directed from one vertex to another, such that following those directions will never form a closed loop.
Topological sorting is performed only on Directed Acyclic Graph (DAG)
Definition of Topological sorting
Given with a DAG listing the vertices in such an order that for every edge in the graph, the vertex where the edge starts is listed before the vertex where the edge ends.
OR
Topological sorting for Directed Acyclic Graph (DAG) is a linear ordering of vertices such that for every directed edge u v, vertex u comes before v in the ordering.
 There can be more than one topological sorting for a graph.

![Picture 3](Picture3.jpg)

![logo](Picture2.jpg)
Dr. Vijayalaxmi Mekali, Professor, Dept of CSE, KSIT
130
21-03-2026

### Notes:

<!-- Slide number: 131 -->
# MODULE 2 : DIVIDE AND CONQUER- Decrease and Conquer               						(Topological sorting)
Topological sorting of DAG is performed with two methods
Depth-First Search (DFS) traversal
Source removal method
Topological sorting with Depth-First Search (DFS) traversal
Steps to perform Topological sorting with Depth-First Search
Step 1: select any arbitrary vertex in a given graph
Step 2: When a vertex is visited first time, it is pushed on to the stack
Step 3: When vertex becomes dead end (not possible to proceed further from that vertex) it is removed from the stack
Step 4: Repeat the step 2 and 3 for all the vertices in the graph
Step 5: Reverse the order of deleted items to get the topological sequence

![Picture 3](Picture3.jpg)

![logo](Picture2.jpg)
Dr. Vijayalaxmi Mekali, Professor, Dept of CSE, KSIT
131
21-03-2026

### Notes:

<!-- Slide number: 132 -->
# MODULE 2 : DIVIDE AND CONQUER- Decrease and Conquer               						(Topological sorting)
Problem1: Apply Depth-First Search based algorithm to solve Topological sorting problem for the following graph.

Solution: Let us consider start with a vertex a
Consider the table like this

![Picture 3](Picture3.jpg)

![logo](Picture2.jpg)
Dr. Vijayalaxmi Mekali, Professor, Dept of CSE, KSIT
132

![Picture 5](Picture5.jpg)
21-03-2026

### Notes:

<!-- Slide number: 133 -->
# MODULE 2 : Decrease and Conquer   (Topological sorting)

![Picture 3](Picture3.jpg)

![logo](Picture2.jpg)
Dr. Vijayalaxmi Mekali, Professor, Dept of CSE, KSIT
133

| Stack | V=adj(S[top]) | Nodes Visited (S) | Pop (stack) |
| --- | --- | --- | --- |
|  |  |  |  |
|  |  |  |  |
|  |  |  |  |
|  |  |  |  |
|  |  |  |  |
---
---
a
(a is visited push a on stack)

a
  b
(b is adjacent to a)
a, b
(b is visited push b on stack)

![Picture 17](Picture17.jpg)
a,  b
 e
(e is adjacent to b)

a, b, e
(e is visited push e on stack)
a,  b, e
 No node is adjacent   to e

a,  b
 g
(g is adjacent to b)

a, b, e, g
(g is visited push g on stack)
a, b, e

e
21-03-2026

### Notes:

<!-- Slide number: 134 -->

![Picture 3](Picture3.jpg)

![logo](Picture2.jpg)
Dr. Vijayalaxmi Mekali, Professor, Dept of CSE, KSIT
134

| Stack | V=adj(S[top]) | Nodes Visited (S) | Pop (stack) |
| --- | --- | --- | --- |
|  |  |  |  |
|  |  |  |  |
|  |  |  |  |
|  |  |  |  |
|  |  |  |  |
---
a, b, g, f
a, b, e, g, f

![Picture 17](Picture17.jpg)
a,  b, g
a,  b
 No node is adjacent   to b

a
 c
(c is adjacent to a)

a, b, e, g, f, c
(c is visited push c on stack)
a,  b, g
 f
(f is adjacent to g)

a, b, e, g, f
(f is visited push f on stack)
 No node is adjacent   to g

b
f
 No node is adjacent   to f

g
a, b, e, g, f
a, b, e, g, f
MODULE 2 : Decrease and Conquer   (Topological sorting)
21-03-2026

### Notes:

<!-- Slide number: 135 -->

![Picture 3](Picture3.jpg)

![logo](Picture2.jpg)
Dr. Vijayalaxmi Mekali, Professor, Dept of CSE, KSIT
135

| Stack | V=adj(S[top]) | Nodes Visited (S) | Pop (stack) |
| --- | --- | --- | --- |
|  |  |  |  |
|  |  |  |  |
|  |  |  |  |
|  |  |  |  |
|  |  |  |  |
a
a, b, e, g, f, c

![Picture 17](Picture17.jpg)
d
 all nodes adjacent d are already visited
The poped order is:   e, f, g, b, c, a, d  (reverse of poped order is Topological sorting)
Resultant Topological sorting is : d, a, c, b, g, f, e

a, c
a, b, e, g, f, c
d
a
 No node is adjacent   to a

a, b, e, g, f, c, d
 No node is adjacent   to c

c
 now stack is empty, next consider any unvisited node which is not visited
MODULE 2 : Decrease and Conquer   (Topological sorting)
21-03-2026

### Notes:

<!-- Slide number: 136 -->
Problem2: Apply the DFS-based algorithm to solve the topological sorting problem for the following digraph:
June/July-2019 (17CS43)

Solution: Let us consider start with a vertex 1
Consider the table like this

![Picture 3](Picture3.jpg)

![logo](Picture2.jpg)
Dr. Vijayalaxmi Mekali, Professor, Dept of CSE, KSIT
136

![Picture 9](Picture9.jpg)
MODULE 2 : Decrease and Conquer   (Topological sorting)
21-03-2026

### Notes:

<!-- Slide number: 137 -->

![Picture 3](Picture3.jpg)

![logo](Picture2.jpg)
Dr. Vijayalaxmi Mekali, Professor, Dept of CSE, KSIT
137

| Stack | V=adj(S[top]) | Nodes Visited (S) | Pop (stack) |
| --- | --- | --- | --- |
|  |  |  |  |
|  |  |  |  |
| now stack is empty, next consider any unvisited node which is not visited, let us consider node 2 |  |  |  |
|  |  |  |  |
|  |  |  |  |
| now stack is empty, next consider any unvisited node which is not visited, let us consider node 3 |  |  |  |
|  |  |  |  |
---
---
1
(1 is visited push 1 on stack)
1
1
2
 No node is adjacent   to 2

![Picture 28](Picture28.jpg)
 No node is adjacent   to 1
1
2
1, 2
1, 2
1, 2, 3
MODULE 2 : Decrease and Conquer   (Topological sorting)
21-03-2026

### Notes:

<!-- Slide number: 138 -->
# MODULE 2 : Decrease and Conquer  (Topological sorting)

![Picture 3](Picture3.jpg)

![logo](Picture2.jpg)
Dr. Vijayalaxmi Mekali, Professor, Dept of CSE, KSIT
138

| Stack | V=adj(S[top]) | Nodes Visited (S) | Pop (stack) |
| --- | --- | --- | --- |
|  |  |  |  |
|  |  |  |  |
|  |  |  |  |
| The poped order is: 1, 2, 4, 3 (reverse of poped order is Topological sorting) Resultant Topological sorting is : 3, 4, 2, 1 |  |  |  |
---
3, 4
1, 2, 3, 4
3
3
 4
(4 is adjacent to 3)

1, 2, 3, 4
(4 is visited push 4 on stack)
 No node is adjacent   to 3

4
 No node is adjacent   to 4

3
1, 2, 3, 4

![Picture 36](Picture36.jpg)
21-03-2026

### Notes:

<!-- Slide number: 139 -->
Problem2: Apply the DFS-based algorithm to solve the topological sorting problem for the following digraph:
June/July-2019 (17CS43) (same problem with different vertex as starting vertex

Solution: Let us consider start with a vertex 3
Consider the table like this

![Picture 3](Picture3.jpg)

![logo](Picture2.jpg)
Dr. Vijayalaxmi Mekali, Professor, Dept of CSE, KSIT
139

![Picture 9](Picture9.jpg)
MODULE 2 : Decrease and Conquer   (Topological sorting)
21-03-2026

### Notes:

<!-- Slide number: 140 -->

![Picture 3](Picture3.jpg)

![logo](Picture2.jpg)
Dr. Vijayalaxmi Mekali, Professor, Dept of CSE, KSIT
140

| Stack | V=adj(S[top]) | Nodes Visited (S) | Pop (stack) |
| --- | --- | --- | --- |
|  |  |  |  |
|  |  |  |  |
|  |  |  |  |
|  |  |  |  |
|  |  |  |  |
---
---
3
(3 is visited push 3 on stack)

3
  1
(1 is adjacent to 3)
3, 1
( 1 is visited push 1 on stack)
3, 1
3, 1

3
 No node is adjacent   to 1

3, 4
 4
(4 is adjacent to 3)

3, 1, 4, 2
( 2 is visited push 2 on stack)

3, 1, 4
( 4 is visited push 4 on stack)

![Picture 28](Picture28.jpg)
1
 2
(2 is adjacent to 4)

MODULE 2 : Decrease and Conquer   (Topological sorting)
21-03-2026

### Notes:

<!-- Slide number: 141 -->
# MODULE 2 : Decrease and Conquer  (Topological sorting)

![Picture 3](Picture3.jpg)

![logo](Picture2.jpg)
Dr. Vijayalaxmi Mekali, Professor, Dept of CSE, KSIT
141

| Stack | V=adj(S[top]) | Nodes Visited (S) | Pop (stack) |
| --- | --- | --- | --- |
|  |  |  |  |
|  |  |  |  |
|  |  |  |  |
| The poped order is: 1, 2, 4, 3 (reverse of poped order is Topological sorting) Resultant Topological sorting is : 3, 4, 2, 1 |  |  |  |
---
3, 4
3, 1, 4, 2
3
3, 4, 2
3, 1, 4, 2
 No node is adjacent   to 3

4
 No node is adjacent   to 2

3
3, 1, 4, 2

![Picture 36](Picture36.jpg)
2
 No node is adjacent   to 4

21-03-2026

### Notes:

<!-- Slide number: 142 -->
Problem2: Apply the DFS-based algorithm to solve the topological sorting problem for the following digraph:

Solution: Let us consider start with a vertex e
Consider the table like this

![Picture 3](Picture3.jpg)

![logo](Picture2.jpg)
Dr. Vijayalaxmi Mekali, Professor, Dept of CSE, KSIT
142

![Picture 5](Picture5.jpg)
MODULE 2 : Decrease and Conquer   (Topological sorting)
21-03-2026

### Notes:

<!-- Slide number: 143 -->
# MODULE 2 : Decrease and Conquer   (Topological sorting)

![Picture 3](Picture3.jpg)

![logo](Picture2.jpg)
Dr. Vijayalaxmi Mekali, Professor, Dept of CSE, KSIT
143

| Stack | V=adj(S[top]) | Nodes Visited (S) | Pop (stack) |
| --- | --- | --- | --- |
|  |  |  |  |
|  |  |  |  |
|  |  |  |  |
|  |  |  |  |
| now stack is empty, next consider any unvisited node which is not visited, let us consider node a |  |  |  |
---
---
e
(e is visited push a on stack)

e
  f
(f is adjacent to e)
e, f
(f is visited push f on stack)
e, f
e, f
e
 No node is adjacent  to f
e, f

f

![Picture 28](Picture28.jpg)
 No node is adjacent  to e
e
21-03-2026

### Notes:

<!-- Slide number: 144 -->

![Picture 3](Picture3.jpg)

![logo](Picture2.jpg)
Dr. Vijayalaxmi Mekali, Professor, Dept of CSE, KSIT
144

| Stack | V=adj(S[top]) | Nodes Visited (S) | Pop (stack) |
| --- | --- | --- | --- |
|  |  |  |  |
|  |  |  |  |
|  |  |  |  |
|  |  |  |  |
|  |  |  |  |
---
---
e, f, a
(a is visited push a on stack)

a

(c is adjacent to a)
e, f, a, c
( c is visited push c on stack)
a, c
a, c, d
a, c
MODULE 2 : Decrease and Conquer   (Topological sorting)

![Picture 27](Picture27.jpg)

(d is adjacent to c)
e, f, a, c, d
( d is visited push d on stack)
 No node is adjacent  to d
e, f, a, c, d
 d
 No node is adjacent  to c
e, f, a, c, d
 c
21-03-2026

### Notes:

<!-- Slide number: 145 -->

![Picture 3](Picture3.jpg)

![logo](Picture2.jpg)
Dr. Vijayalaxmi Mekali, Professor, Dept of CSE, KSIT
145

| Stack | V=adj(S[top]) | Nodes Visited (S) | Pop (stack) |
| --- | --- | --- | --- |
|  |  |  |  |
| now stack is empty, next consider any unvisited node which is not visited, let us consider node b |  |  |  |
|  |  |  |  |
|  |  |  |  |
| The poped order is: f, e, d, c, a, b (reverse of poped order is Topological sorting) Resultant Topological sorting is : b, a, c, d, e, f |  |  |  |
a
---
b
MODULE 2 : Decrease and Conquer   (Topological sorting)

![Picture 27](Picture27.jpg)
e, f, a, c, d, b
( b is visited push b on stack)
 No node is adjacent  to b
e, f, a, c, d, b
 b
 No node is adjacent  to a
e, f, a, c, d
 a
---
21-03-2026

### Notes:

<!-- Slide number: 146 -->
Source removal method
In a given graph, for every vertex ingree and outdegree is defined
Indegree: No of incoming edges to the vertex is know as indegree
Outdegree: No of outgoing edges

![Picture 3](Picture3.jpg)

![logo](Picture2.jpg)
Dr. Vijayalaxmi Mekali, Professor, Dept of CSE, KSIT
146
MODULE 2 : Decrease and Conquer   (Topological sorting)
21-03-2026

![Picture 8](Picture8.jpg)

| Vertex | Indegree | Outdegree |
| --- | --- | --- |
| 1 | 0 | 1 |
| 2 | 0 | 1 |
| 3 | 2 | 2 |
| 4 | 1 | 1 |
| 5 | 2 | 0 |

### Notes:

<!-- Slide number: 147 -->
Source removal method
Source removal method is based on decrease and conquer technique.
In this method, a vertex who’s indegree is zero is selected  and deleted along with the its all out going edges.
If there are several vertices with indegree zero, arbitrarily a vertex is selected.
This procedure repeated unitill all vertices are deleted
The order in which the vertices are visited and deleted one by one is Topological sorting.

![Picture 3](Picture3.jpg)

![logo](Picture2.jpg)
Dr. Vijayalaxmi Mekali, Professor, Dept of CSE, KSIT
147
MODULE 2 : Decrease and Conquer   (Topological sorting)
21-03-2026

### Notes:

<!-- Slide number: 148 -->

Source removal method
Apply the Source removal method algorithm to solve the topological sorting problem for the following digraph

Solution:

![Picture 3](Picture3.jpg)

![logo](Picture2.jpg)
Dr. Vijayalaxmi Mekali, Professor, Dept of CSE, KSIT
148
MODULE 2 : Decrease and Conquer   (Topological sorting)

![Picture 1](Picture1.jpg)
21-03-2026

![Picture 2](Picture2.jpg)

![Picture 20](Picture20.jpg)

### Notes:

<!-- Slide number: 149 -->
Source removal method

Solution:

![Picture 3](Picture3.jpg)

![logo](Picture2.jpg)
Dr. Vijayalaxmi Mekali, Professor, Dept of CSE, KSIT
149
MODULE 2 : Decrease and Conquer   (Topological sorting)
Delete 1

![Picture 9](Picture9.jpg)

![Picture 13](Picture13.jpg)
Delete 2

![Picture 16](Picture16.jpg)
Identify vertices with indegree zero, they are 1 and 2, let select 1
Identify vertices with inderee zero, it is 2
Identify vertices with indegree zero, it is 3
21-03-2026

![Picture 2](Picture2.jpg)

![Picture 20](Picture20.jpg)

### Notes:

<!-- Slide number: 150 -->

Source removal method
Solution:

![Picture 3](Picture3.jpg)

![logo](Picture2.jpg)
Dr. Vijayalaxmi Mekali, Professor, Dept of CSE, KSIT
150
MODULE 2 : Decrease and Conquer   (Topological sorting)
Delete 3

![Picture 5](Picture5.jpg)
Delete 4

![Picture 12](Picture12.jpg)
Identify vertices with indegree zero, it is 4
Delete 5
Topological sorting is 1, 2, 3, 4, 5
Another solution is if first selected arbitrary vertex is 2
2, 1, 3, 4, 5
21-03-2026

### Notes:

<!-- Slide number: 151 -->

Source removal method
Step 1: Find the vertices  u with indegree zero and place them on stack.
Step 2: Pop the top most vertex from the stack.
Step 3: Find the vertex v which is adjacent to poped vertex,  decrement the indegree of v by 1,
Step 4. Repeat the steps 1 to 3

![Picture 3](Picture3.jpg)

![logo](Picture2.jpg)
Dr. Vijayalaxmi Mekali, Professor, Dept of CSE, KSIT
151
MODULE 2 : Decrease and Conquer   (Topological sorting)
21-03-2026

### Notes:

<!-- Slide number: 152 -->
Source removal method
Apply the Source removal method algorithm to solve the topological sorting problem for the following digraph

Solution:  Write a indegree of all nodes in  given graph

![Picture 3](Picture3.jpg)

![logo](Picture2.jpg)
Dr. Vijayalaxmi Mekali, Professor, Dept of CSE, KSIT
152
MODULE 2 : Decrease and Conquer   (Topological sorting)

![Picture 20](Picture20.jpg)
21-03-2026

| Node | indegree |
| --- | --- |
| a | 0 |
| b | 0 |
| c | 1 |
| d | 2 |
| e | 1 |
| f | 3 |

### Notes:

<!-- Slide number: 153 -->
# MODULE 2 : Decrease and Conquer   (Topological sorting)

![Picture 3](Picture3.jpg)

![logo](Picture2.jpg)
Dr. Vijayalaxmi Mekali, Professor, Dept of CSE, KSIT
153

![Picture 28](Picture28.jpg)
Select the node with indegree 0, let us consider a. Delete node a from the graph along with it delete its out going edges. By this indegree of c and d decreases by 1

21-03-2026

![Picture 2](Picture2.jpg)
Delete a

![Picture 3](Picture3.jpg)
Delete b

![Picture 4](Picture4.jpg)
Delete c

![Picture 5](Picture5.jpg)
Delete d

![Picture 6](Picture6.jpg)
Delete e
Delete f
Topological sorting is a,b,c,d,e,f
Another solution is if first selected arbitrary vertex is b
b,a,c,d,e,f

### Notes:

<!-- Slide number: 154 -->
Exhaustive Search is brute force algorithm design technique, it suggests generating each and every element of problem domain by selecting those of them that satisfy all the constraints and then finding  a desired element.
Knapsack problem

![Picture 3](Picture3.jpg)

![logo](Picture2.jpg)
Dr. Vijayalaxmi Mekali, Professor, Dept of CSE, KSIT
154
MODULE 2 : Brute force (Exhaustive Search)
21-03-2026

### Notes:

<!-- Slide number: 155 -->
# MODULE 2 : Brute force (Exhaustive Search)

![Picture 3](Picture3.jpg)

![logo](Picture2.jpg)
Dr. Vijayalaxmi Mekali, Professor, Dept of CSE, KSIT
21-03-2026
155

<!-- Slide number: 156 -->
# MODULE 2 : Brute force (Exhaustive Search)
Knapsack problem
The profit and weights are positive numbers
A feasible solution is any set  of (x1, x2, ……xn)  that satisfies Eq. 2 and Eq. 3
The optimal solution is a feasible solution for which Eq. 1 is maximized

![Picture 3](Picture3.jpg)

![logo](Picture2.jpg)
Dr. Vijayalaxmi Mekali, Professor, Dept of CSE, KSIT
21-03-2026
156

<!-- Slide number: 157 -->
# MODULE 2 : Brute force (Exhaustive Search)
Example 1: using Exhaustive Search Find the optimal solution to the knapsack instance
n=4, m=20n=3, m=10
Profits (p1, p2, p3) = (42, 12, 40, 25) and
Weights (w1, w2, w3 ) = (7, 3, 4, 5)

![Picture 3](Picture3.jpg)

![logo](Picture2.jpg)
Dr. Vijayalaxmi Mekali, Professor, Dept of CSE, KSIT

| Subset | Total weight | Total value |
| --- | --- | --- |
| Null set | 0 | 0 |
| {1} | 7 | 42 |
| {2} | 3 | 12 |
| {3} | 4 | 40 |
| {4} | 5 | 25 |
| {1, 2} | 10 | 52 |
| {1,3} | 11 | Not feasible |
| {1, 4} | 12 | Not feasible |
| {2,3} | 7 | 52 |
| {2, 4} | 8 | 37 |
| {3,4} | 9 | 65 |
21-03-2026
157

<!-- Slide number: 158 -->
# MODULE 2 : Brute force (Exhaustive Search)
Example 1: using Exhaustive Search Find the optimal solution to the knapsack instance
n=4, m=20n=3, m=10
Profits (p1, p2, p3) = (42, 12, 40, 25) and
Weights (w1, w2, w3 ) = (7, 3, 4, 5)

![Picture 3](Picture3.jpg)

![logo](Picture2.jpg)
Dr. Vijayalaxmi Mekali, Professor, Dept of CSE, KSIT

| Subset | Total weight | Total value |
| --- | --- | --- |
| Null set | 0 | 0 |
| {1} | 7 | 42 |
| {2} | 3 | 12 |
| {3} | 4 | 40 |
| 4} | 5 | 25 |
| {1, 2} | 10 | 52 |
| {1,3} | 11 | Not feasible |
| {1, 4} | 12 | Not feasible |
| {2,3} | 7 | 52 |
| {2, 4} | 8 | 37 |
| {3,4} | 9 | 65 |
21-03-2026
158

<!-- Slide number: 159 -->
# MODULE 2 : Brute force (Exhaustive Search)
Travelling salesmen problem (TSP)

![Picture 3](Picture3.jpg)

![logo](Picture2.jpg)
Dr. Vijayalaxmi Mekali, Professor, Dept of CSE, KSIT

![Picture 2](Picture2.jpg)
21-03-2026
159