# coding=utf8
from . import api
from flask import request, json, make_response


@api.route('/materials/save/', methods=['POST'])
def save():
    i = request.json
    rst = make_response('xxx')
    rst.headers['Access-Control-Allow-Origin'] = '*'
    return rst
