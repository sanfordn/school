def complete_puzzle(In, row_idx, col_idx):
    for number in range(1, len(In + 1)):
        if is_valid(row_idx, col_idx, number):
            return 0
def is_valid():
    return True

print(complete_puzzle([1]))
