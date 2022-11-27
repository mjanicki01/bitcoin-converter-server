from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def connect_db(app):
    db.app = app
    db.init_app(app)



class EURData(db.Model):
    __tablename__ = "eur"

    currency = db.Column(
        db.String,
        primary_key = True,
        default="eur",
        unique= False,
        nullable = False
    )

    xValueRate = db.Column(
        db.Integer,
        unique = False,
        nullable = False
    )

    yValueDate = db.Column(
        db.String,
        unique = True,
        nullable = False
    )

    def serialize(self):
        return {
            'currency': self.currency,
            'xValue-Rate': self.xValueRate,
            'yValue-Date': self.yValueDate
        }


class USDData(db.Model):
    __tablename__ = "usd"

    currency = db.Column(
        db.String,
        primary_key = True,
        default="usd",
        unique= False,
        nullable = False
    )

    xValueRate = db.Column(
        db.Integer,
        unique = False,
        nullable = False
    )

    yValueDate = db.Column(
        db.String,
        unique = True,
        nullable = False
    )

    def serialize(self):
        return {
            'currency': self.currency,
            'xValue-Rate': self.xValueRate,
            'yValue-Date': self.yValueDate
        }


class GBPData(db.Model):
    __tablename__ = "gbp"

    currency = db.Column(
        db.String,
        primary_key = True,
        default="gpb",
        unique= False,
        nullable = False
    )

    xValueRate = db.Column(
        db.Integer,
        unique = False,
        nullable = False
    )

    yValueDate = db.Column(
        db.String,
        unique = True,
        nullable = False
    )

    def serialize(self):
        return {
            'currency': self.currency,
            'xValue-Rate': self.xValueRate,
            'yValue-Date': self.yValueDate
        }
