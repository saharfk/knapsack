# Knapsack problem

The knapsack problem is a problem in [combinatorial optimization](https://en.wikipedia.org/wiki/Combinatorial_optimization): Given a set of items, each with a weight and a value, determine the number of each item to include in a collection so that the total weight is less than or equal to a given limit and the total value is as large as possible. It derives its name from the problem faced by someone who is constrained by a fixed-size [knapsack](https://en.wikipedia.org/wiki/Knapsack) and must fill it with the most valuable items. The problem often arises in [resource allocation](https://en.wikipedia.org/wiki/Resource_allocation) where the decision makers have to choose from a set of non-divisible projects or tasks under a fixed budget or time constraint, respectively.

The knapsack problem has been studied for more than a century, with early works dating as far back as 1897.[1] The name "knapsack problem" dates back to the early works of the mathematician [Tobias Dantzig](https://en.wikipedia.org/wiki/Tobias_Dantzig) (1884–1956),[2] and refers to the commonplace problem of packing the most valuable or useful items without overloading the luggage.

------

# Definition
The most common problem being solved is the 0-1 knapsack problem, which restricts the number {\displaystyle x_{i}}x_{i} of copies of each kind of item to zero or one. Given a set of {\displaystyle n}n items numbered from 1 up to {\displaystyle n}n, each with a weight {\displaystyle w_{i}}w_{i} and a value {\displaystyle v_{i}}v_{i}, along with a maximum weight capacity {\displaystyle W}W,

maximize {\displaystyle \sum _{i=1}^{n}v_{i}x_{i}}\sum _{i=1}^{n}v_{i}x_{i}
subject to {\displaystyle \sum _{i=1}^{n}w_{i}x_{i}\leq W}\sum _{i=1}^{n}w_{i}x_{i}\leq W and {\displaystyle x_{i}\in \{0,1\}}x_{i}\in \{0,1\}.
Here {\displaystyle x_{i}}x_{i} represents the number of instances of item {\displaystyle i}i to include in the knapsack. Informally, the problem is to maximize the sum of the values of the items in the knapsack so that the sum of the weights is less than or equal to the knapsack's capacity.

The bounded knapsack problem (BKP) removes the restriction that there is only one of each item, but restricts the number {\displaystyle x_{i}}x_{i} of copies of each kind of item to a maximum non-negative integer value {\displaystyle c}c:

maximize {\displaystyle \sum _{i=1}^{n}v_{i}x_{i}}\sum _{i=1}^{n}v_{i}x_{i}
subject to {\displaystyle \sum _{i=1}^{n}w_{i}x_{i}\leq W}\sum _{i=1}^{n}w_{i}x_{i}\leq W and {\displaystyle x_{i}\in \{0,1,2,\dots ,c\}.}{\displaystyle x_{i}\in \{0,1,2,\dots ,c\}.}
The unbounded knapsack problem (UKP) places no upper bound on the number of copies of each kind of item and can be formulated as above except for that the only restriction on {\displaystyle x_{i}}x_{i} is that it is a non-negative integer.

maximize {\displaystyle \sum _{i=1}^{n}v_{i}x_{i}}\sum _{i=1}^{n}v_{i}x_{i}
subject to {\displaystyle \sum _{i=1}^{n}w_{i}x_{i}\leq W}\sum _{i=1}^{n}w_{i}x_{i}\leq W and {\displaystyle x_{i}\geq 0,\ x_{i}\in \mathbb {Z} .}{\displaystyle x_{i}\geq 0,\ x_{i}\in \mathbb {Z} .}
One example of the unbounded knapsack problem is given using the figure shown at the beginning of this article and the text "if any number of each box is available" in the caption of that figure.


---------


# Solving
Several algorithms are available to solve knapsack problems, based on the dynamic programming approach,[13] the branch and bound approach[14] or hybridizations of both approaches.[11][15][16][17]

Dynamic programming in-advance algorithm
The unbounded knapsack problem (UKP) places no restriction on the number of copies of each kind of item. Besides, here we assume that {\displaystyle x_{i}>0}x_i > 0

{\displaystyle m[w']=\max \left(\sum _{i=1}^{n}v_{i}x_{i}\right)}{\displaystyle m[w']=\max \left(\sum _{i=1}^{n}v_{i}x_{i}\right)}
subject to {\displaystyle \sum _{i=1}^{n}w_{i}x_{i}\leq w'}{\displaystyle \sum _{i=1}^{n}w_{i}x_{i}\leq w'} and {\displaystyle x_{i}>0}x_i > 0
Observe that {\displaystyle m[w]}m[w] has the following properties:

1. {\displaystyle m[0]=0\,\!}m[0]=0\,\! (the sum of zero items, i.e., the summation of the empty set).

2. {\displaystyle m[w]=\max(v_{1}+m[w-w_{1}],v_{2}+m[w-w_{2}],...,v_{i}+m[w-w_{i}])}{\displaystyle m[w]=\max(v_{1}+m[w-w_{1}],v_{2}+m[w-w_{2}],...,v_{i}+m[w-w_{i}])} , {\displaystyle w_{i}\leq w}{\displaystyle w_{i}\leq w}, where {\displaystyle v_{i}}v_{i} is the value of the {\displaystyle i}i-th kind of item.

The second property needs to be explained in detail. During the process of the running of this method, how do we get the weight {\displaystyle w}w? There are only {\displaystyle i}i ways and the previous weights are {\displaystyle w-w_{1},w-w_{2},...,w-w_{i}}{\displaystyle w-w_{1},w-w_{2},...,w-w_{i}} where there are total {\displaystyle i}i kinds of different item (by saying different, we mean that the weight and the value are not completely the same). If we know each value of these {\displaystyle i}i items and the related maximum value previously, we just compare them to each other and get the maximum value ultimately and we are done.

Here the maximum of the empty set is taken to be zero. Tabulating the results from {\displaystyle m[0]}m[0] up through {\displaystyle m[W]}m[W] gives the solution. Since the calculation of each {\displaystyle m[w]}m[w] involves examining at most {\displaystyle n}n items, and there are at most {\displaystyle W}W values of {\displaystyle m[w]}m[w] to calculate, the running time of the dynamic programming solution is {\displaystyle O(nW)}O(nW). Dividing {\displaystyle w_{1},\,w_{2},\,\ldots ,\,w_{n},\,W}w_{1},\,w_{2},\,\ldots ,\,w_{n},\,W by their greatest common divisor is a way to improve the running time.

Even if P≠NP, the {\displaystyle O(nW)}O(nW) complexity does not contradict the fact that the knapsack problem is NP-complete, since {\displaystyle W}W, unlike {\displaystyle n}n, is not polynomial in the length of the input to the problem. The length of the {\displaystyle W}W input to the problem is proportional to the number of bits in {\displaystyle W}W, {\displaystyle \log W}\log W, not to {\displaystyle W}W itself. However, since this runtime is pseudopolynomial, this makes the (decision version of the) knapsack problem a weakly NP-complete problem.

0-1 knapsack problem
A similar dynamic programming solution for the 0-1 knapsack problem also runs in pseudo-polynomial time. Assume {\displaystyle w_{1},\,w_{2},\,\ldots ,\,w_{n},\,W}w_{1},\,w_{2},\,\ldots ,\,w_{n},\,W are strictly positive integers. Define {\displaystyle m[i,w]}m[i,w] to be the maximum value that can be attained with weight less than or equal to {\displaystyle w}w using items up to {\displaystyle i}i (first {\displaystyle i}i items).

We can define {\displaystyle m[i,w]}m[i,w] recursively as follows: (Definition A)

{\displaystyle m[0,\,w]=0}m[0,\,w]=0
{\displaystyle m[i,\,w]=m[i-1,\,w]}m[i,\,w]=m[i-1,\,w] if {\displaystyle w_{i}>w\,\!}w_{i}>w\,\! (the new item is more than the current weight limit)
{\displaystyle m[i,\,w]=\max(m[i-1,\,w],\,m[i-1,w-w_{i}]+v_{i})}m[i,\,w]=\max(m[i-1,\,w],\,m[i-1,w-w_{i}]+v_{i}) if {\displaystyle w_{i}\leqslant w}w_{i}\leqslant w.
The solution can then be found by calculating {\displaystyle m[n,W]}m[n,W]. To do this efficiently, we can use a table to store previous computations.

https://en.wikipedia.org/wiki/Knapsack_problem
