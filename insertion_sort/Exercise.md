### Exercise: Insertion Sort

Compute the running median of a sequence of numbers. That is, given a stream of numbers, print out the median of the list so far on each new element.

Recall that the median of an even-numbered list is the average of the two middle numbers in a *sorted list*.

For example, given the sequence `[2, 1, 5, 7, 2, 0, 5]`, your algorithm should print out:

```
2
1.5
2
3.5
2
2
2
```
More easy explanation:
Certainly! The task is to find and print the median each time a new number is added to a sequence. The median is the middle value of a list when it’s sorted. If the list has an odd number of elements, the median is the exact middle value. But if the list has an even number of elements, the median is the average of the two middle values.

Here's a step-by-step breakdown, using the sequence `[2, 1, 5, 7, 2, 0, 5]` for clarification:

**Step 1**: Begin with the first number: `[2]`. 
- The sorted list is `[2]`. 
- The median is just `2` since there's only one number.

**Step 2**: Add the next number to the sequence: `[2, 1]`.
- The sorted list becomes `[1, 2]`. 
- The median is the average of `1` and `2`, which is `1.5` (since it’s an even-numbered list).

**Step 3**: Add the next number to form `[2, 1, 5]`.
- After sorting, the list looks like `[1, 2, 5]`.
- The median is '2' because it's the middle value in the sorted list (odd-numbered list).

**Step 4**: Add the next number, changing the sequence to `[2, 1, 5, 7]`.
- The sorted list is `[1, 2, 5, 7]`. 
- The median now is `(2 + 5)/2 = 3.5` (because there are an even number of elements).

**Step 5**: Now add another number: `[2, 1, 5, 7, 2]`.
- Sorting gives us `[1, 2, 2, 5, 7]`. 
- The median is `2` (the middle of the sorted list, now an odd-numbered list).

**Step 6**: Add one more number: `[2, 1, 5, 7, 2, 0]`.
- The sorted list becomes `[0, 1, 2, 2, 5, 7]`.
- The median is `(2 + 2)/2 = 2` (average of the two middle numbers).

**Step 7**: Finally, add the last number to have `[2, 1, 5, 7, 2, 0, 5]`.
- Sorting, we get `[0, 1, 2, 2, 5, 5, 7]`. 
- The median returns to being `2`.

Each time you add a new element, sort the sequence and then find the middle value(s) to determine the median. Print this value before the next number is added.
This explanation breaks down how to calculate the running median after each addition to the series.

 [Solution](https://github.com/codebasics/data-structures-algorithms-python/blob/master/algorithms/4_InsertionSort/insertion_sort_exercise_solution.py)