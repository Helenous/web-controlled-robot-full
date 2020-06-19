import pickle

# Create file
f = open("c:\\tmp\\results.txt", "ab")
pickle.dump([],f)
f.close()


# Read old top 5
f = open("c:\\tmp\\results.txt", "rb")
top5 = pickle.load(f)
f.close()

# Run a new game
top5.append(["Player2",64])

# Sort 
def sortScore(val): 
    return val[1]
top5.sort(key=sortScore, reverse=True)


# Write out new top 5
f = open("c:\\tmp\\results.txt", "wb")
pickle.dump(top5[:5],f)
f.close()



print(top5[:5])
