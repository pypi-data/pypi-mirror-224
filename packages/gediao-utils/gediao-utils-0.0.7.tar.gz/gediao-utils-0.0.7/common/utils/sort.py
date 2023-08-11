
def quicksort(array, vs, big_to_small=1):
    if len(array) < 2:
        return array
    else:
        index = len(array) // 2
        # pivot = array[index]  # 在数列中，选择一个元素作为基准，或者叫比较值
        pivot_v = vs[index]
        equals = []
        # equals.append(pivot)
        # array.remove(pivot)  # 在原数组中把比较值移除
        less, greater = [], []  # 定义基准值左右两个列表
        less_vs, greater_vs = [], []
        for i in range(len(array)):
            iv = vs[i]
            if iv < pivot_v:  # 小于基准值的放一侧
                less.append(array[i])
                less_vs.append(iv)
            elif iv > pivot_v:
                greater.append(array[i])  # 大于基准值的放另一侧
                greater_vs.append(iv)
            else:
                equals.append(array[i])

        if big_to_small == 1:
            return quicksort(greater, greater_vs) + equals + quicksort(less, less_vs)
        else:
            return quicksort(less, less_vs) + equals + quicksort(greater, greater_vs)
