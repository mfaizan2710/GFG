#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3
#User function Template for python3

#Function to find a continuous sub-array which adds up to a given number.
class Solution:
    def subArraySum(self,arr, n, s): 
       #Write your code here
        current_sum = 0
        start = 0
        
        # Traverse the array
        for end in range(n):
            current_sum += arr[end]  # Add the current element to the current sum
            
            # If current_sum exceeds the target sum, shrink the window from the left
            while current_sum > s and start < end:
                current_sum -= arr[start]
                start += 1
            
            # If the current sum matches the target, return the 1-based indices
            if current_sum == s:
                return [start + 1, end + 1]  # +1 for 1-based indexing
            
        # If no subarray is found, return -1
        return [-1]

#{ 
 # Driver Code Starts.
#Initial Template for Python 3

import math

def main():
        T=int(input())
        while(T>0):
            
            NS=input().strip().split()
            N=int(NS[0])
            S=int(NS[1])
            
            A=list(map(int,input().split()))
            ob=Solution()
            ans=ob.subArraySum(A, N, S)
            
            for i in ans:
                print(i, end=" ")
                
            print()
            
            T-=1


if __name__ == "__main__":
    main()
# } Driver Code Ends