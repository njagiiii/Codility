# intuition
# i will use backtracking to solve this problem by trying different possibilities
#Finding connstaraints for the missing number of dice(F)

# Pseudocode
#initiate a currrent_sum variable to find the sum of the known rolls
#min_sum and maxumum_sum which will be my choice of numbers ranging from 1 to 6
#Constraints(Decision restriction) to check if the mean is within the specified choice
#create an empty array to store the missing rolls

def solution(A, F, M):
    arr_len = len(A)
    sum_of_F_rolls = M * (arr_len + F) - sum(A)
    possible_division_by_F = (sum_of_F_rolls // F)
    if not (1 <= possible_division_by_F <= 6):
        return [0]
        
    result = [possible_division_by_F] * F
    check_reminder = sum_of_F_rolls % F
    
    for i in range(check_reminder):
        result[i] += 1
    
    return result

print(solution([3, 2, 4, 3], 2, 4))
print(solution([1, 5, 6], 4, 3))
print(solution([1, 2, 3, 4], 4, 6))
print(solution([6, 1], 1, 1))
print(solution([6], 10, 4))


        

