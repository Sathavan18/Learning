What is Big-O notation:
It is used to describe the time or space complexity of algorithms. It is a way to express an upper bound of an algorithms time or space complexity. We manily consdier the worst case scenario of the algorithm to find its time complxity.

Given two functions f(n) and g(n), we say that f(n) is O(g(n)) if there exist constants c > 0 and n0 >= 0 such that f(n) <= c*g(n) for all n >= n0.
In simpler terms, f(n) is O(g(n)) if f(n) grows no faster than c*g(n) for all n >= n0 where c and n0 are constants.

Important Properities:
1) Reflexitivity: For any function f(n), f(n) = O(f(n)).
For example: f(n) = n2, then f(n) = O(n2).
2) Transivity: If f(n) = O(g(n)) and g(n) = O(h(n)), then f(n) = O(h(n)).
For example: If f(n) = n^2, g(n) = n^3, and h(n) = n^4, then f(n) = O(g(n)) and g(n) = O(h(n)). Therefore, by transitivity, f(n) = O(h(n)).
3) Constant factor: For any constant c > 0 and functions f(n) and g(n), if f(n) = O(g(n)), then cf(n) = O(g(n)).
For example: f(n) = n, g(n) = n^2. Then f(n) = O(g(n)). Therefore, 2f(n) = O(g(n)).
4) Sum Rule: If f(n) = O(g(n)) and h(n) = O(k(n)), then f(n) + h(n) = O(max( g(n), k(n) )) When combining complexities, only the largest term dominates.
For example: f(n) = n^2, h(n) = n^3. Then , f(n) + h(n) = O(max(n^2 + n^3)) = O ( n^3)
5) Product Rule: If f(n) = O(g(n)) and h(n) = O(k(n)), then f(n) * h(n) = O(g(n) * k(n)).
For example: f(n) = n, g(n) = n^2, h(n) = n^3, k(n) = n^4. Then f(n) = O(g(n)) and h(n) = O(k(n)). Therefore, f(n) * h(n) = O(g(n) * k(n)) = O(n^6).
6) Composition Rule: If f(n) = O(g(n)), then f(h(n)) = O(g(h(n))).

Linear Time Complexity: Big O(n)
The running time of an algrotihm grows linearly with the size of the input.

Logarithmic Time Complexity: Big O(log n)
The running time of an algorithm is proportional to the logarithm of the input size.

Quadratic Time Complexity: Big O(n^2)
The running time of an algorithm is proportional to the square of the input size. 

Cubic Time Complexity: Big O(n^3)
The running time of an algorithm is proportional to the cube of the input size.

Polynomial Time Complexity: Big O(n^k)
k is a constant and represents the degree of the polynomial. The are generally considrered efficient. 

Exponential Time Complexity: Big O(2^n)
The running time of an algorithm doubles with each addition to the input data set.

Factorial Time Complexity: Big O(n!) 
The running time of an algorithm grows factorially with the size of the input.


Nested Loops are usually O(n^2) because for every i value, we loop thorugh every j value. Dictionary/Set lookups are usually O(1) because they use hash tables internally which allows constant time lookup.
