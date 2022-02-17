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
