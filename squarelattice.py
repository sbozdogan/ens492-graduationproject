differentprices=[0.0, 0.05, 0.1, 0.15, 0.2, 0.25, 0.3, 0.35, 0.4, 0.45, 0.5, 0.55, 0.6, 0.65, 0.7, 0.75, 0.8, 0.85, 0.9, 0.95, 1] #x axis of simulation: changes in prices
result = [] #array of n_of_adopters
for changeprice in differentprices:
    
#import essential libraries
        import networkx as nx
        import matplotlib.pyplot as plt
        import random
        from random import randint
        import numpy as np

        G=nx.Graph()
        j=0
        n=40 #example square lattice size: 4x4
        
        for i in range(n*n):
          while n*n>j:
            G.add_node(j,purchasingpower=random.random())
            j+=1

# edges for square lattice (2-dimensional, degree 8)
        for a in range(n*n-1):
         G.add_edge(a,a+1)
         if not a>=(n*(n-1)-1):
            G.add_edge(a,a+n)
            G.add_edge(a,a+n-1)
            G.add_edge(a,a+n+1)
         elif not a>= (n*(n-1)):
            G.add_edge(a,a+n)
            G.add_edge(a,a+n-1)

#give a uniformly distributed price for the product
            p=changeprice

        n_of_adopters=[0]
        purchasingpower= nx.get_node_attributes(G,'purchasingpower')

        allneighbors  = set()
        visited = set()

        purchasingpower[13]=0.9
        def purchase(i):
            visited.add(i)
            if purchasingpower[i] >= p :
                n_of_adopters[0]= n_of_adopters[0]+1
                for e in G.neighbors(i) :
                    if e not in visited :
                       allneighbors.add(e)


        purchase(13)
        while len(allneighbors) is not 0:

         purchase(allneighbors.pop())

        print(n_of_adopters[0])
        
        
        x = n_of_adopters[0]
        result.append(x)
        
print(result)
plt.plot(differentprices, result, 'd', color ='blue')
plt.xlabel('price')
plt.ylabel('n-of-adopters')
plt.show()
