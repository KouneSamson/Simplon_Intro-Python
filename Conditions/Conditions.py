#%% True and False

print(1 == 1)
print(2 <= 3)
print(5 > 8)
print("pi" != 3.14)
print(8 >= 2**4)
print("b" < "a")
print(0 == '0')
print(-1 >= -2)
print(4 != 4)
print(0 <= 0)

#%% Three is a Crowd

def crowded(people) :
    if len(people) > 3 : print("the room is crowded")

people = ["victor","mélissa","polgara","luc"]
crowded(people)
people.pop()
del people[0]
crowded(people)

#%% Three is a Crowd - Part 2 ( the return )

def crowded2(people) :
    if len(people) > 3 : print("the room is crowded")
    else : print("oof, so few people in here")

people = ["victor","mélissa","polgara","luc"]
crowded2(people)
people.pop()
del people[0]
crowded2(people)

#%% Six is a Mob

def mobTest(people) :
    nbP = len(people)
    if nbP > 0 :
        if nbP > 5 : print("Watch out, there is a mob here")
        elif nbP <= 2 : print("oof, so few people in here")
        else : print("the room is crowded")
    else : print("is there anyone here ??")

people = ["victor","mélissa","polgara","luc","pascale","françois"]
mobTest(people)
people.pop()
del people[0]
mobTest(people)
del people[2]
people.pop()
mobTest(people)
people.clear()
mobTest(people)

#%% Challenge: Alien Points

aliens = ["red","red","red","red","red","red","green","green","green","blue"]
score = 0
for a in aliens :
    if a == "red" : score += 5
    elif a == "green" : score += 10
    elif a == "blue" : score += 20

print("Ce groupe d'aliens rapporte %d points" % score)
