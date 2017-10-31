from rack import Rack


class Cluster:
    # Oppretter tom regneklynge for racks med oppgitt maxtall noder/ rack
    # @param noderPerRack max antall noder som kan plasseres i et rack
    def __init__(self, nodesPerRack):
        self.nodesPerRack = nodesPerRack
        self.rackList = [Rack(self.nodesPerRack)]

    # Alternativ konstruktor for de som loser oppgave d). Kan ellers ignoreres
    # Leser data om regneklynge fra fil, bygger datastrukturen.
    # @param filnavn filene der dataene for regneklyngen ligger
#	def __init__(self, filnavn):
#		pass

    # Plasserer en node inn i et rack med ledig plass, eller i et nytt
    # @param node referanse til noden som skal settes inn i datastrukturen
    def insertNode(self, node):
        if self.rackList[-1].getNodeNumber() >= self.rackList[-1].totalNumberOfNodes:
            self.rackList.append(Rack(self.nodesPerRack))
            self.rackList[-1].insertNode(node)
        else:
            self.rackList[-1].insertNode(node)

    # Beregner totalt antall prosessorer i hele regneklyngen
    # @return totalt antall prosessorer
    def getProcessorTotal(self):
        processors = 0
        for rack in self.rackList:
            processors += rack.getProcessorTotal()
        return processors

    def getNodeTotal(self):
        nodes = 0
        for rack in self.rackList:
            nodes += rack.getNodeNumber()
        return nodes

    # Beregner antall noder i regneklyngen med minne over angitt grense
    # @param paakrevdMinne hvor mye minne skal noder som telles med ha
    # @return antall noder med tilstrekkelig minne
    def necessaryNodeMemoy(self, requiredMemory):
        nodesWithEnoughMemory = 0
        for rack in self.rackList:
            nodesWithEnoughMemory += rack.necessaryNodeMemory(requiredMemory)
        return nodesWithEnoughMemory

    # Henter antall racks i regneklyngen
    # @return antall racks
    def getRackTotal(self):
        return len(self.rackList)
