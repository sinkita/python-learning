import time
def freq_number(arr):
    map = {}

    for i in range(len(arr)):
        time.sleep(1)
        print("------------------------------------")
        print("value -> ", arr[i])
        print("current map -> ", map)
        if arr[i] in map.keys():
            map[arr[i]] = map[arr[i]] + 1
            print("above -> ", map)
        else:
            map[arr[i]] = 1
            print("below -> ", map)
        print("------------------------------------")

    print(map)


arr = [1, 2, 1, 4, 2, 1, 4, 2]
freq_number(arr)