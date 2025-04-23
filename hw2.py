
def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    mid = 0
    i = 0
    h = high

    while low <= high:
 
        i =+ 1
        mid = (high + low) // 2
        if arr[mid] < x:
            low = mid + 1
 
        elif arr[mid] > x:
            h = arr[mid]
            high = mid - 1
 
        else:
            return [i,arr[mid]]

    return [i,h]


if __name__ == "__main__":
    arr = [2.1, 3.5, 4.3, 9.8, 13.1, 33.2, 33.3, 33.4, 40.6]
    x = 33
    print(binary_search(arr, x))