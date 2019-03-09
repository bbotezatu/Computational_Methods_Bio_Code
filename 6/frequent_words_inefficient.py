from count_patterns import count


def frequent_words(text, k):
    freq_dict = {}
    for i in range(0, len(text) - k):
        pattern = text[i: i + k]
        if not pattern in freq_dict:
            n = count(text, pattern)
            freq_dict[pattern] = n

    counts = freq_dict.values()
    m = max(counts)
    words = []
    for w, c in freq_dict.items():
        if c == m:
            words.append(w)
    return words


def read_input(filename):
    f = open(filename, 'r')
    text = f.readline().rstrip('\n')
    k = int(f.readline().rstrip('\n'))
    ans = f.readline().rstrip('\n').split()
    return text, k, ans


def check_answers(words, ans):
    words.sort()
    ans.sort()
    if words == ans:
        print('Correct')
    else:
        print('Wrong')
    print(words)


def run_test(file_name):
    text, k, ans = read_input(file_name)
    words = frequent_words(text, k)
    print('Test: ', end='')
    check_answers(words, ans)


if __name__ == '__main__':
    run_test('P1_short.txt')
    print()
    run_test('P1_long.txt')