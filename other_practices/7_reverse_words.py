message = ['c', 'a', 'k', 'e', ' ',
           'p', 'o', 'u', 'n', 'd', ' ',
           's', 't', 'e', 'a', 'l']


def reverse_chars(msg, l_idx, r_idx):
    while l_idx < r_idx:
        msg[l_idx], msg[r_idx] = msg[r_idx], msg[l_idx]
        l_idx += 1
        r_idx -= 1


def reverse_words(msg):
    reverse_chars(msg, 0, len(msg)-1)

    l_idx = 0
    for i in range(len(msg)+1):
        if i == len(msg) or msg[i] == ' ':
            reverse_chars(msg, l_idx, i-1)
            l_idx = i + 1


reverse_words(message)

# Prints: 'steal pound cake'
print(''.join(message))


# O(n) time and O(1) space!
