my_list = []
print(f"{'Step':<30} {my_list}")

my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)
print(f"{'After appending 10,20,30,40':<30} {my_list}")

my_list.insert(1,15)
print(f"{'After inserting 15 at pos 2':<30} {my_list}")

my_list.extend([50,60,70])
print(f"{'After extending with [50,60,70]':<30} {my_list}")

my_list.pop()
print(f"{'After removing last element':<30} {my_list}")

my_list.sort()
print(f"{'After sorting ascending':<30} {my_list}")

index_of_30 = my_list.index(30)
print(f"{'Index of 30':<30} {index_of_30}")

