class vigener:
    def __init__(self):
        self.alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"

    def crypt(self, data, key, target):
        if data.isspace() or len(data) == 0:
            raise ValueError(f"invalid data: \"{data}\": there is nothing to encrypt")
        
        if key.isalpha():
            if all(True if letter in self.alphabet else False for letter in key):
                '''
                Completing the password

                Сalculate the integer part of dividing 
                the length of the data string by the length of the code 
                and add the remainder of the division.

                Example:
                Data  : Hello, World!
                Pass  : test
                Result: testtesttestt
                '''
                result = ""
                new_key = key * (len(data) // len(key)) + key[:(len(data) % len(key))]
                
                for letter in range(len(data)):
                    place = self.alphabet.find(data[letter])
                    place_code = self.alphabet.find(new_key[letter])

                    new_place = (place + (int(place_code) if target == "En" else -1 * int(place_code))) % len(self.alphabet)
                    if data[letter] in self.alphabet:
                        result += self.alphabet[new_place]
                    else:
                        result += data[letter]
                
                return result
            else:
                raise ValueError(f"invalid key: \"{key}\": the key must contain only Cyrillic characters")
        else:
            raise ValueError(f"invalid key: \"{key}\": the key must be a word")