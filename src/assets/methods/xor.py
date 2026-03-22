import flet as ft


class xor:
    def __init__(self):
        pass
    
    def crypt(self, data, key, local, details=False):
        if data.isspace() or len(data) == 0:
            raise ValueError(f"invalid data: \"{data}\": there is no target")

        if key.isdigit():
            if int(key) > 0:
                if details:
                    detail_result = [
                        [ft.Text(local["xor_details"][i], weight=ft.FontWeight.BOLD)] 
                        for i in range(0, 7)                 
                    ]

                    for symbol in data:
                        detail_result[0].append(ft.Text(symbol, weight=ft.FontWeight.BOLD))
                        detail_result[1].append(ft.Text(ord(symbol)))
                        detail_result[2].append(ft.Text(bin(ord(symbol))[2:]))
                        detail_result[3].append(ft.Text(bin(int(key))[2:]))
                        detail_result[4].append(ft.Text(bin(int(key) ^ ord(symbol))[2:]))
                        detail_result[5].append(ft.Text(int(key) ^ ord(symbol)))
                        detail_result[6].append(ft.Text(chr(int(key) ^ ord(symbol)), weight=ft.FontWeight.BOLD))

                    return detail_result

                return "".join([chr(ord(symbol) ^ int(key)) for symbol in data])
            else:
                raise ValueError(f"invalid key: \"{key}\": the key must be a positive number")
        else:
            raise ValueError(f"invalid key: \"{key}\": the key must be a number")