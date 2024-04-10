from .. import db


class TowerStaybarConr(db.Model):
    __tablename__ = 'tower_staybar_conr'
    phid = db.Column(db.Integer, primary_key=True)
    c_no = db.Column(db.String(255), unique=True)
    o_time = db.Column(db.String(255))
    d_time = db.Column(db.String(255))
    amount = db.Column(db.Integer)
    mapper = db.Column(db.String(255))
    client = db.Column(db.String(255))
    order_no = db.Column(db.String(255))

    def __init__(self, obj):
        mobj = obj['mdata']
        self.m_amount = mobj['m_amount']
        self.phid = mobj['phid']
        self.m_no = mobj['m_no']
        self.m_name = mobj['m_name']
        self.m_unit = mobj['m_unit']
        self.m_kind = mobj['m_kind']
        self.m_remark = mobj['m_remark']
        self.kind_id = obj["kind_id"]

    def to_json(self):
        mjson = {
            'phid': self.phid,
            'm_amount': self.m_amount,
            'm_no': self.m_no,
            'm_name': self.m_name,
            'm_unit': self.m_unit,
            'm_kind': self.m_kind,
            'm_remark': self.m_remark,
            'kind_id': self.kind_id
        }
        return mjson

    def __repr__(self):
        return '<Material %r>' % self.m_name