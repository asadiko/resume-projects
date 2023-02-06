'''S = '####A#B#A#B#B'
T = 'A##B#B#A##B##'
class Solution:
    def isItPossible(sef, S, T, M, N):
        i = 0
        j = 0
        if M != N:
            return 0
        while i < M or j < N:
            while i < M and S[i] == "#":
                i += 1
            while j < N and T[j] == "#":
                j += 1
            if i >= M and j < N:
                return 0
            if i < M and j >= N:
                return 0
            if i >= M and j >= N:
                return 1
            if S[i] != T[j]:
                return 0
            else:
                if S[i] == "A" and i < j:
                    return 0
                elif S[i] == "B" and i > j:
                    return 0
            i += 1
            j += 1
        return 1
Solution()'''

# You dont need to read input or print anything. 
# Complete the function maxSumLCM() 
# which takes n as input parameter and returns the maximum sum of distinct numbers 
# such that the LCM of all these numbers is equal to n.
def maxSumLCM(n):
	# Initialize result
	max_sum = 0
	# Finding a divisor of n and adding
	# it to max_sum
	i = 1
	while (i * i <= n):
		if (n % i == 0):
			max_sum = max_sum + i
			if (n // i != i):
				max_sum = max_sum + (n // i)
		i = i + 1
	return max_sum
# Driver code
n = 8
print(maxSumLCM(n))

