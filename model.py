from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def connect_db(app):
    db.app = app
    db.init_app(app)


class EURData(db.Model):
    __tablename__ = "eur"

    id = db.Column(db.Integer,
        primary_key=True,
        autoincrement=True)

    currency = db.Column(
        db.String,
        default="eur",
        unique= False,
        nullable = False)

    apiTimestamp = db.Column(
        db.String,
        unique = False,
        nullable = False)

    xValueRate = db.Column(
        db.Integer,
        unique = False,
        nullable = False)

    yValueTime = db.Column(
        db.String,
        unique = True,
        nullable = False)

    def serialize(self):
        return {
            'currency': self.currency,
            'apiTimestamp': self.apiTimestamp,
            'xValueRate': self.xValueRate,
            'yValueTime': self.yValueTime
        }



class USDData(db.Model):
    __tablename__ = "usd"

    id = db.Column(db.Integer,
        primary_key=True,
        autoincrement=True)

    currency = db.Column(
        db.String,
        default="usd",
        unique= False,
        nullable = False)

    apiTimestamp = db.Column(
        db.String,
        unique = False,
        nullable = False)

    xValueRate = db.Column(
        db.Integer,
        unique = False,
        nullable = False)

    yValueTime = db.Column(
        db.String,
        unique = True,
        nullable = False)

    def serialize(self):
        return {
            'currency': self.currency,
            'apiTimestamp': self.apiTimestamp,
            'xValueRate': self.xValueRate,
            'yValueTime': self.yValueTime
        }


class GBPData(db.Model):
    __tablename__ = "gbp"

    id = db.Column(db.Integer,
        primary_key=True,
        autoincrement=True)

    currency = db.Column(
        db.String,
        default="gpb",
        unique= False,
        nullable = False)

    apiTimestamp = db.Column(
        db.String,
        unique = False,
        nullable = False)

    xValueRate = db.Column(
        db.Integer,
        unique = False,
        nullable = False)

    yValueTime = db.Column(
        db.String,
        unique = True,
        nullable = False)
        
    def serialize(self):
        return {
            'currency': self.currency,
            'apiTimestamp': self.apiTimestamp,
            'xValueRate': self.xValueRate,
            'yValueTime': self.yValueTime
        }