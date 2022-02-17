# Longest common subsequence O(2^n)
def len_lcs(seq1, seq2, idx1=0, idx2=0):
    if idx1 == len(seq1) or idx2 == len(seq2):
        return 0
    elif seq1[idx1] == seq2[idx2]:
        return 1 + len_lcs(seq1, seq2, idx1 + 1, idx2 + 1)
    else:
        option1 = len_lcs(seq1, seq2, idx1 + 1, idx2)
        option2 = len_lcs(seq1, seq2, idx1, idx2 + 1)
        return max(option1, option2)

# complexity now much better but eats up memory


def lcs_memo(seq1, seq2):
    memo = {}

    def recurse(idx1=0, idx2=0):
        key = (idx1, idx2)
        if key in memo:
            return memo[key]
        elif idx1 == len(seq1) or idx2 == len(seq2):
            memo[key] = 0
        elif seq1[idx1] == seq2[idx2]:
            memo[key] = 1 + recurse(idx1+1, idx2+1)
        else:
            memo[key] = max(recurse(idx1+1, idx2), recurse(idx1, idx2+1))
        return memo[key]
    return recurse(0, 0)


# Iterative uses less memory O(n^2)
def lcs_dp(seq1, seq2):
    n1, n2 = len(seq1), len(seq2)
    # Creates a matrix of n1,n2
    table = [[0 for x in range(n2 + 1)] for x in range(n1+1)]
    for i in range(n1):
        for j in range(n2):
            if seq1[i] == seq2[j]:
                table[i + 1, j+1] = 1 + table[i][j]
            else:
                table[i+1][j+1] = max(table[i][j+1], table[i+1][j])
    return table[-1][-1]


# Knapsack Problem O(2^n)
def max_profit_recur(weights, profits, capacity, idx=0):
    if idx == len(weights):
        return 0
    elif weights[idx] > capacity:
        return max_profit_recur(weights, profits, capacity, idx + 1)
    else:
        option1 = max_profit_recur(weights, profits, capacity, idx + 1)
        option2 = profits[idx] + \
            max_profit_recur(weights, profits, capacity-weights[idx], idx + 1)
    return max(option1, option2)


test0 = {
    'input': {
        'capacity': 165,
        'weights': [23, 31, 29, 44, 53, 38, 63, 85, 89, 82],
        'profits': [92, 57, 49, 68, 60, 43, 67, 84, 87, 72]
    },
    'output': 309
}


#x = max_profit_recur(**test0['input'])
# print(x)


# Dynamic Knapsack Problem O(N)
def max_profit_dp(weights, profits, capacity):
    n = len(weights)
    # Creates matrix with extra row and column for computation purposes, beware of off by one
    table = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]
    for i in range(n):
        for c in range(1, capacity+1):
            # It's plus one because of the additional row and column in creating the matrix
            if weights[i] > c:
                table[i+1][c] = table[i][c]
            else:
                table[i+1][c] = max(table[i][c], profits[i] +
                                    table[i][c-weights[i]])
    return table[-1][-1]


x = max_profit_dp(**test0['input'])
print(x)
