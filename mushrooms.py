import dci_closed as dci


minSupp = 300
dataBase = {}
maxItemId = dci.readDataFromFileToDataBase(dataBase, "mushroom.dat")
postSet = dci.createPostSet(dataBase, maxItemId, minSupp)
# print(postSet)
postSet = dci.sortPostSet(postSet, dataBase)

closedSet = []
closedSetTIds = []
preSet = []

# print(postSet)
# for i in postSet:
    # print(getSupport(i, dataBase))
f_out = open("python_mushroom_out","w")
dci.dci_closed(True, closedSet, closedSetTIds, postSet, preSet, minSupp, dataBase, f_out)
f_out.close()