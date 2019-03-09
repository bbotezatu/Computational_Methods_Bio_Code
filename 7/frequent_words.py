def pattern_to_number(pattern):
    vals = { 'A': 0, 'C': 1, 'G': 2,'T': 3 }
    if pattern == '':
        return 0
    letter = pattern[-1:]
    prefix = pattern[:-1]
    return 4 * pattern_to_number(prefix) + vals[letter]


def number_to_pattern(index, k):
    vals = { 0: 'A', 1: 'C', 2: 'G', 3:'T' }
    if k == 1:
        return vals[index]
    prefix_index = index // 4
    r = index % 4
    letter = vals[r]
    prefix_pattern = number_to_pattern(prefix_index, k - 1)
    return prefix_pattern + letter


def read_input(filename):
    f = open(filename, 'r')
    val = f.readline().rstrip('\n')
    ans = f.readline().rstrip('\n')
    return val, ans


def read_input2(filename):
    f = open(filename, 'r')
    val = int(f.readline().rstrip('\n'))
    k = int(f.readline().rstrip('\n'))
    ans = f.readline().rstrip('\n')
    return val, k, ans


def check_answers(val, ans):
    if val == ans:
        print('Correct')
    else:
        print('Wrong')
    print(val)


def run_pattern_to_number(file_name):
    pattern, ans = read_input(file_name)
    num = pattern_to_number(pattern)
    print('Test: ', end='')
    check_answers(num, int(ans))


def run_number_to_pattern(file_name):
    index, k, ans = read_input2(file_name)
    pattern = number_to_pattern(index, k)
    print('Test: ', end='')
    check_answers(pattern, ans)


if __name__ == '__main__':
    run_pattern_to_number('P2a_short.txt')
    print()
    run_pattern_to_number('P2a_long.txt')
    print()
    run_number_to_pattern('P2b_short.txt')
    print()
    run_number_to_pattern('P2b_long.txt')