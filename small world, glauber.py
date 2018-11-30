# -*- coding: utf-8 -*-
"""
Created on Sun Oct 29 11:59:44 2017

@author: alihan
"""
problar=[0.0,0.0001,0.001,0.01,0.1,0.3,0.5,0.7,1.0]
for problarınici in problar:
    for e in range(100): #for running the code multiple times
        
        import networkx as nx
        import matplotlib.pyplot as plt
        import random
        from random import randint
        import numpy as np
        from collections import Counter
        import time
        G=nx.Graph()
        
        j=0
        n=40 ## network size nxn
        size=4 ## node size
        X=[] # set of X
        Y=[]# set of Y
        z=0.5
        calisma=1
    
    #assigning X's and Y's
        i=0
        while i in range(0,n*n):
            b=randint(0,1)
            if b==0 and i not in X:
                X.append(i)
                i+=1
            elif b==1 and i not in Y:
                Y.append(i)
                i+=1
    
    # Network (graph) properties
        for i in range(n):
            k=0 
            while k>-n:
                if j in X or Y:
                    G.add_node(j,pos=(i,k), pot=0, shape=1, fillcolor='w', utility=0)
                j+=1
                k-=1
        
        pos=nx.get_node_attributes(G,'pos')
        
    # edges for square lattice        
        for a in range(n*n-1):
            G.add_edge(a,a+1)
            if not a>=(n*(n-1)-1):
                G.add_edge(a,a+n)
                G.add_edge(a,a+n-1)         
                G.add_edge(a,a+n+1)
            elif not a>= (n*(n-1)):
                G.add_edge(a,a+n)
                G.add_edge(a,a+n-1)
        
        u=n-1
        for i in range(n-1):
            if not i>=(n-2):
                G.remove_edge(u,u+n+1)
            u+=n    
          
        u=0
        for i in range(n-2):
            G.remove_edge(u,u+n-1)
            u+=n    
            
        for i in range(0,n*n,n):
            G.add_edge(i,i+n-1)
        
        for i in range(n,n*(n-1),n):
            G.add_edge(i,i+n-1-n)
            G.add_edge(i,i+n-1+n)
            
        
        for i in range(0,n):
            G.add_edge(i,i+n*(n-1))
        
        for i in range(1,n-1):   ## periodic boundary 
            G.add_edge(i,i+n*(n-1)+1)
        
        for i in range(1,n):
            G.add_edge(i,i+n*(n-1)-1) 
        G.add_edge(0,n*(n-1))
        G.add_edge(0,n-1+n)
        G.add_edge(0,n*(n-1)+1)
        G.add_edge(0,n*n-1)
        G.add_edge(n-1,n*(n-1))
        G.add_edge(n-1,n-1+n)
        G.add_edge(n-1,n*n-1)
        
        
    #for w=2
        """
        ikincikomsu={}
        for a in range(n*n):
            ikincikomsu[a]=[]
            for i in G.neighbors(a):
                for j in G.neighbors(i):
                    if j not in ikincikomsu[a] and j!=a and j not in G.neighbors(a):
                        ikincikomsu[a].append(j)
        
    #for w=3            
               
        ucuncukomsu={}
        for a in range(n*n):
            ucuncukomsu[a]=[]
            for i in G.neighbors(a):
                for j in G.neighbors(i):
                    for k in G.neighbors(j):
                        if k not in ucuncukomsu[a] and k!=a:
                            ucuncukomsu[a].append(k)
                        
        
        a=0
        while a<n*n:                
            for k in ucuncukomsu[a]:
                G.add_edge(a,k)
            a+=1              
                   
               
        
        for i in G.nodes():
            for j in ikincikomsu[i]:
                G.add_edge(i,j)
        """        
                
        for i in X:
            G.node[i]['fillcolor']='red' 
                
        for i in Y:
            G.node[i]['fillcolor']='green'
        
        reprob=problarınici
        randnum=0.0
        H=G.copy()
        for i in G.nodes():
            for j in H.neighbors(i):
                if G.has_edge(i,j) == True:    
                        randnum=random.random()
                        if randnum < reprob:
                            G.remove_edge(i,j)
                            k=randint(0,n*n-1)
                            if k!=i and k not in G.neighbors(i):
                                G.add_edge(i,k)
                            else:
                                while k==i or k in G.neighbors(i):
                                       k=randint(0,n*n-1)
                                G.add_edge(i,k)
                    
        def firststep():
            tx=[]
            ty=[]
            tx.extend(X)
            ty.extend(Y)
            global moved
            global unhappy1
            moved=[]
            unhappy1=[]
            for i in range(len(tx)+len(ty)):
                    u = [len(tx), len(ty)]
                    a=randint(0,1)
                    while u[a]==0:
                            a=randint(0,1)   
                    if a==0:
                        if len(tx)>0:
                            i=random.choice(tx)
                            xcount=0
                            ycount=0
                            for j in G.neighbors(i):
                                if G.node[j]['fillcolor']=='red':
                                    xcount +=1
                                elif G.node[j]['fillcolor'] =='green':
                                    ycount +=1
                            if ycount>xcount:
                                moved.append(i)
                                unhappy1.append(i)
                            tx.remove(i)    
                    elif a==1:
                        if len(ty)>0:
                            i=random.choice(ty)
                            xcount=0
                            ycount=0
                            for j in G.neighbors(i):
                                if G.node[j]['fillcolor']=='red':
                                    xcount +=1
                                elif G.node[j]['fillcolor'] =='green':
                                    ycount +=1
                            if xcount>ycount:
                                moved.append(i)
                                unhappy1.append(i)
                            ty.remove(i)
        firststep()     
                              
                        
    #changing agent type by using Glauber dynamics              
        def secondstep():
            global moved
            while len(moved)>0:
                i=random.choice(moved)
                if G.node[i]['fillcolor']=='red':
                    xcount=0
                    ycount=0
                    for j in G.neighbors(i):
                        if G.node[j]['fillcolor']=='red':
                            xcount+=1
                        elif G.node[j]['fillcolor']=='green':
                            ycount+=1
                    if ycount>xcount:
                        X.remove(i)
                        Y.append(i)
                        G.node[i]['fillcolor']='green'
                        moved.remove(i)
                    else:
                        moved.remove(i)
                elif G.node[i]['fillcolor']=='green':
                    xcount=0
                    ycount=0
                    for j in G.neighbors(i):
                        if G.node[j]['fillcolor']=='red':
                            xcount+=1
                        elif G.node[j]['fillcolor']=='green':
                            ycount+=1        
                    if xcount>ycount:
                        Y.remove(i)
                        X.append(i)
                        G.node[i]['fillcolor']='red'
                        moved.remove(i)
                    else:    
                        moved.remove(i)
                        
        secondstep()
        t=0
        while len(unhappy1)>0:
            firststep()
            secondstep()
            t+=1
            print('time: ', t)
            
        with open('finalX.txt', 'a') as the_file:
                string="" 
                string+=str(len(X))
                string+="\n"
                the_file.write(string)            
        with open('finalY.txt', 'a') as the_file:
                string="" 
                string+=str(len(Y))
                string+="\n"
                the_file.write(string) 
        nx.draw_networkx_nodes(G,pos,nodelist=X,node_shape='o',node_size=size)
        nx.draw_networkx_nodes(G,pos,nodelist=X,with_labels=True,  node_color='red',node_size=size)
        nx.draw_networkx_nodes(G,pos,nodelist=Y, node_color='green',node_size=size)  
        plt.savefig('final.png')
    

        
    
    
            