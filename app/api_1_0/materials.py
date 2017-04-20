# coding=utf8
from . import api
from flask import request, json, make_response, jsonify
from ..models import Material, db, Kind


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


@api.route('/kindtree/save/', methods=['POST'])
def savekind():
    data = request.get_json()
    for v in data['mdata']:
        kind = Kind(v)
        db.session.add(kind)
        db.session.commit()
    return 'success'


@api.route('/kindtree/get/', methods=['GET'])
def gettree():
    kinds = Kind.query.all()
