class MergeSort:
    def __init__(self):
        pass

    def merge(self, l ,r, m, arr):
        lenL = m - l + 1
        lenR = r - m
        L, R = [], []
        for i, p in enumerate(range(l, m + 1)):
            L.append(arr[p])

        for i, p in enumerate(range(m + 1, r + 1)):
            R.append(arr[p])

        i, j, k = 0, 0 ,l
        while (i < lenL and j < lenR):
            if (L[i] <= R[j]):
                arr[k] = L[i]
                i += 1
                k += 1
            else:
                arr[k] = R[j]
                j += 1
                k += 1

        while (i < lenL):
            arr[k] = L[i]
            i += 1
            k += 1

        while (j < lenR):
            arr[k] = R[j]
            j += 1
            k += 1


    def sort(self, l, r, arr):
        if (l < r):
            m = (l + r) // 2
            self.sort(l, m, arr)
            self.sort(m + 1, r, arr)
            self.merge(l, r, m, arr)
        print(arr)



if __name__ == '__main__':
    ms = MergeSort()
    print("Please type the length of your list:")
    len = input()
    print("Please type you list element: (separate it with blank!)")
    l = input().split()
    print("This is your list: ")
    print(l)
    print("Enter to start MergeSort")
    choice = input()
    if (choice == ""):
        ms.sort(0, int(len) - 1, l)
    else:
        print("Invaild input")

    
