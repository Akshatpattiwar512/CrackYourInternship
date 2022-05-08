# Given an array of size n, generate and print all possible combinations of r elements in array. For example, if input array is {1, 2, 3, 4} and r is 2, 
# then output should be {1, 2}, {1, 3}, {1, 4}, {2, 3}, {2, 4} and {3, 4}.

def combinationUtil(arr, data, start,
                    end, index, r):
    if (index == r):
        for j in range(r):
            print(data[j], end = " ");
        print();
        return;
    i = start;
    while(i <= end and end - i + 1 >= r - index):
        data[index] = arr[i];
        combinationUtil(arr, data, i + 1,
                        end, index + 1, r);
        i += 1;

        # Driver Code
arr = [1, 2, 3, 4, 5];
r = 3;
n = len(arr);
printCombination(arr, n, r);
