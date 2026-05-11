from node import Node
import time

def count_all(node: Node, current_depth=0):
    if not node:
        return 0
    
    node.height = current_depth
    

    count_all(node.left, current_depth + 1)
    count_all(node.right, current_depth + 1)
    
    return 1 

def get_all_heights(node, sp):
    
    if not node:
        return
    else:
        sp.append(node.height) 
        get_all_heights(node.left, sp)
        get_all_heights(node.right, sp)
    
def get_statistics(mas, l):
    start = time.time()
    for num in mas:
        l.insert(num)
    end = time.time()

    count_all(l.root)

    all_height = []
    get_all_heights(l.root, all_height)

    if not all_height:  
        return (0, 0, end - start)
    
    average = sum(all_height) / len(all_height)
    mx = max(all_height)

    return (average, mx, end - start)