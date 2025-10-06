lst = [1, 2, 3, 4, 5, 6]
reversed_every_second = lst[::2][::-1]
print(reversed_every_second)  # [5, 3, 1]

def sort_by_length(words):
    return sorted(words, key=len, reverse=False)

words_list = ["apple", "kiwi", "banana", "pear"]
sorted_words = sort_by_length(words_list)
print(sorted_words)  # ['kiwi', 'pear', 'apple', 'banana']

def swap_inner(lst):
    if len(lst) >= 4:
        lst[1], lst[-2] = lst[-2], lst[1]
    return lst

data = [100, 200, 300, 400, 500]
swapped_data = swap_inner(data)
print(swapped_data)  # [100, 400, 300, 200, 500]
