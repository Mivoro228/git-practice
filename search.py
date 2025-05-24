def binary_search(arr, target):
    if not arr:
    
        return 'Массив не содержит ни одного элемента'  # если массив пустой

    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        # сравниваем элемент в середине с целью
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return 'эллемент не найден'  # если элемент не найден
