from panda3d.core import LVector3f
<<<<<<< HEAD
from toontown.dna import DNAGroup
from toontown.dna import DNABattleCell
from toontown.dna import DNAUtil
=======
import DNAGroup
import DNABattleCell
from DNAUtil import *
>>>>>>> origin/master

class DNAVisGroup(DNAGroup.DNAGroup):
    __slots__ = (
        'visibles', 'suitEdges', 'battleCells')
    
    COMPONENT_CODE = 2

    def __init__(self, name):
        DNAGroup.DNAGroup.__init__(self, name)
        self.visibles = []
        self.suitEdges = []
        self.battleCells = []

    def getVisGroup(self):
        return self

    def addBattleCell(self, battleCell):
        self.battleCells.append(battleCell)

    def addSuitEdge(self, suitEdge):
        self.suitEdges.append(suitEdge)

    def addVisible(self, visible):
        self.visibles.append(visible)

    def getBattleCell(self, i):
        return self.battleCells[i]

    def getNumBattleCells(self):
        return len(self.battleCells)

    def getNumSuitEdges(self):
        return len(self.suitEdges)

    def getNumVisibles(self):
        return len(self.visibles)

    def getSuitEdge(self, i):
        return self.suitEdges[i]

    def getVisibleName(self, i):
        return self.visibles[i]

    def removeBattleCell(self, cell):
        self.battleCells.remove(cell)

    def removeSuitEdge(self, edge):
        self.suitEdges.remove(edge)

    def removeVisible(self, visible):
        self.visibles.remove(visible)

    def makeFromDGI(self, dgi, dnaStorage):
        DNAGroup.DNAGroup.makeFromDGI(self, dgi)

        numEdges = dgi.getUint16()
        for _ in xrange(numEdges):
            index = dgi.getUint16()
            endPoint = dgi.getUint16()
            self.addSuitEdge(dnaStorage.getSuitEdge(index, endPoint))

        numVisibles = dgi.getUint16()
        for _ in xrange(numVisibles):
            self.addVisible(dgiExtractString8(dgi))

        numCells = dgi.getUint16()
        for _ in xrange(numCells):
            w = dgi.getUint8()
            h = dgi.getUint8()
            x, y, z = [dgi.getInt32() / 100.0 for i in xrange(3)]
            self.addBattleCell(DNABattleCell.DNABattleCell(w, h, LVector3f(x, y, z)))
            
    def packerTraverse(self, recursive=True, verbose=False):
        packer = DNAGroup.DNAGroup.packerTraverse(self, recursive=False, verbose=verbose)
        packer.name = 'DNAVisGroup'  # Override the name for debugging.
        packer.pack('suit edge count', len(self.suitEdges), UINT16)
        for edge in self.suitEdges:
            startPointIndex = edge.startPoint.index
            packer.pack('start point index', startPointIndex, UINT16)
            endPointIndex = edge.endPoint.index
            packer.pack('end point index', endPointIndex, UINT16)
        packer.pack('visible count', len(self.visibles), UINT16)
        for visible in self.visibles:
            packer.pack('visible', visible, STRING)
        packer.pack('battle cell count', len(self.battleCells), UINT16)
        for cell in self.battleCells:
            packer.pack('width', cell.width, UINT8)
            packer.pack('height', cell.height, UINT8)
            for component in cell.pos:
                packer.pack('position', int(component * 100), INT32)
        if recursive:
            packer += self.packerTraverseChildren(verbose=verbose)
        return packer
