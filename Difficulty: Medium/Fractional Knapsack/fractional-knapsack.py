#User function Template for python3

class Item:
    def __init__(self,val,w):
        self.value = val
        self.weight = w
        
class Solution:    
    #Function to get the maximum total value in the knapsack.
    def fractionalknapsack(self, w,arr,n):
        arr.sort(key=lambda x: x.value / x.weight, reverse=True)
        
        total_value = 0.0  # Total value in the knapsack
        remaining_capacity = w  # Remaining weight capacity of the knapsack
        
        for i in range(len(arr)):
            if arr[i].weight <= remaining_capacity:
                # If the current item can fully fit in the knapsack
                total_value += arr[i].value
                remaining_capacity -= arr[i].weight
            else:
                # If only a fraction of the current item can fit
                total_value += (remaining_capacity * (arr[i].value / arr[i].weight))
                break  # The knapsack is full, so we can stop here
            
        return total_value 
            
                
            
        # code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

#Contributed by : Nagendra Jha


class Item:

    def __init__(self, val, w):
        self.value = val
        self.weight = w


if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        n, w = map(int, input().strip().split())
        info = list(map(int, input().strip().split()))
        arr = [Item(0, 0) for i in range(n)]
        for i in range(n):
            arr[i].value = info[2 * i]
            arr[i].weight = info[2 * i + 1]

        ob = Solution()
        print("%.6f" % ob.fractionalknapsack(w, arr, n))

# } Driver Code Ends