from os import listdir, mkdir
from os.path import isdir
from random import randint


class Database:
    def makedb():
        if not isdir("db"):
            mkdir("db")

    def check(id:str) -> bool:
        return id + ".txt" not in listdir("db")


    def stock(data:str) -> str:
        while True:
            id = "".join(str(randint(0,9)) for _ in range(10))
            if Database.check(id):
                break
        with open("db/"+id+".txt", 'w') as f:
            f.write(data)
        return id

    def get(id:str) -> bool:
        with open("db/"+id+".txt", 'r') as f:
            return f.read()
