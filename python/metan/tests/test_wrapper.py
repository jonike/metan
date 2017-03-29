# -*- coding:utf-8 -*-
import unittest
import maya.cmds as cmds
import maya.mel as mel
import metan.core as mtn


class TestScene(unittest.TestCase):

    def test_getset(self):
        cmds.file(new=True, f=True)
        cube = cmds.polyCube()[0]
        print cube
        m = mtn.M(u"pCube1")


        print 'm.t.get()', m.t.get()
        print 'm.translate.get()', m.translate.get()
        print 'm.tx.get()', m.tx.get()
        print 'm.translateX.get()', m.translateX.get()
        print 'm.t.x.get()', m.t.x.get()
        print 'm.translate.x.get()', m.translate.x.get()
        print 'm.t.tx.get()', m.t.tx.get()
        print 'm.translate.translateX.get()', m.translate.translateX.get()
        print " "
        print 'm.attr("t").get()', m.attr("t").get()
        print 'm.attr("translate").get()', m.attr("translate").get()
        print 'm.attr("tx").get()', m.attr("tx").get()
        print 'm.attr("translateX").get()', m.attr("translateX").get()
        print 'm.attr("t").x.get()', m.attr("t").x.get()
        print 'm.attr("translate").x.get()', m.attr("translate").x.get()
        print 'm.attr("t").tx.get()', m.attr("t").tx.get()
        print 'm.attr("translate").tx.get()', m.attr("translate").tx.get()
        print 'm.attr("t").attr("x").get()', m.attr("t").attr("x").get()
        print 'm.attr("translate").attr("x").get()', m.attr("translate").attr("x").get()
        print 'm.attr("t").attr("tx").get()', m.attr("t").attr("tx").get()
        print 'm.attr("translate").attr("translateX").get()', m.attr("translate").attr("translateX").get()
        print " "
        print 'm.m.get()', m.m.get()
        print 'm.matrix.get()', m.matrix.get()
        print 'm.pim.get()', m.pim.get()
        print 'm.parentInverseMatrix.get()', m.parentInverseMatrix.get()
        print 'm.pim[0].get()', m.pim[0].get()
        print 'm.parentInverseMatrix[0].get()', m.parentInverseMatrix[0].get()
        print 'm.attr("pim").get()', m.attr("pim").get()
        print 'm.attr("parentInverseMatrix").get()', m.attr("parentInverseMatrix").get()
        print 'm.attr("pim")[0].get()', m.attr("pim")[0].get()
        print 'm.attr("parentInverseMatrix")[0].get()', m.attr("parentInverseMatrix")[0].get()
        print 'm.attr("pim[0]").get()', m.attr("pim[0]").get()
        print 'm.attr("parentInverseMatrix[0]").get()', m.attr("parentInverseMatrix[0]").get()

        assert(repr(m.t.getChildren()) == u'[Attribute("translateX"), Attribute("translateY"), Attribute("translateZ")]')

        print "="*20

        cmds.circle()
        m = mtn.M(u"nurbsCircleShape1")
        assert(m.wn.get() == [[0.0, 0.0, 1.0]])
        assert(m.attr("wn").get() == [[0.0, 0.0, 1.0]])
        assert(m.worldNormal.get() == [[0.0, 0.0, 1.0]])
        assert(m.attr("worldNormal").get() == [[0.0, 0.0, 1.0]])
        assert(m.wn[0].get() == [0.0, 0.0, 1.0])
        assert(m.attr("wn")[0].get() == [0.0, 0.0, 1.0])
        assert(m.attr("wn[0]").get() == [0.0, 0.0, 1.0])
        assert(m.worldNormal[0].get() == [0.0, 0.0, 1.0])
        assert(m.attr("worldNormal")[0].get() == [0.0, 0.0, 1.0])
        assert(m.attr("worldNormal[0]").get() == [0.0, 0.0, 1.0])
        assert(m.wn.wnx.get() == 0.0)
        assert(m.attr("wn").wnx.get() == 0.0)
        assert(m.attr("wn").attr("wnx").get() == 0.0)
        assert(m.worldNormal.wnx.get() == 0.0)
        assert(m.attr("worldNormal").wnx.get() == 0.0)
        assert(m.attr("worldNormal").attr("wnx").get() == 0.0)
        assert(m.worldNormal.worldNormalX.get() == 0.0)
        assert(m.attr("worldNormal").worldNormalX.get() == 0.0)
        assert(m.attr("worldNormal").attr("worldNormalX").get() == 0.0)
        assert(m.wn.x.get() == 0.0)
        assert(m.attr("wn").x.get() == 0.0)
        assert(m.attr("wn").attr("x").get() == 0.0)
        assert(m.worldNormal.x.get() == 0.0)
        assert(m.attr("worldNormal").x.get() == 0.0)
        assert(m.attr("worldNormal").attr("x").get() == 0.0)
        assert(m.worldNormal[0].wnx.get() == 0.0)
        assert(m.attr("worldNormal")[0].wnx.get() == 0.0)
        assert(m.attr("worldNormal")[0].attr("wnx").get() == 0.0)
        assert(m.attr("worldNormal[0]").wnx.get() == 0.0)
        assert(m.attr("worldNormal[0]").attr("wnx").get() == 0.0)
        assert(m.worldNormal[0].x.get() == 0.0)
        assert(m.attr("worldNormal")[0].x.get() == 0.0)
        assert(m.attr("worldNormal")[0].attr("x").get() == 0.0)
        assert(m.attr("worldNormal[0]").x.get() == 0.0)
        assert(m.attr("worldNormal[0]").attr("x").get() == 0.0)
        assert(m.worldNormal[0].worldNormalX.get() == 0.0)
        assert(m.attr("worldNormal")[0].worldNormalX.get() == 0.0)
        assert(m.attr("worldNormal")[0].attr("worldNormalX").get() == 0.0)
        assert(m.attr("worldNormal[0]").worldNormalX.get() == 0.0)
        assert(m.attr("worldNormal[0]").attr("worldNormalX").get() == 0.0)
        assert(m.mmv.get() == [0.0, 8.0])
        assert(m.minMaxValue.get() == [0.0, 8.0])
        assert(m.obcc.get() == [0.0, 0.0, 0.0])
        assert(m.attr("obcc").get() == [0.0, 0.0, 0.0])
        assert(m.objectColorRGB.get() == [0.0, 0.0, 0.0])
        assert(m.attr("objectColorRGB").get() == [0.0, 0.0, 0.0])
        assert(m.obcc.obcr.get() == 0.0)
        assert(m.attr("obcc").obcr.get() == 0.0)
        assert(m.attr("obcc").attr("obcr").get() == 0.0)
        assert(m.objectColorRGB.obcr.get() == 0.0)
        assert(m.attr("objectColorRGB").obcr.get() == 0.0)
        assert(m.attr("objectColorRGB").attr("obcr").get() == 0.0)
        assert(m.objectColorRGB.objectColorR.get() == 0.0)
        assert(m.attr("objectColorRGB").attr("objectColorR").get() == 0.0)
        assert(m.objectColorR.get() == 0.0)
        assert(m.attr("objectColorR").get() == 0.0)

        m = mtn.M(u"pCubeShape1")
        assert(m.vertexColor[0].vertexFaceColor[0].get() == [[0.0, 0.0, 0.0], 1.0])
        assert(m.attr("vertexColor")[0].vertexFaceColor[0].get() == [[0.0, 0.0, 0.0], 1.0])
        assert(m.attr("vertexColor")[0].attr("vertexFaceColor")[0].get() == [[0.0, 0.0, 0.0], 1.0])
        assert(m.attr("vertexColor[0]").attr("vertexFaceColor")[0].get() == [[0.0, 0.0, 0.0], 1.0])
        assert(m.attr("vertexColor[0]").attr("vertexFaceColor[0]").get() == [[0.0, 0.0, 0.0], 1.0])
        assert(m.vertexColor[0].vertexFaceColor[0].vertexFaceColorRGB.get() == [0.0, 0.0, 0.0])
        assert(m.vertexColor[0].vertexFaceColor[0].attr("vertexFaceColorRGB").get() == [0.0, 0.0, 0.0])
        assert(m.vertexColor[0].attr("vertexFaceColor")[0].vertexFaceColorRGB.get() == [0.0, 0.0, 0.0])
        assert(m.attr("vertexColor")[0].vertexFaceColor[0].vertexFaceColorRGB.get() == [0.0, 0.0, 0.0])
        assert(m.attr("vertexColor")[0].attr("vertexFaceColor")[0].vertexFaceColorRGB.get() == [0.0, 0.0, 0.0])
        assert(m.attr("vertexColor")[0].attr("vertexFaceColor")[0].attr("vertexFaceColorRGB").get() == [0.0, 0.0, 0.0])
        assert(m.attr("vertexColor[0]").attr("vertexFaceColor")[0].attr("vertexFaceColorRGB").get() == [0.0, 0.0, 0.0])
        assert(m.attr("vertexColor[0]").attr("vertexFaceColor[0]").attr("vertexFaceColorRGB").get() == [0.0,0.0,0.0])

        assert(m.vertexColor[0].vertexFaceColor[0].vertexFaceColorRGB.vertexFaceColorB.get() == 0.0)

        mel.eval("curve -d 3 -p -6.875966 0 1.086021 -p -5.392687 0 2.925972 -p -2.426129 0 6.605875 \
         -p 5.887674 0 7.227014 -p 2.9318 0 2.277118 -p -8.971029 0 -5.450958 -p 1.340971 0 4.394752 \
         -p -1.974355 0 6.056083 -p -3.632019 0 6.886748 -k 0 -k 0 -k 0 -k 1 -k 2 -k 3 -k 4 -k 5 -k 6 -k 6 -k 6 ;")
        m = mtn.M(u"curveShape1")
        assert(m.cp.name() == u"curveShape1.controlPoints")
        assert(m.attr("cp").name() == u"curveShape1.controlPoints")
        assert(m.attr("controlPoints").name() == u"curveShape1.controlPoints")
        assert(m.cp.size() == 9)
        assert(m.attr("cp").size() == 9)
        assert(m.attr("controlPoints").size() == 9)
        assert(len(m.cp) == 9)
        assert(len(m.attr("cp")) == 9)
        assert(len(m.attr("controlPoints")) == 9)
        for a in m.controlPoints:
            print a.name(), a.get()


        assert(mtn.M(u"pCube1.t").name() == u'pCube1.translate')
        assert(mtn.M(u"pCube1.translate").name() == u'pCube1.translate')
        assert(mtn.M(u"pCube1.t.tx").name() == u'pCube1.translateX')
        assert(mtn.M(u"pCube1.translate.translateX").name() == u'pCube1.translateX')
        assert(mtn.M(u"pCube1.tx").name() == u'pCube1.translateX')
        assert(mtn.M(u"pCube1.translateX").name() == u'pCube1.translateX')
        assert(mtn.M(u"pCube1.wm").name() == u'pCube1.worldMatrix')
        assert(mtn.M(u"pCube1.wm[0]").name() == u'pCube1.worldMatrix[0]')

        assert(mtn.M(u"pCubeShape1.vertexColor.vertexFaceColor.vertexFaceColorRGB.vertexFaceColorB").name()
                == u'pCubeShape1.vertexColor[0].vertexFaceColor[0].vertexFaceColorB')

        assert(mtn.M(u"pCubeShape1.vertexColor[0].vertexFaceColor[0].vertexFaceColorRGB.vertexFaceColorB").name()
               == u'pCubeShape1.vertexColor[0].vertexFaceColor[0].vertexFaceColorB')



    def test_types(self):
        print("start : node type test.")
        cmds.file(new=True, f=True)

        m = mtn.M(cmds.polyCube()[0])
        _name = m.name()
        m2 = mtn.M(_name)
        assert(m.nodeType() == u'transform')
        assert(hash(m) == hash(m2))
        assert(hash(m.t) == hash(m2.attr("t")))
        assert(hash(m.translate) == hash(m2.attr("t")))
        assert(hash(m.t) == hash(m2.attr("translate")))
        assert(hash(m.t.tx) == hash(m2.attr("translate").tx))
        assert(hash(m.tx) == hash(m2.attr("translate").attr("tx")))
        assert(hash(m.translateX) == hash(m2.attr("translate").attr("tx")))
        assert(hash(m.pim) == hash(m2.attr("pim")))
        assert(hash(m.pim) == hash(m2.pim))
        assert(hash(m.pim[0]) != hash(m2.pim))
        assert(hash(m.pim[0]) == hash(m2.pim[0]))
        assert(hash(mtn.M(_name+".translateX")) == hash(mtn.M(_name).attr("t").attr("tx")))
        assert(hash(mtn.M(_name+".translateX")) == hash(mtn.M(_name).attr("t.translateX")))
        assert(m == m2)
        assert(m.t == m2.attr("t"))
        assert(m.translate == m2.attr("t"))
        assert(m.t == m2.attr("translate"))
        assert(m.t.tx == m2.attr("translate").tx)
        assert(m.tx == m2.attr("translate").attr("tx"))
        assert(m.translateX == m2.attr("translate").attr("tx"))
        assert(m.pim == m2.attr("pim"))
        assert(m.pim == m2.pim)
        assert(m.pim[0] != m2.pim)
        assert(m.pim[0] == m2.pim[0])
        assert(mtn.M(_name+".translateX") == mtn.M(_name).attr("t").attr("tx"))
        assert(mtn.M(_name+".translateX") == mtn.M(_name).attr("t.translateX"))

        j = mtn.M(cmds.createNode(u"joint"))
        assert(j.nodeType() == u'joint')

        t = mtn.M(u"time1")
        assert(t.nodeType() == u'time')

        print("end : node type test.")

    def runTest(self):
        self.test_getset()
        self.test_types()



