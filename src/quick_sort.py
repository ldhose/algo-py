def quick_sort(elems):
    if len(elems) < 2:
        return elems;
    else:
        pivot = elems[0]
        less = [elem for elem in elems[1:] if elem <= pivot]
        greater = [elem for elem in elems[1:] if elem > pivot]
        return quick_sort(less) + [pivot] + quick_sort(greater)