class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None
        
    
class Huffman:
    def __init__(self, freq) -> None:
        self.freq = freq
        self.codes = {}
        self.root = None
        
    def tree(self):
        nodes = [Node(char, freq) for char, freq in self.freq.items()]
        
        
        while len(nodes) > 1:
            nodes.sort(key =  lambda x: x.freq)
            
            left = nodes.pop(0)
            right = nodes.pop(0)
            
            merged = Node(None, left.freq + right.freq)
            
            merged.left = left
            merged. right = right
            
            nodes.append(merged)
            
        self.root = nodes[0]
        
        
    def generate_codes(self, node = None, current_node = ""):
        if node is None:
            node = self.root
            
        if node.char is not None:
            self.codes[node.char] = current_node
            return
        
        self.generate_codes(node.left, current_node + "0")
        self.generate_codes(node.right, current_node + "1")
        
        
    def get_codes(self):
        if not self.codes:
            self.generate_codes()
        return self.codes
    
    
    
def main():
    
    freq = {
        'h': 20,
        'e': 20,
        'o': 20,
        'l': 40,
    }
    
    huffman = Huffman(freq)
    huffman.tree()
    codes = huffman.get_codes()
    
    for i, j in codes.items():
        print(f"{i}: {j}")
        
        
        
main()
    