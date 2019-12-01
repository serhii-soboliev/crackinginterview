class Hex:

    def to_hex_speak(self, num: str) -> str:
        int_num = int(num)
        hex_num = hex(int_num)[2:]
        return self.hex_speack(hex_num)

    def hex_speack(self, hex_num):
        res = []
        for s in hex_num:
            if s in ["a", "b", "c", "d", "e", "f"]:
                res.append(s.upper())
            elif s == "1":
                res.append("I")
            elif s == "0":
                res.append("O")
            else:
                return "ERROR"
        return "".join(res)



