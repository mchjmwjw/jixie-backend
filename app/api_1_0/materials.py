# coding=utf8
from . import api
from flask import request, json, make_response, jsonify
from ..models import Material, db, Kind
from flask_cors import *


def serialize_instance(obj):
    d = {'__classname__': type(obj).__name__}
    d.update(vars(obj))
    return d


@api.route('/materials/save/', methods=['POST'])
def save():
    data = request.get_json()
    material = Material(data)
    db.session.add(material)
    db.session.commit()
    # 返回所有数据
    return get()


@api.route('/materials/get/', methods=['GET'])
def get():
    materials = Material.query.all()
    ms = []
    for item in materials:
        ms.append(item.to_json())
    data2 = json.dumps(ms)  # , default=serialize_instance)
    rst = make_response(data2)
    rst.headers['Access-Control-Allow-Origin'] = '*'
    return rst

# 保存tree数据
@api.route('/kindtree/save/', methods=['POST'])
# @cross_origin()
def savekind():
    data = request.get_json()
    dic = {}
    datalist = []
    # 保存新增的节点
    for v in data['mdata']:
        kind = Kind(v)
        if kind.phid < 0:
            oldid = kind.phid
            kind.phid = None
            db.session.add(kind)
            db.session.commit()
            dic[oldid] = kind.phid
        datalist.append(kind)
    # 保存修改/未修改的节点
    for d in datalist:
        if (d.pid is not None) and d.pid < 0:
            d.pid = dic[d.pid]
        kindDic = {}
        for (k, v) in d.__dict__.items():
            if(k is not '_sa_instance_state'):
                kindDic[k] = v
        k = Kind.query.filter_by(phid=d.phid).update(kindDic)
    # 删除已remove的节点
    for index in data['removeIds']:
        kind = Kind.query.filter_by(phid=index).first()
        db.session.delete(kind)

    db.session.commit()
    return gettree()
    # return jsonify(res='success')

# 获取树
@api.route('/kindtree/get/', methods=['GET'])
def gettree():
    kinds = Kind.query.all()
    ms = []
    for item in kinds:
        ms.append(item.to_json())
    data2 = json.dumps(ms)  # , default=serialize_instance)
    rst = make_response(data2)
    rst.headers['Access-Control-Allow-Origin'] = '*'
    return rst
