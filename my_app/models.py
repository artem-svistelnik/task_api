from my_app import db


class Products(db.Model):
    id=db.Column(db.Integer,autoincrement=True)
    title=db.Column(db.VARCHAR,nullable=False)
    asin=db.Column(db.VARCHAR,nullable=False,primary_key=True)
    reviewses = db.relationship('Reviews', backref='products', lazy=True)
    def __repr__(self):
        return self.asin

    def to_dict(self):
        return {'id':self.id,
                'title':self.title,
                'asin':self.asin}

class Reviews(db.Model):
    id=db.Column(db.Integer,autoincrement=True,primary_key=True)
    products_asin=db.Column(db.VARCHAR, db.ForeignKey('products.asin'),nullable=False)
    title = db.Column(db.VARCHAR, nullable=False)
    review=db.Column(db.TEXT,nullable=False)

    def __repr__(self):
        return '<Asin {}>'.format(self.products_asin)

    def to_dict(self):
        return {'id': self.id,
                'title': self.title,
                'asin': self.products_asin,
                'review':self.review}
