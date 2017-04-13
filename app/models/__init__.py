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

    def __repr__(self):
        return '<Material %r>' % self.m_name

