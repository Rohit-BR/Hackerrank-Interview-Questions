def findMedian(arr):
    arr = sorted(arr)
    median = len(arr)//2
    return arr[median]

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    print(findMedian(arr))