class Node():
    # Oppretter en node med gitt minne-storrelse og antall prosessorer
    #  @param memory GB minne i den nye noden
    #  @param amountOfProcessors antall prosessorer i den nye noden
    def __init__(self, memory, amountOfProcessors):
        self.memory = memory
        self.amountOfProcessors = amountOfProcessors

    # Henter antall prosessorer i noden
    #  @return antall prosessorer i noden
    def getProcessorTotal(self):
        return self.amountOfProcessors

    # Sjekker om noden har tilstrekkelig minne for et program
    #  @param requiredMemory GB minne som kreves for programmet
    #  @return True hvis noden har minst saa mye minne
    def enoughMemory(self, requiredMemory):
        if self.memory >= requiredMemory:
            return True
        else:
            return False
