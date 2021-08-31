from random import randint


data = {}

class Database:

    def check(id:str) -> bool:
        return id not in data


    def stock(content:str) -> str:
        while True:
            id = "".join(str(randint(1,9)) for _ in range(10))
            if Database.check(id):
                break
        data[id] = content
        return id

    def get(id:str) -> bool:
        if id in data:
            return data[id]
        return False
