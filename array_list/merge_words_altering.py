"""ou are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. If a string is longer than the other, append the additional letters onto the end of the merged string.

Return the merged string.

 

Example 1:

Input: word1 = "abc", word2 = "pqr"
Output: "apbqcr"
Explanation: The merged string will be merged as so:
word1:  a   b   c
word2:    p   q   r
merged: a p b q c r
Example 2:

Input: word1 = "ab", word2 = "pqrs"
Output: "apbqrs"
Explanation: Notice that as word2 is longer, "rs" is appended to the end.
word1:  a   b 
word2:    p   q   r   s
merged: a p b q   r   s
Example 3:

Input: word1 = "abcd", word2 = "pq"
Output: "apbqcd"
Explanation: Notice that as word1 is longer, "cd" is appended to the end.
word1:  a   b   c   d
word2:    p   q 
merged: a p b q c   d
 

Constraints:

1 <= word1.length, word2.length <= 100
word1 and word2 consist of lowercase English letters."""

word1 = "abcd"
word2 = "efgklmnoprs"
# My variant


def altering_words(word1, word2):
    max_len = max(len(word1), len(word2))
    min_len = min(len(word1), len(word2))
    answer = ""

    if max_len == min_len:
        for i in range(min_len):
            answer += word1[i] + word2[i]
    else:
        if max_len == len(word1):
            for i in range(min_len):
                answer += word1[i] + word2[i]

            answer += word1[-(max_len - min_len) :]
        elif max_len == len(word2):
            for i in range(min_len):
                answer += word1[i] + word2[i]

            answer += word2[-(max_len - min_len) :]

    return answer


print("equall", altering_words("asdf", "zxcv"))
print("first", altering_words("asdfefg", "zxcv"))

# variant from tutorial


def merge_altirnately(word1, word2):
    A, B = len(word1), len(word2)
    a, b = 0, 0
    word = []
    switcher = 1
    while a < A and b < B:
        if switcher == 1:
            word.append(word1[a])
            a += 1
            switcher = 2
        else:
            word.append(word2[b])
            b += 1
            switcher = 1

    while a < A:
        word.append(word1[a])
        a += 1

    while b < B:
        word.append(word2[b])
        b += 1
    
    return ''.join(word)
    
