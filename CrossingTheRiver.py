class MissCannProblem():
    def __init__(self,mLeft,cLeft,boat,mRight,cRight):
        self.mLeft = mLeft
        self.cLeft = cLeft
        self.boat = boat
        self.mRight = mRight
        self.cRight = cRight
##      self.endGoal = (0, 0, 0)
        self.root = None

    # The end goal is to have both missionaries and cannibals on the right side therefore, both miss/cann on left = 0
    def endGoal(self):
        if self.mLeft == 0 and self.cLeft == 0:
            return True
        else:
            return False
    
    # Finding an effective path to identify the best solution
    def validPath(self):
        if self.mLeft >= 0 and self.mRight >= 0 and self.cLeft >= 0 and self.cRight >= 0 and self.mLeft == 0 or self.mRight == 0 and self.cLeft == 0 or self.cRight == 0:
            return True
        else:
            return False      
     
    def getSuccessors(currOutcome):
        nodes = [];
        if currOutcome.boat == 'left':
            newOutcome = MissCannProblem(currOutcome.cLeft, currOutcome.mLeft - 2, 'right', currOutcome.cRight, currOutcome.mRight + 2)
            # Two missionaries cross left to right
            if newOutcome.validPath():
                newOutcome.root = currOutcome
                nodes.append(newOutcome)
                newOutcome = MissCannProblem(currOutcome.cLeft - 2, currOutcome.mLeft, 'right', currOutcome.cRight + 2, currOutcome.mRight)
            # Two cannibals cross left to right
            if newOutcome.validPath():
                newOutcome.root = currOutcome
                nodes.append(newOutcome)
                newOutcome = MissCannProblem(currOutcome.cLeft - 1, currOutcome.mLeft - 1, 'right', currOutcome.cRight + 1, currOutcome.mRight + 1)
            # One missionary and one cannibal cross left to right
            if newOutcome.validPath():
                newOutcome.root = currOutcome
                nodes.append(newOutcome)
                newOutcome = MissCannProblem(currOutcome.cLeft, currOutcome.mLeft - 1, 'right', currOutcome.cRight, currOutcome.mRight + 1)
            # One missionary crosses left to right
            if newOutcome.validPath():
                newOutcome.root = currOutcome
                nodes.append(newOutcome)
                newOutcome = MissCannProblem(currOutcome.cLeft - 1, currOutcome.mLeft, 'right', currOutcome.cRight + 1, currOutcome.mRight)
            # One cannibal crosses left to right
            if newOutcome.validPath():
                newOutcome.root = currOutcome
                nodes.append(newOutcome)
        else:
            newOutcome = MissCannProblem(currOutcome.cLeft, currOutcome.mLeft + 2, 'left', currOutcome.cRight, currOutcome.mRight - 2)
            # Two missionaries cross right to left
            if newOutcome.validPath():
                newOutcome.root = currOutcome
                nodes.append(newOutcome)
                newOutcome = MissCannProblem(currOutcome.cLeft + 2, currOutcome.mLeft, 'left', currOutcome.cRight - 2, currOutcome.mRight)
            # Two cannibals cross right to left
            if newOutcome.validPath():
                newOutcome.root = currOutcome
                nodes.append(newOutcome)
                newOutcome = MissCannProblem(currOutcome.cLeft + 1, currOutcome.mLeft + 1, 'left', currOutcome.cRight - 1, currOutcome.mRight - 1)
            # One missionary and one cannibal cross right to left
            if newOutcome.validPath():
                newOutcome.root = currOutcome
                nodes.append(newOutcome)
                newOutcome = MissCannProblem(currOutcome.cLeft, currOutcome.mLeft + 1, 'left', currOutcome.cRight, currOutcome.mRight - 1)
            # One missionary crosses right to left
            if newOutcome.validPath():
                newOutcome.root = currOutcome
                nodes.append(newOutcome)
                newOutcome = MissCannProblem(currOutcome.cLeft + 1, currOutcome.mLeft, 'left', currOutcome.cRight - 1, currOutcome.mRight)
            # One cannibal crosses right to left
            if newOutcome.validPath():
                newOutcome.root = currOutcome
                nodes.append(newOutcome)
        return nodes
        
# Use of a breadth first search    
def breadthFirstSearch():
    initOutcome = MissCannProblem(3,3,'left',0,0)
    if initOutcome.endGoal():
        return initOutcome
        unIDSearch = list()
        idSearch = set()
        unIDSearch.append(initOutcome)
        while unIDSearch:
            outcome = unIDSearch.pop(0)
            if outcome.endGoal():
                return outcome
                idSearch.add(outcome)
                nodes = getSuccessors(outcome)
                for i in nodes:
                    if i not in idSearch or i not in unIDSearch:
                        unIDSearch.append(i)
        return None

def printProbSol(answer):
    path = []
    path.append(answer)
    root = answer.root
    while root:
        path.append(root)
        root = root.root
        for p in range(len(path)):
            outcome = path[len(path) - p - 1]
            print (str(outcome.cLeft) + ',' + str(outcome.mLeft) + ',' + str(outcome.boat) + ',' + str(outcome.cRight) + "," + str(outcome.mRight))

def main():
    bfs = breadthFirstSearch()
    print ('Crossing the River solution')
    print ('mLeft,cLeft,boat,mRight,cRight')
    printProbSol(bfs)

if __name__ == "__main__":
    main()