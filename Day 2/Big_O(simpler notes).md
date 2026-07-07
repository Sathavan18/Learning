What is Big-O?
Big-O measures how the running time or memory usage of an algorithm grows as the input size grows.

Time Complexity: How long an algorithm takes to run.
Example: 
for num in nums:
    print(num)
The loop visits every element once. If there are 10 elements, there are 10 iterations. 1000 -> 1000. Therefore, O(n)

Space Complexity: How much extra memroy an algorithm uses.
Example:
new_list = []
for num in nums:
    new_list.append(num)
If the original list has 100 items, the new list also has 100 items. Therefore, O(n).

Constant Time: O(1)
x = num[5]
Whether the list has 10 or 1000 items, you still access one element.

Linear Time: O(n)
for num in nums:
Every element is visited once. 

Quadratic Time: O(n^2)
for i in nums:
    for j in nums:
Every item is compared with every other item.

Logarithmic Time: O(log n)
The amount of work shrinks each step. 
Example: Binary Search
Each step cuts the search space in half.

O(n log n):
Slightly worse than linear. 

Rules For Working Out Time Complexity:
1) One loop -> O(n^2)
2) Nested loop -> Mulitply
3) Separate loops -> Add them (O(n) + O(n) = O(n) simplified)
4) Ignore Constants
5) Ignore smaller terms -> O(n^2+n) -> O(n^2)

Good Questions to consider:
1) How many times does the algorithm go through the data?
2) Are there nested loops?
3) Does it create another list, dictionary, or set?
4) Can I use a better data structure to reduce the work?

Practice Question:
1) 
for i in range(n):
    print(i)
Time complexity: O(n) - running through everything in n so as n increases in size, so does the growth in time.
Space complexity: O(1) - not creating anything

2) 
for i in range(n):
    for j in range(n):
        print(i, j)
Time complexity: O(n^2) - nested loop, for every i, you run thorugh every j.
Space complexity: O(1) - not creating anything

3) 
numbers = set(nums)
Time complexity - O(n) - have to run through whole list
Space complexity - O(n) - creating a new set

4) 
sorted(nums)
Time complexity: O(n log n) - have to go through entire list in worst case, compare and rearrange.
Space complexity: O(n) - creating a new list.

5) 
x = nums[7]
Time complexity - O(1) - doesn't matter size of nums, since accessing jsut the one constant element. 
Space complexity - O(1) - not creating anything new.