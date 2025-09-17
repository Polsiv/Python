from ucimlrepo import fetch_ucirepo 
  
# fetch dataset 
mushroom = fetch_ucirepo(id=73) 
  
# data (as pandas dataframes) 
X = mushroom.data.features 
y = mushroom.data.targets 
  
# # metadata 
# print(mushroom.metadata) 
  
# # variable information 
# print(mushroom.variables) 

# Imprimir la primera fila
print(mushroom.variables.head(1))

# # O una fila aleatoria
# print(mushroom.variables.sample(1))