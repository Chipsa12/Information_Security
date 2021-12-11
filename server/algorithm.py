key = 9781089456781069708340269810706897116749046413504990993630599262706029164758074870909826067655683710252409777219301855391825159608287534608729311564047562949682246938933332675426449823882269730137894


class Crypt(object):
    def __init__(self, key, length):
        self._key = key
        self._length = length
        self._subkeys = [(key >> (1 * i)) & 0xA for i in range(self._length)]

    def encrypt(self, msg):
        enc = []
        for i in range(len(msg)):
            enc.append(bin(msg[i] ^ self._subkeys[i])[2:])
        return enc

    def decrypt(self, crypted_msg):
        dec = []
        for i in range(len(crypted_msg)):
            dec.append(chr(int(crypted_msg[i], 2) ^ self._subkeys[i]))
        return dec


def main(input_text, type_mode):
    if not input_text:
        return {"result": "Отсутствует текст"}
    if type_mode != '-s' and type_mode != '-d':
        return {"result": "Не указана опция для шифрования или расшифровки"}
    if type_mode == '-s':
        gost = Crypt(key, len(input_text))
        try:
            s = []
            for i in input_text:
                s.append(ord(i))
            return {"result": gost.encrypt(s)}
        except:
            return {"result": "Ошибка шифравания"}
    if type_mode == '-d':
        gost = Crypt(key, len(input_text))
        try:
            dec_text = input_text.split(' ')
            res = gost.decrypt(dec_text)
            return {"result": "".join(i for i in res)}
        except:
            return {"result": "Ошибка расшифрования"}


if __name__ == '__main__':
    main()
