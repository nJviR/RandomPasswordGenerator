from random import randint

class Generator:
    length: int = 0

    result: str = ""
    variabals: str = "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789"

    def __init__(self, lenght):
        self.length = lenght

    def createpass(self) -> str:
        res: str = self.result
        for i in range(0, self.length):
            rund_el = randint(0, len(self.variabals))
            res = res + self.variabals[rund_el]
        return res
