# intuition of this problem
# i will use a sliding window approach to find the minimum number.The idea is to find the best segments to patch
#  while minimizing the number of patches...i'll slide the window of size 3 to find the best solution to minimise this problem

# Pseudocode
# 1. initialize 3 variables...ie Two pointers, left and right, 
# patches to keep count of the patches fixed and N ro store the size of array
# Now update the right pointer in that when we move from left to right and we encounter a pothole,
# we update the patches by one then increment the right by 3 since we can fix three potholes

# Time and space complexity
# o(N)
# o(1)

def Solution(S):
    N = len(S)
    patches =0
    left,right =0, 0

    while right < N:
        if S[right] == 'X':
            patches +=1
            right +=3

        else:
            right +=1

            # check if window is greater than 3, if it greater than 3 do back to the starting point which is left and increament by 1

            if right -left > 3:
                left +=1

    return patches

print(Solution("X.XXXXX.X."))