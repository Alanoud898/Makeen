from collections import Counter

arr = [1, 8, 7, 4, 1, 2, 2, 2]

counter = Counter(arr)
most_common_element = counter.most_common(1)[0][0]

print("The most frequent item :", most_common_element)
