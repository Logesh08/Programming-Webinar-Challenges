# Sort Every K Integers - Ascending

# The program must accept an integer array of size N and sort every K values in ascending order. If the array size N is not a multiple of K then for the last set sort the remaining elements. Finally, the program must print the modified array.

# Boundary Condition(s):
# 2 <= K <= N <= 100
# 1 <= Each integer value <= 1000

# Input Format:
# The first line contains N and K separated by a space.
# The second line contains N integers separated by a space.

# Output Format:
# The first line contains the modified N integers separated by a space.

# Example Input/Output 1:
# Input:
# 11 3
# 6 2 1 8 7 9 50 60 40 55 45

# Output:
# 1 2 6 7 8 9 40 50 60 45 55

# Example Input/Output 2:
# Input:
# 6 6
# 15 81 93 17 53 47

# Output:
# 15 17 47 53 81 93

# Example Input/Output 3:
# Input:
# 5 4
# 98 31 39 88 42

# Output:
# 31 39 88 98 42




n,k=map(int,input().split())
arr=list(map(int,input().split()))
for i in range(0,n,k):
    print(*sorted(arr[i:i+k]))
