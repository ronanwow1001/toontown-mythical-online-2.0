from panda3d.core import LVector3f, PandaNode
<<<<<<< HEAD
from toontown.dna import DNAGroup
=======
from DNAUtil import *
import DNAGroup
>>>>>>> origin/master

class DNANode(DNAGroup.DNAGroup):
    __slots__ = (
        'pos', 'hpr', 'scale')

    COMPONENT_CODE = 3

    def __init__(self, name):
        DNAGroup.DNAGroup.__init__(self, name)
        self.pos = LVector3f()
        self.hpr = LVector3f()
        self.scale = LVector3f(1, 1, 1)

    def getPos(self):
        return self.pos

    def setPos(self, pos):
        self.pos = pos

    def getHpr(self):
        return self.hpr

    def setHpr(self, hpr):
        self.hpr = hpr

    def getScale(self):
        return self.scale

    def setScale(self, scale):
        self.scale = scale

    def makeFromDGI(self, dgi):
        DNAGroup.DNAGroup.makeFromDGI(self, dgi)

        x = dgi.getInt32() / 100.0
        y = dgi.getInt32() / 100.0
        z = dgi.getInt32() / 100.0
        self.pos = LVector3f(x, y, z)

        h = dgi.getInt32() / 100.0
        p = dgi.getInt32() / 100.0
        r = dgi.getInt32() / 100.0
        self.hpr = LVector3f(h, p, r)

        sx = dgi.getInt16() / 100.0
        sy = dgi.getInt16() / 100.0
        sz = dgi.getInt16() / 100.0
        self.scale = LVector3f(sx, sy, sz)

    def traverse(self, nodePath, dnaStorage):
        node = PandaNode(self.name)
        node = nodePath.attachNewNode(node, 0)
        node.setPosHprScale(self.pos, self.hpr, self.scale)
        for child in self.children:
            child.traverse(node, dnaStorage)
        
        node.flattenMedium()
        
    def packerTraverse(self, recursive=True, verbose=False):
        packer = DNAGroup.DNAGroup.packerTraverse(self, recursive=False, verbose=verbose)
        packer.name = 'DNANode'  # Override the name for debugging.
        for component in self.pos:
            packer.pack('position', int(component * 100), INT32)
        for component in self.hpr:
            packer.pack('rotation', int(component * 100), INT32)
        for component in self.scale:
            packer.pack('scale', int(component * 100), UINT16)
        if recursive:
            packer += self.packerTraverseChildren(verbose=verbose)
        return packer