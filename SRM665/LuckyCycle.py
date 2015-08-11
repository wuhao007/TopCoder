class LuckyCycle:
    def getEdge(self, edge1, edge2, weight):
        n = len(weight) + 1
        graph = [[] for _ in range(n)]
        for i in range(n - 1):
            node1 = edge1[i] - 1
            node2 = edge2[i] - 1
            graph[node1] += [(node2, weight[i])]
            graph[node2] += [(node1, weight[i])]
        print graph
                
            

luckyCycle = LuckyCycle()
#luckyCycle.getEdge(tuple([1]), tuple([2]), tuple([4]))
luckyCycle.getEdge(tuple([1, 3, 2, 4]), tuple([2, 2, 4, 5]), tuple([4, 7, 4, 7]))

            
