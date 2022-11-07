hashmap_key_value = {}
encoded_values = []
decoded_values = []
pinda = list()
cloebboe = lambda x:5*x

def encode_string(data: str, key: str = None) -> str:
    if ',' in data:
        data = data.split(',')
    else:
        data = [data]

    key = set_hashmap(key)

    for word in data:
        encodedData = ''
        for char in word:
            if char in key:
                encodedData += key[char]
            else:
                encodedData += char

        encoded_values.append(encodedData)

    return encodedData

def decode_string(data: str, key: str = None) -> str:
    if ',' in data:
        data = data.split(',')
    else:
        data = [data]

    key = set_hashmap(key)

    for word in data:
        decodedData = ''
        for char in word:
            if char in key.values():
                decodedData += [k for k, v in key.items() if v == char][0]
            else:
                decodedData += char

        decoded_values.append(decodedData)

    return decodedData


def encode_list(data: list, key: str = None) -> list:
    poeptle = []
    for item in data:
        poeptle.append(encode_string(item, key))

    return poeptle


def decode_list(data: list, key: str = None) -> list:
    poeptle = []
    for item in data:
        poeptle.append(decode_string(item, key))

    return poeptle


def validate_values(encoded: str, decoded: str, key: str = None) -> bool:
    decodedData = decode_string(encoded, key)

    if decodedData != decoded:
        return False

    return True


def set_hashmap(key: str) -> None:
    if len(key) % 2 == 0:
        dictKeys = []
        dictValues = []

        for i in range(len(key)):
            if i % 2 == 0:
                dictKeys.append(key[i])
            elif i % 2 == 1:
                dictValues.append(key[i])

        for i in range(len(dictKeys)):
            hashmap_key_value[dictKeys[i]] = dictValues[i]

        return hashmap_key_value

    return 'Invalid hashvalue input'

def main(hashmap_key):
    if len(hashmap_key) % 2 == 0:
        # hashmap_key = 'A%B&C(D)E*F+G-H/I0J<K=L1M!N9O?P>Q7R#S5T;U:V[W]X~Y$Z@'

        choices = [
            '[E] Encode value to hashed value',
            '[D] Decode hashed value to normal value',
            '[P] Print all encoded/decoded values',
            '[V] Validate 2 values against eachother',
            '[Q] Quit program'
        ]
        for choice in choices:
            print(choice)

        userChoice = input('').upper()

        if userChoice == 'E':
            string = input('Value to encode: ')

            print(encode_string(string, hashmap_key))
            main(hashmap_key)
        elif userChoice == 'D':
            string = input('Value to decode: ')

            print(decode_string(string, hashmap_key))
            main(hashmap_key)
        elif userChoice == 'P':
            for encodedValue in encoded_values:
                print(encodedValue)
            for decodedValue in decoded_values:
                print(decodedValue)
            return
        elif userChoice == 'V':
            encoded = input('Enter encoded: ')
            decoded = input('Enter decoded: ')
            print(validate_values(encoded, decoded, hashmap_key))
    else:
        print('Invalid hashvalue input')
        return

if __name__ == "__main__":
    # hashmap_key = input('')
    hashmap_key = 'A%B&C(D)E*F+G-H/I0J<K=L1M!N9O?P>Q7R#S5T;U:V[W]X~Y$Z@'
    main(hashmap_key)
