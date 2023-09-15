
def find_lexicographically_smallest(S):
    N = len(S)
    current_position = 0
    
    while current_position < N - 2:
        if S[current_position] == '0' and S[current_position + 1] == '0' and S[current_position + 2] == '1':
            S = S[:current_position] + '100' + S[current_position + 3:]
            current_position += 2
        else:
            current_position += 1

    return S
for _ in range(int(input())):
    n=int(input())
    S =input()
    result = find_lexicographically_smallest(S)
    print(result)