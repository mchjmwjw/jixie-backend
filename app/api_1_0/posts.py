# coding=utf8
from flask import jsonify, request, g, abort, url_for, current_app
from . import api
from flask import json, make_response
from flask_json import FlaskJSON,as_json_p
from flask_cors import *


class material(object):
    def __init__(self, phid, m_no, m_name, m_unit, m_amount, m_kind, m_remark):
        self.phid = phid
        self.m_no = m_no
        self.m_name = m_name
        self.m_unit = m_unit
        self.m_amount = m_amount
        self.m_kind = m_kind
        self.m_remark = m_remark

data = [material(1, '10001', u'铁板', u'吨', 12, u'类别1', u'无')]


def serialize_instance(obj):
    d = {'__classname__': type(obj).__name__}
    d.update(vars(obj))
    return d


@api.route('/jsonp/', methods=['GET'])
@as_json_p
def get_jsonp():
    return json.dumps(data, default=serialize_instance)


@api.route('/cors/')
# @cross_origin()
def set_header():
    data2 = json.dumps(data, default=serialize_instance)
    rst = make_response(data2)
    rst.headers['Access-Control-Allow-Origin'] = '*'
    # rst.headers['Access-Control-Allow-Methods'] = 'POST, GET, OPTIONS'
    # rst.headers['Access-Control-Allow-Headers'] = 'Origin, X-Requested-With, Content-Type, Accept, Authorization'
    # rst.headers['Access-Control-Allow-Origin'] = '*'
    # rst.headers['Access-Control-Request-Method'] = '*'
    # rst.headers['Content-Type'] = 'text/html; charset=utf-8'
    # rst.headers['Access-Control-Max-Age'] = '1728000'
    return rst
