lst = [1, 2, 3, 4, 5]
reversed_lst = lst[::-1]
print(reversed_lst) # [5, 4, 3, 2, 1]

def list_sort(lst):
return sorted(lst, key=abs, reverse=True)

numbers = [-10, 3, -5, 7, -1]
sorted_numbers = list_sort(numbers)
print(sorted_numbers) # [-10, 7, -5, 3, -1]

def change(lst):
if len(lst) >= 2:
lst[0], lst[-1] = lst[-1], lst[0]
return lst

my_list = [10, 20, 30, 40]
changed_list = change(my_list)
print(changed_list) # [40, 20, 30, 10]
