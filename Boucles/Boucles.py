#%% Growing Strength

strength = 5
print("Your strength is at %d" % strength)
while strength < 10 :
    strength += 1
    print("Your strength is at %d" % strength)

print("You are now too strong for this place")

#%% Game Preferences

games = ["FFXIV","Monster Hunter","Bloodborne","The Legend of Zelda"]
print("I like to play : ")
for g in games :
    print("\t- %s" % g)

print("")
yourgame = input("Tell me a game that you like.\n")

games.append(yourgame)
print("")
print("We like to play : ")
for g in games :
    print("\t- %s" % g)

#%% Many Games
nbGameAdded = 0
games = ["FFXIV","Monster Hunter","Bloodborne","The Legend of Zelda"]
print("I like to play : ")
for g in games :
    print("\t- %s" % g)

wantTo = input("Would you like to add a game ? (y/n)\n")

while wantTo == 'y' :
    yourgame = input("Tell me a game that you like.\n")
    games.append(yourgame)
    nbGameAdded += 1
    wantTo = input("Would you like to add another game ? (y/n)\n")

print("")

if nbGameAdded > 0 :
    print("We like to play : ")
    for g in games :
        print("\t- %s" % g)
else : print("We do not like the same type of games")

#%% Marveling at Infinity

while True :
    print("Quel horreur !")

#%% Challenge Gaussian Addition

def gaussIsGood(numSet) :
    numSet.sort()
    nbNum = len(numSet)
    maxi = max(numSet)
    subSum = 0
    Sum = 0
    while len(numSet) > 0 :
        if len(numSet) == 1 :
            num = numSet.pop()
            Sum += num
            print("Adding %d to the final Sum" % num)
        else :
            f_num = numSet.pop(0)
            l_num = numSet.pop()
            partial = f_num + l_num
            subSum += 1
            Sum += partial
            print("Adding %d , the sum between %d and %d , to the final Sum" % (partial,f_num,l_num))
    
    print("There has been a total of %d sub sum done." % subSum)
    print("The result of these sums is : %d ." % Sum)
    gauss = (nbNum/2)*(maxi+1)
    print("The result of Gauss' multiplication is : %d ." % gauss)

gaussIsGood(list(range(1,19)))

