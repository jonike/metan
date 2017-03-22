# -*- coding:utf-8 -*-
from __future__ import print_function
from __future__ import absolute_import
from __future__ import division

import maya.cmds as cmds
import maya.api.OpenMaya as om


class MetanAttr(object):

    def __new__(cls, *args, **kws):
        _api_objects = dict([(k, None) for k in ["_mDependNode", "_mPlug", "_mObject", "_mHandle"]])
        _cache = dict([(k, None) for k in ["_isCompound", "_numChildren", "_apiType", "_apiTypeStr"]])
        newobj = super(cls.__class__, cls).__new__(cls)

        # if args[0].type() == om.MFn.kDependencyNode:
        if isinstance(args[0], om.MFnDependencyNode):
            _dependnode = args[0]
            _plug = _dependnode.findPlug(_dependnode.attribute(args[1]), False)
            _api_objects["_mDependNode"] = _dependnode

        # elif isinstance(args[0], om.MPlug):
        elif isinstance(args[0], MetanAttr):
            _pplug = args[0]
            _dependnode = _pplug._mDependNode
            _plug = _dependnode.findPlug(_dependnode.attribute(args[1]), False)

        elif isinstance(args[0], om.MPlug):
            _plug = args[0]

        _attribute = _plug.attribute()

        _api_objects["_mPlug"] = _plug
        _api_objects["_mObject"] = _attribute
        _cache["_isCompound"] = _plug.isCompound
        if _cache["_isCompound"]:
            _cache["_numChildren"] = _plug.numChildren()
        _cache["_apiType"] = _attribute.apiType()
        _cache["_apiTypeStr"] = _attribute.apiTypeStr

        for k, v in _api_objects.items():
            newobj.__setattr__(k, v)

        for k, v in _cache.items():
            newobj.__setattr__(k, v)

        return newobj

    def attr(self, attr):
        try:
            return MetanAttr(self, attr)
        except RuntimeError:
            try:
                _attr = self._mPlug.partialName()+attr
                return MetanAttr(self, _attr)
            except RuntimeError:
                raise AttributeError("%r has no attribute or method named '%s'" % (self, attr))

    def __getattr__(self, attr):
        # todo: self.attrをコールせずにアトリビュートの有無を確認して例外処理した方が効率がよいのでは？
        return self.attr(attr)

    def __repr__(self):
        return '{0}("{1}")'.format(self.__class__.__name__, self.name())

    def __str__(self):
        return self.__repr__()

    def __iter__(self):
        u"""TODO: これ実装しないと無限ループする"""
        pass

    def __getitem__(self, index):
        # return self.attr("{0}[{1}]".format(self._mDependNode.name(), index))
        # return self.attr(self._mPlug.elementByLogicalIndex(index))
        return MetanAttr(self._mPlug.elementByLogicalIndex(index))

    def name(self):
        return self._mPlug.name().split(".")[-1]

    def _get_plug_value(self, plug):
        _obj = plug.attribute()
        _apitype = _obj.apiType()
        # _obj = self._mObject
        # _apitype = self._apiType
        # print(_obj.apiTypeStr, plug.name())

        if _apitype in [om.MFn.kAttribute3Double, om.MFn.kAttribute3Float, om.MFn.kAttribute4Double]:
            res = []
            _plug = None
            _count_children = plug.numChildren()
            for i in range(_count_children):
                _plug = plug.child(i)
                res.append(self._get_plug_value(_plug))

            _child_apitype = _plug.attribute().apiType()

            if _count_children > 3:
                return res

            if _child_apitype in [om.MFn.kDoubleLinearAttribute, om.MFn.kFloatLinearAttribute]:
                return om.MVector(res)
            elif _child_apitype in [om.MFn.kDoubleAngleAttribute, om.MFn.kFloatAngleAttribute]:
                return om.MVector(res)
            else:
                return res

        elif _apitype in [om.MFn.kDoubleAngleAttribute, om.MFn.kFloatAngleAttribute]:
            angle_unit = om.MAngle.uiUnit()
            if angle_unit == om.MAngle.kDegrees:
                return plug.asMAngle().asDegrees()
            else:
                return plug.asDouble()

        elif _apitype in [om.MFn.kDoubleLinearAttribute, om.MFn.kFloatLinearAttribute]:
            return plug.asDouble()

        elif _apitype == om.MFn.kNumericAttribute:
            _mfnattr = om.MFnNumericAttribute(_obj)
            _type = _mfnattr.numericType()
            if _type == om.MFnNumericData.kBoolean:
                return plug.asBool()
            elif _type in [om.MFnNumericData.kShort, om.MFnNumericData.kInt, om.MFnNumericData.kLong, om.MFnNumericData.kByte]:
                return plug.asInt()
            elif _type in [om.MFnNumericData.kFloat, om.MFnNumericData.kDouble, om.MFnNumericData.kAddr]:
                return plug.asDouble()

        elif _apitype == om.MFn.kEnumAttribute:
            return plug.asInt()

        elif _apitype == om.MFn.kTypedAttribute:
            _mfnattr = om.MFnTypedAttribute(_obj)
            _type = _mfnattr.attrType()
            if _type == om.MFnData.kString:
                return plug.asString()
            elif _type == om.MFnData.kMatrix:
                # print(plug.name(), plug.isArray, plug.isElement)
                if plug.isArray:
                    return om.MFnMatrixData(plug.elementByLogicalIndex(0).asMObject()).matrix()
                # if plug.isElement:
                #     print(plug.array())
                #     return om.MFnMatrixData(plug.asMObject()).matrix()
                return om.MFnMatrixData(plug.asMObject()).matrix()

        elif _apitype == om.MFn.kCompoundAttribute:
            res = []
            _plug = None
            _count_children = plug.numChildren()
            for i in range(_count_children):
                _plug = plug.child(i)
                res.append(self._get_plug_value(_plug))
            return res

    def get(self):
        # todo: 型に応じて適切な値をget
        return self._get_plug_value(self._mPlug)
        # return self._mPlug.asDouble()

    def set(self, value):
        self.set_by_cmds(value)
        # self.set_by_api(value)

    def set_by_cmds(self, value):
        # todo: 型に応じて適切な値をset cmds.setAttr()を利用する
        cmds.setAttr(self._mPlug.name(), value)

    def set_by_api(self, value):
        # todo: 型に応じて適切な値をset apiでsetする undo非サポート
        self._mPlug.setDouble(value)

    # def valid(self):
    #     return self._mHandle.isValid()

