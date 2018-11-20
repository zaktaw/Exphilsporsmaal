import random

def make_db(filename, db_name):             #Oppretter en database fra valgt fil
    with open(filename, "r") as f:
        db_name = {}
        for line in f:
            if line[0].isdigit():
                data = line.strip()
                data = data.split(";")
                key = int(data[0])
                value = [data[1],data[2]]
                db_name[key] = value
        return db_name

sokr = make_db("sokrates og sofistene.txt", "sokrates og sofistene")
plat = make_db("platon.txt", "platon")

liste = [sokr,plat]

def questions(filosof):
    db = filosof.copy()
    user_input = -1
    choices = []
    for num in range(1,len(db)+1):
        choices.append(num)
    while user_input != 0 and db:
        choice = random.choice(choices)
        print(db[choice][0])
        input("Dit svar: ")
        print("Forslag til svar: ")
        print(db[choice][1])
        del db[choice]
        choices.remove(choice)

def menu():
    user_input = -1
    while user_input != 0:
        print("Velg en filosof\n")
        print("1: Sokrates og sofistene\n2: Platon")
        user_input = int(input("Hva vil du velge?"))
        questions(liste[user_input-1])

menu()


