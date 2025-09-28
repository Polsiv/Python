from ucimlrepo import fetch_ucirepo 
  
# fetch dataset 
mushroom = fetch_ucirepo(id=73) 
  
# data (as pandas dataframes) 
X = mushroom.data.features 
y = mushroom.data.targets 
  
print(X )
# # metadata 
# print(mushroom.metadata) 
  
# # variable information 
# print(mushroom.variables) 

# Imprimir la primera fila 
#print(mushroom.data.features)

# print(X.iloc[0])
# print(y.iloc[0])

# # O una fila aleatoria
# print(mushroom.variables.sample(1))