test_string = 'barry is the spy'
test_word = 'dog'
test_code = 'txm srom vkda gl lzlgzr qpdb? fepb ejac! ubr imn tapludwy mhfbz cza ruxzal wg zztcgcexxch!'
test_code_word = 'friends'
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
            'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
            'u', 'v', 'w', 'x', 'y', 'z']


def caesar_encode(string, offset):
    decoded_string = []
    for elem in string:
        if elem in alphabet:
            if alphabet.index(elem) - offset >= 0:
                decoded_string.append(alphabet[alphabet.index(elem) - offset])
            else:
                decoded_string.append(alphabet[alphabet.index(elem) + 26 - offset])
        else:
            decoded_string.append(elem)
    return ''.join(decoded_string)

def caesar_decode(string, offset):
    decoded_string = []
    for elem in string:
        if elem in alphabet:
            if alphabet.index(elem) + offset >= 26:
                decoded_string.append(alphabet[alphabet.index(elem) - 26 + offset])
            else:
                decoded_string.append(alphabet[alphabet.index(elem) + offset])

        else:
            decoded_string.append(elem)
    return ''.join(decoded_string)

def vigenere_encode(string, word):
    i = 0
    code_list = []
    for elem in string:
        if elem in alphabet:
            code_list.append(word[i % len(word)])
            i += 1
        else:
            code_list.append(' ')
    coded_string = ''.join(code_list)

    it = 0
    v_coded = []
    for letter in string:
        if letter in alphabet:
            if alphabet.index(letter) - alphabet.index(word[it % len(word)]) >= 0:
                v_coded.append(alphabet[alphabet.index(letter) - alphabet.index(word[it % len(word)])])
                it += 1
            else:
                v_coded.append(alphabet[alphabet.index(letter) - alphabet.index(word[it % len(word)]) + 26])
                it += 1
        else:
            v_coded.append(' ')
        v_coded_fin = ''.join(v_coded)
    print(v_coded_fin)
    return v_coded_fin


def vigenere_decode(string, word):
    i = 0
    code_list = []
    for elem in string:
        if elem in alphabet:
            code_list.append(word[i % len(word)])
            i += 1
        else:
            code_list.append(' ')
    coded_string = ''.join(code_list)

    it = 0
    v_coded = []
    for letter in string:
        if letter in alphabet:
            if alphabet.index(letter) + alphabet.index(word[it % len(word)]) >= 26:
                v_coded.append(alphabet[alphabet.index(letter) + alphabet.index(word[it % len(word)]) - 26])
                it += 1
            else:
                v_coded.append(alphabet[alphabet.index(letter) + alphabet.index(word[it % len(word)])])
                it += 1
        else:
            v_coded.append(' ')
        v_coded_fin = ''.join(v_coded)
    print(v_coded_fin)
    return v_coded_fin


print(len(test_word))
vigenere_encode(test_string, test_word)
vigenere_decode(test_code, test_code_word)

# TODO
# rewrite ifs using lambda
# lambda x: (alphabet.index(letter) - 3) if ((alphabet.index(letter) - 3) >= 0) else (alphabet.index(letter) - 3 + 26)













