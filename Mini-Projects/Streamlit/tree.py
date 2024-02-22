import tree
import matplotlib.pyplot as plt    

root = tree.Node("Root")
child1 = tree.Node("Child 1")
child2 = tree.Node("Child 2")

root.add_child(child1)
root.add_child(child2)

plt.show(root)