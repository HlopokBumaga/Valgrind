class caesar:
    def __init__(self):
        self.alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZабвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ0123456789!\"#$%&'()*+,-./0123456789:;<=>?@[\\]^_`{|}~ "
    
    def crypt(self, data, key, target):
        if data.isspace() or len(data) == 0:
            raise ValueError(f"invalid data: \"{data}\": there is nothing to encrypt")

        if all([True if number.isdigit() or number == "-" else False for number in key]):
            if int(key) != 0:
                result = ""

                for letter in data:
                    place = self.alphabet.find(letter)
                    new_place = (place + (int(key) if target == "En" else -1 * int(key))) % len(self.alphabet)
                    if letter in self.alphabet:
                        result += self.alphabet[new_place]
                    else:
                        result += letter
                
                return result
            else:
                raise ValueError(f"invalid key: \"{key}\": the key must not be zero")
        else:
            raise ValueError(f"invalid key: \"{key}\": the key must be a positive or negative number")