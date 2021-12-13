scoresGym = (1,2,3,4,5,6,7,8,9,10)
print("The lowest possible score is %d, and the highest possible score is %d." % (min(scoresGym),max(scoresGym)))
for score in scoresGym :
    if score != 1 :
        print("A judge can give a gymnast %d points." % score)
    else :
        print("A judge can give a gymnast %d point." % score)