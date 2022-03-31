from sys import maxsize
from attr import define

# function for sum maximum and minimum
def miniMaxSum(arr):
    # Write your code here
    try:
        total_sum = 0
        maximum = max(arr)
        minimum = min(arr)
        
        for i in arr:
            total_sum+= i    

        max_sum = total_sum-minimum
        min_sum = total_sum-maximum
        print(min_sum, max_sum)
    except:
        print("SOMETHING WENT WRONG, PLEASE CHECK THE SOURCE CODE...")
    

arr = [1,2,3,4,5]
miniMaxSum(arr)