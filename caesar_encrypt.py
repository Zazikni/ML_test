from string import ascii_lowercase


def encrypt(message: str, shift: int, alphabet: str) -> str:
    """
    A function that implements the Caesar encryption algorithm.

    :param message: String witch should be encoded
    :param shift: Alphabetical shift
    :param alphabet: Alphabet for encryption
    :return: Encrypted string
    """
    if any(sym not in alphabet for sym in message):
        raise ValueError('some characters in the message are not in the alphabet')

    result_string = ''
    if shift == 0:
        return message
    # Блок кода снизу решает основную на мй взгляд проблему алгоритма - выход за пределы алфавита,
    # тк алгоритм основан на индексах
    elif shift > 0:
        alph_len = len(alphabet)

        for sym in message:
            new_index = (alphabet.index(sym) + shift) % alph_len # поскольку смещение положительное новый индекс не выйдет за пределы списка справа, новый индекс находится путем нахождения остатка от деления суммы предыдущего индекса элемента и смещения на мощность алфавита
            result_string += alphabet[new_index]

    elif shift < 0:
        alph_len = -len(alphabet)
        shift = shift % alph_len  # смещение >= мощности алфавит бессмысленно (тк циклично) поэтому нахожу реальное смещение
        for sym in message:
            new_index = alphabet.index(sym) + shift  # поскольку смещение отрцательное новый индекс не может выйти за пределы справа, пользуемся обратной индексацией
            result_string += alphabet[new_index]

    return result_string


def main():
    while True:
        try:
            encrypt_shift = int(input('Введите сдвиг (целое число): '))
            break
        except ValueError as ex:
            print('Сдвиг должен быть целым числом, попробуйте еще раз.', end='\n' * 2)

    string_to_encrypt = input('Введите текст: ')
    encoded_str = encrypt(string_to_encrypt, encrypt_shift, ' ' + ascii_lowercase)
    print(encoded_str, end='\n' * 2)


if __name__ == '__main__':
    while True:
        main()
