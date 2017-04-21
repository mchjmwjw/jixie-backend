from .. import db


class Kind(db.Model):
    __tablename__ = 'kind'
    phid = db.Column(db.Integer, primary_key=True)
    pid = db.Column(db.Integer)
    k_name = db.Column(db.String(500))

    def __init__(self, obj):
        self.phid = obj['phid']
        self.pid = obj['pid']
        self.k_name = obj['k_name']

    def to_json(self):
        mjson = {
            'phid': self.phid,
            'pid': self.pid,
            'k_name': self.k_name
        }
        return mjson

    def __repr__(self):
        return '<Kind %r>' % self.k_name
