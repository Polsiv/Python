class Node(object):
    info, sig = None, None
    
aux = Node()

aux.info = "First node"
word = input("Enter any word: ")

naux = aux

print(naux.info) # should print "First node"

while(word != ""):
    node = Node()
    node.info = word
    naux.sig = node
    naux = node

    word = input("Enter any word")

while(aux is not None):
    print(aux.info)
    aux=aux.sig