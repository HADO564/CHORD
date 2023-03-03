import math


class node:
    fingList = list()
    id = None

    def __init__(self, id):
        self.id = id
        pred = list()

    def appendTable(self, activenodes):
        filled= len(fingList)
        if filled < 5:
            finglist.append(activenodes[i])
        else:
            pass



class network:
    activeNodes = list()

    def updateActive(self, node):
        self.activeNodes.append(node)

    def displayNodes(self):
        print(self.activeNodes)

    def joinNet(self, node):
        pass

    def leaveNet(self, node):
        pass



class chord:
    pass  # For Communication Functions
