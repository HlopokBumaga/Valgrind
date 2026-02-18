class xor:
    def __init__(self):
        pass
    
    def crypt(self, data, key):
        if data.isspace() or len(data) == 0:
            raise ValueError(f"invalid data: \"{data}\": there is nothing to encrypt")

        if key.isdigit():
            if int(key) > 0:
                return "".join([chr(ord(symbol) ^ int(key)) for symbol in data])
            else:
                raise ValueError(f"invalid key: \"{key}\": the key must be a positive number")
        else:
            raise ValueError(f"invalid key: \"{key}\": the key must be a number")