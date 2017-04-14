# coding=utf8
from . import api
from flask import request, json, make_response, jsonify
from ..models import Material, db


def serialize_instance(obj):
    d = {'__classname__': type(obj).__name__}
    d.update(vars(obj))
    return d


@api.route('/materials/save/', methods=['POST'])
def save():
    data = request.get_json()
    material = Material(data)
    # for(k, v) in data.items():
    db.session.add(material)
    db.session.commit()
    # 返回所有数据
    materials = Material.query.all()
    data2 = json.dumps(materials, default=serialize_instance)
    rst = make_response(data2)
    rst.headers['Access-Control-Allow-Origin'] = '*'
    return rst


@api.route('/materials/get/', methods=['GET'])
def get():
    materials = Material.query.all()
    data2 = json.dumps(materials[0].to_json())  # , default=serialize_instance)
    rst = make_response(data2)
    rst.headers['Access-Control-Allow-Origin'] = '*'
    return rst

