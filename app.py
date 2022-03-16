# from crypt import methods
# from urllib import request
from flask import request,Flask
from flask_sqlalchemy import *
import datetime
# from jsonify import json
# from stripe_api import *
# from config import *
import hashlib
# from dp import backend


app = Flask(__name__)
# app.config["SQLALCHEMY_DATABASE_URI"]="sqlite:///test.db";
# app.config["SQLALCHEMY_DATABASE_URI"] = 'mysql://root:@localhost/testing'
app.config["SQLALCHEMY_DATABASE_URI"] = 'postgres://btgenrxmkacrcl:87d95f26a64a1a8040d72fc7f225effeb8d7d0a5f344c2db26bfe5c6f1df5bc5@ec2-3-219-63-251.compute-1.amazonaws.com:5432/da7d8gda18qasj'
app.config[" SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.secret_key= "dharmeshmohanbhaipatel_1801"

db = SQLAlchemy(app)
# name="asa"
# email="asa"
# password="asa"
# mobile="asas"


class Usertable(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), primary_key=False)
    email = db.Column(db.String(100), primary_key=False, nullable=False)
    password = db.Column(db.String(100), primary_key=False, nullable=False)
    mobile = db.Column(db.String, primary_key=False, nullable=False)

    def __repr__(self):
        return f"{self.sno}-|-{self.name}\n"


# @app.route("/payment")
# def payment():


#     stripe.issuing.Transaction.retrieve(
#     "po_1KVmqKSE4LGeWcqjQeu32xwt",
# )
#     return render_template("success.html", title="payments")


@app.route("/", methods=["GET", "POST"])
def Usertable_view():
    # print(l["charges"]["data"][0]["name"])

    # name=request.form["nm"];
    # email=request.form["email"]
    # password=request.form["password"]
    # mobile=request.form["mobile"]
    # strToday = "2020-02-01"
    # dateToday = datetime.datetime.strptime(strToday, '%Y-%m-%d')
    # print(dateToday)
    if (request.method == "POST"):
        # print()
        name = request.form.get("name")
        # print(request.form.get(("name"), ("email")))
        email = request.form.get("email")
        # dummy = request.form
        # print(request.json)

        # emailExists=Usertable.query.filter_by(email=email).first();
        # print(emailExists)
        # if emailExists:
        #     redirect("/")
        #     return "<script>alert('email already exist')</script>"
        password = request.form.get("password")
        # print(password)
        mobile = request.form.get("mobile")
        # print(name)
        # print(request.POST.get('name', False))
        # request.po
        # global name,email,password,mobile
        # password = 'pa$$w0rd'
        hashPassword = hashlib.md5(password.encode())
        # print(hashPassword.hexdigest())
        # print()
        user = Usertable(name=name, email=email,
                         password=hashPassword.hexdigest(), mobile=mobile)
        db.session.add(user)
        db.session.commit()
    return render_template("index.html", title="Registration")


@app.route("/show")
def showUser():

    allUsers = Usertable.query.all()
    print(type(allUsers))
    return render_template("user.html", user=allUsers, title="Show")


@app.route("/delete/<int:sno>")
def deleteUser(sno):
    allUsers = Usertable.query.filter_by(sno=sno).first()

    db.session.delete(allUsers)
    db.session.commit()
    return redirect("/show")


@app.route("/update/<int:sno>", methods=["POST", "GET"])
def update(sno):
    if(request.method == "POST"):
        name = request.form.get("name")
        email = request.form.get("email")
        # emailExists=
        password = request.form.get("password")
        mobile = request.form.get("mobile")
        allUsers = Usertable.query.filter_by(sno=sno).first()
        allUsers.name = name
        allUsers.email = email
        allUsers.password = password
        allUsers.mobile = mobile

        db.session.add(allUsers)
        db.session.commit()
        return redirect('/show')
    allUsers = Usertable.query.filter_by(sno=sno).first()
    return render_template("update.html", allUsers=allUsers, title="Update")


if __name__ == '__main__':
    app.run()
