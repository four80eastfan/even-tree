# Enter your code here. Read input from STDIN. Print output to STDOUT
#gold = []
#found = False
cuts = 0

'''def fetch_subtree(tree, value):
    global gold
    global found
    
    if not found:
        if tree[0] == value:
            #return tree
            gold = tree
            found = True

        if not tree[1]:
            return None
        else:
            for i in tree[1]:
                fetch_subtree(i, value)'''
                
def add_child(tree, parent, value):
    if tree[0] == parent:
        tree[1].append([value, []])
    elif not tree[1]:
        return None
    else:
        for i in tree[1]: 
            add_child(i, parent, value)
            
def node_count(tree): # number of nodes in the tree
    count = 1
    if not tree[1]:
        return count
    else:
        # count = count + len(tree[1])
        for i in tree[1]:
            count = count + node_count(i)
        return count

def num_cuts(tree):
    global cuts
    #cuts = 0
    num_nodes = node_count(tree)
    # or len(tree[1]) == 1
    
    if (num_nodes - 1) == len(tree[1]): # all descendents are immediate children
        #return cuts
        cuts = cuts + 0
    elif num_nodes % 2 == 1: # odd number of nodes
        for i in tree[1]:
            #cuts = cuts + num_cuts(i)
            num_cuts(i)
        #return cuts        
    else: # even number of nodes
        cuts = cuts + 1
        for i in tree[1]:
            #cuts = cuts + num_cuts(i)
            num_cuts(i)
        #return cuts
        
#treezy = [1,[]]

#gold = fetch_subtree(treezy, 3)
#print gold
#add_child(treezy, 4, 5)
#print treezy
MN = raw_input()
M,N = MN.split()
tree = [1, []]

for i in range(int(M) - 1):
    #add child
    
    xy = raw_input()
    x,y = xy.split()
    x = int(x)
    y = int(y)
    
    # build tree
    add_child(tree, y, x)

'''for i in tree[1]:
    #for each child node of root
    num_cuts(i)'''
#print node_count(tree)
num_cuts(tree)
        
print cuts