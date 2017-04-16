from .. import db


class Material(db.Model):
    __tablename__ = 'materials'
    phid = db.Column(db.Integer, primary_key=True)
    m_no = db.Column(db.String(255), unique=True)
    m_name = db.Column(db.String(1000))
    m_unit = db.Column(db.String(50))
    m_amount = db.Column(db.Integer)
    m_kind = db.Column(db.String(255))
    m_remark = db.Column(db.String(1000))

    def __init__(self, obj):
        mobj = obj['mdata']
        self.m_amount = mobj['m_amount']
        self.phid = mobj['phid']
        self.m_no = mobj['m_no']
        self.m_name = mobj['m_name']
        self.m_unit = mobj['m_unit']
        self.m_kind = mobj['m_kind']
        self.m_remark = mobj['m_remark']

    def to_json(self):
        mjson = {
            'phid': self.phid,
            'm_amount': self.m_amount,
            'm_no': self.m_no,
            'm_name': self.m_name,
            'm_unit': self.m_unit,
            'm_kind': self.m_kind,
            'm_remark': self.m_remark
        }
        return mjson

    def __repr__(self):
        return '<Material %r>' % self.m_name