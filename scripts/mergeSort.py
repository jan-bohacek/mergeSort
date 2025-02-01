from merge import merge

input = [5,4,9,6,2,3,9,3,7,16,1,1965,12,6,0,48]

def mergeSort(in_array, a=0, b=None):
    if not b:
        b = len(in_array)

    c = b // 2
    l,r = in_array[a:c], in_array[c:b]
    # print(l, r)
    if len(l) > 1:
        mergeSort(l, a, c)
    if len(r) > 1:
        mergeSort(r, a, b-c)
    # print(l,r)
    merge(in_array, l, r)

mergeSort(input)



# print(f"Original Array: {a}")
# merge(a, l, r)
# print(f"Sorted Array: {a}")