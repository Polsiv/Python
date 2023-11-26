from user import *
from sklearn.tree import DecisionTreeClassifier

m1 = Man("bob", 13, 213455)
m2 = Man("bor", 53, 213354455)
m3 = Man("jack", 21, 3095)
m4 = Man("bob", 15, 3408579)

man_instances = [m1, m2, m3, m4]

# Create a list of feature vectors (age in this case)
X = [[man.age] for man in man_instances]

# Create a list of target labels (name in this case)
y = [man.name for man in man_instances]

# Create a DecisionTreeClassifier
clf = DecisionTreeClassifier()

# Fit the classifier with the data
clf.fit(X, y)

# Prompt the user for input
user_age = int(input("Enter an age: "))
user_input = [[user_age]]

# Predict the name based on age
predicted_name = clf.predict(user_input)[0]

# Filter the data based on the predicted name
filtered_data = [man for man in man_instances if man.name == predicted_name]

print("Filtered data:")
for man in filtered_data:
    print(f"Name: {man.name}, Age: {man.age}, Code: {man.code}")