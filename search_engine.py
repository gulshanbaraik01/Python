'''
A program which allows fast full text search
Author: Gulshan Baraik
'''

import pickle as pc

file_path = "searchengine"

#Method to add statement with 2 parameters
def addText(id1, text):
    allid={}
    tokens={}
    data ={}
    try:
        with open(file_path, 'rb') as file:
            data = pc.load(file)
            tokens=data["tokens"]
            allid=data["allid"]
    except:
        allid={}
        tokens={}
        data ={}
    allid[id1]=text
    words = text.split()
    for w in words:
        if w in tokens:
            tokens[w].add(id1)
        else:
            tokens[w]=set()
            tokens[w].add(id1)

    data["tokens"]=tokens
    data["allid"]=allid
    with open(file_path, 'wb') as file:
        pc.dump(data, file)
    return data

#Method to search text
def searchText(text):
    allid={}
    tokens={}
    data ={}
    with open(file_path, 'rb') as file:
        data = pc.load(file)
        tokens=data["tokens"]
        allid=data["allid"]

    words = text.split()
    final = set()
    for id1 in allid.keys():
        final.add(id1)
    
    for w in words:
        if w in tokens:
            final = tokens[w].intersection(final)
        else:
            final = {"count":0}
            return final
    document = {}
    for id1 in final:
        document[id1]=allid[id1]
    ans = {"count": len(final), "document": document}
    return ans
