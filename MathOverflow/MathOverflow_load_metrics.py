import pickle
import pandas as pd

with open('MathOverflow/adamicAdar_MathOverflow.pkl', 'rb') as y:
    adamicAdarList = pickle.load(y)

with open('MathOverflow/commonNeighbors_MathOverflow.pkl', 'rb') as y:
    commonNeighborsList = pickle.load(y)

with open('MathOverflow/rootedPageRankList_MathOverflow.pkl', 'rb') as y:
    rootedPageRankList = pickle.load(y)

with open('MathOverflow/jaccard_MathOverflow.pkl', 'rb') as y:
    jaccardList = pickle.load(y)

with open('MathOverflow/resAllocation_MathOverflow.pkl', 'rb') as y:
    resAllocationList = pickle.load(y)

with open('MathOverflow/assocStrength_MathOverflow.pkl', 'rb') as y:
    assocStrengthList = pickle.load(y)
    
with open('MathOverflow/labels_MathOverflow.pkl', 'rb') as y:
    labels = pickle.load(y)    
    
labels2 = []
for el in labels:
    if el == 1:
        labels2.append("yes")
    else:
        labels2.append("no")
    
dataset = pd.DataFrame(
    {'Adamic Adar': adamicAdarList,
     'Common Neighbors': commonNeighborsList,
     'Rooted PageRank': rootedPageRankList,
     'Jaccard': jaccardList,
     'Resource Allocation': resAllocationList,
     'Association Strength': assocStrengthList,
     'Labels': labels2,
    })
