
differentprices = [0.0, 0.05, 0.1, 0.15, 0.2, 0.25, 0.3, 0.35, 0.4, 0.45, 0.5, 0.55, 0.6, 0.65, 0.7, 0.75, 0.8, 0.85, 0.9, 0.95,
           1]  # x axis of simulation: changes in prices
result = []  # initial condition of results list
for i in differentprices:
 result.append(0)
for e in range(100):

  for e in range(len(differentprices)):
    # import essential libraries
     import networkx as nx
     import matplotlib.pyplot as plt
     import random
     from random import randint

     G = nx.Graph()   #empty graph created
     j = 0            #number of a particular node
     n = 40          # example square lattice size: 40x40

     for i in range(n * n):        #nodes of the network created
        while n * n > j:
            G.add_node(j, purchasingpower=random.random())   #add every node an attribute which indicates node's purchasing power (a uniformly distributed random number between 0 and one
            j += 1

    # edges between neighbors created for square lattice network(2-dimensional, degree 8)
     for a in range(n * n - 1):
        G.add_edge(a, a + 1)
        if not a >= (n * (n - 1) - 1):
            G.add_edge(a, a + n)
            G.add_edge(a, a + n - 1)
            G.add_edge(a, a + n + 1)
        elif not a >= (n * (n - 1)):
            G.add_edge(a, a + n)
            G.add_edge(a, a + n - 1)

     #price changes to see the change in the number of adapters with different prices

     price = differentprices[e]
     
     #change the square lattice into small world network by randomly rewiring
     reprob = 0.1  #rewiring probability is 0.1
     randnum=0.0   #defining the requirement for rewiring 
     H=G.copy()    #to rewire, generate a seperate link of all the neighbors and nodes
     for i in G.nodes():
         for j in H.neighbors(i):  
             if G.has_edge(i,j) == True:    #go through the list one by one, for every neighbor in every node
                 randnum=random.random()    #to randomly rewire
                 if randnum < reprob:       #choose to rewire if the random requirement(randnum) is less than rewiring probability
                                            #rewiring:
                     G.remove_edge(i,j)     #remove the edge from graph
                     k=randint(0,n*n-1)     #k is a randomly chosen node
                     if k!=i and k not in G.neighbors(i):    #avoid self-linking
                         G.add_edge(i,k)    #create new edge where the end point is the randomly chosen node k
                     else:
                         while k==i or k in G.neighbors(i):  #when there is self linking
                             k=randint(0,n*n-1)              #choose a new randomly chosen node k
                         G.add_edge(i,k)    #create new edge where the end point is the randomly chosen node k
                    
     
     n_of_adopters = [0] #number of adapters is an array with one element that is 0
     purchasingpower = nx.get_node_attributes(G, 'purchasingpower') #get every nodes purchasing power

     allneighbors = set()   # create a set of allneigbors
     visited = set()        # create a set of visited

     purchasingpower[13] = 0.95     #the initially informed node


     def purchase(i):             #definition of purchase function
        visited.add(i)
        if purchasingpower[i] >= price:     #if purchasing power of indicated node is bigger than the price
            n_of_adopters[0] = n_of_adopters[0] + 1  # node adapts, increment the first element of number of adapters
            for e in G.neighbors(i):         #for all the the neighbors of node i
                if e not in visited:
                    allneighbors.add(e)   #add e to allneighbors set


     purchase(13)              #purchase node 13 which is the initially informed node (the seed)
     while len(allneighbors) is not 0:
        purchase(allneighbors.pop()) #pop() function returns the last element from the allneighbor set and remove it afterwards. So this process will countinue until the set is empty.

        #to show the results

     x = float((n_of_adopters[0]))/float(n*n)  #the ratio of number of adapters to whole population

     result[e]= result[e]+x  # add every x (defined ratio) to result list

  
trials=100



finalresult= [x / trials for x in result]
print(finalresult)
plt.plot(differentprices, finalresult, 'd', color='blue') #to create the plot of price vs n of adopters
plt.xlabel('price')
plt.ylabel('n-of-adopters/population')
plt.show()
