class Rack():
    # oppretter et rack der det senere kan plasseres noder
    #
    def __init__(self, totalNumberOfNodes):
        self.totalNumberOfNodes = totalNumberOfNodes
        self.nodeList = []

    # Plasserer en ny node inn i racket
    #  @param node noden som skal plasseres inn
    def insertNode(self, node):
        self.nodeList.append(node)

    # Henter antall noder i racket
    # @return antall noder
    def getNodeNumber(self):
        return len(self.nodeList)

    # Beregner sammenlagt antall prosessorer i nodene i et rack
    # @return antall prosessorer
    def getProcessorTotal(self):
        processors = 0
        for node in self.nodeList:
            processors += node.getProcessorTotal()
        return processors

    # Beregner antall noder i racket med minne over gitt grense
    # @param paakrevdMinne antall GB minne som kreves
    # @return antall noder med tilstrekkelig minne
    def necessaryNodeMemory(self, requiredMemory):
        nodesWithEnoughMemory = 0
        for node in self.nodeList:
            if node.enoughMemory(requiredMemory):
                nodesWithEnoughMemory += 1
        return nodesWithEnoughMemory
