from merge import merge

a = [5,4,9,6,2,3,9,3,7]

l = [4,5,6,9]
r = [2,3,3,7,9]

print(f"Original Array: {a}")
merge(a, l, r)
print(f"Sorted Array: {a}")