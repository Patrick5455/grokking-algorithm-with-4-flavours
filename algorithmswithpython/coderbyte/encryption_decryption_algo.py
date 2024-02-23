cipher_map = {
    'a': 'e',
    'o': 'u',
    'p': 'b',
    't': 'd',
    's': 'c',
    'j': 'g',
    'm': 'n'
}


def encrypt(word: str) -> str:
    print(f'to_encrypt={word}')
    word_List = list(word.lower())
    parsed_word_list = []
    prev_word = 0
    parsed_word_list.append(word_List[0])
    for char in word_List[1:]:
        if char == word_List[prev_word]:
            char = char.upper()
            parsed_word_list = parsed_word_list[:-1]
            parsed_word_list.append(char)
        else:
            parsed_word_list.append(char)
        prev_word += 1
    result = ''.join(char for char in helper_en_de_cryption(parsed_word_list))
    print(f'encrypted={result}')
    return result


def decrypt(word: str) -> str:
    print(f'to_decrypt={word}')
    word_List = list(word)
    parsed_word_list = []
    for char in word_List:
        if char.isupper():
            parsed_word_list.append(char.lower() * 2)
        else:
            parsed_word_list.append(char)
    result = ''.join(char for char in helper_en_de_cryption(parsed_word_list))
    print(f'decrypted={result}')
    return result


def helper_en_de_cryption(word: list[str]) -> list[str]:
    crypted = []
    for char in word:
        if char in cipher_map.keys():
            crypted.append(cipher_map[char])
        elif char in cipher_map.values():
            crypted.append(key_val_helper(cipher_map, char))
        else:
            crypted.append(char)
    return crypted


def key_val_helper(pair: dict, value: str):
    key = list(pair.keys())
    val = list(pair.values())
    key = key[val.index(value.lower())]
    return key


if __name__ == '__main__':
    encrypted = encrypt('Pool')
    decrypt(encrypted)
