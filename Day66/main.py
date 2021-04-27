from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
import random

app = Flask(__name__)

##Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


##Cafe TABLE Configuration
class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    seats = db.Column(db.String(250), nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    coffee_price = db.Column(db.String(250), nullable=True)

    def to_dict(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}


@app.route("/")
def home():
    return render_template("index.html")


## HTTP GET - Read Record
@app.route("/random")
def get_random_cafe():
    cafes = db.session.query(Cafe).all()
    random_cafe = random.choice(cafes)

    return jsonify(random_cafe.to_dict())


@app.route("/all")
def get_all_cafes():
    cafes = db.session.query(Cafe).all()
    print([cafe.to_dict() for cafe in cafes])
    return jsonify(cafes=[cafe.to_dict() for cafe in cafes])


@app.route("/search")
def search():
    search_location = request.args.get("loc").title()
    cafes = db.session.query(Cafe).filter_by(location=search_location).all()
    if cafes:
        return jsonify(cafes=[cafe.to_dict() for cafe in cafes])
    else:
        return jsonify(error={"Not Found": "Sorry, we don't have a cafe at that location."})


## HTTP POST - Create Record
def make_bool(val: int) -> bool:
    return bool(int(val))


@app.route("/add", methods=["POST"])
def post_new_cafe():
    new_cafe = Cafe(
        name=request.form.get("name"),
        map_url=request.form.get("map_url"),
        img_url=request.form.get("img_url"),
        location=request.form.get("loc"),
        has_sockets=make_bool(request.form.get("sockets")),
        has_toilet=make_bool(request.form.get("toilet")),
        has_wifi=make_bool(request.form.get("wifi")),
        can_take_calls=make_bool(request.form.get("calls")),
        seats=request.form.get("seats"),
        coffee_price= "£" + request.form.get("coffee_price"),
    )
    db.session.add(new_cafe)
    db.session.commit()
    return jsonify(response={"success": "Successfully added the new cafe."})


## HTTP PUT/PATCH - Update Record
@app.route("/update-price/<int:cafe_id>",methods=["PATCH"])
def update_price(cafe_id):
    cafe = db.session.query(Cafe).get(cafe_id)
    if cafe:
        new_price = "£" + request.args.get("new_price")
        cafe.coffee_price = new_price
        db.session.commit()

        return jsonify(response={"success": "Successfully updated the price"}),200
    else:
        return jsonify(error={"Error": "Could not update price"}),404

# HTTP DELETE - Delete Record
    book_id = 1
    book_to_delete = Book.query.get(book_id)
    db.session.delete(book_to_delete)
    db.session.commit()

@app.route("/report-closed/<int:cafe_id>",methods=["DELETE"])
def delete_cafe(cafe_id):
    api_key = "TopSecretAPIKey"

    cafe = db.session.query(Cafe).get(cafe_id)
    if cafe and request.args.get("api_key") == api_key:
        db.session.delete(cafe)
        db.session.commit()
        return jsonify(response={"success": "Successfully deleted cafe"}),200
    elif request.args.get("api_key") != api_key:
        return jsonify(error={"Error": "Sorry, that's not allowed."}),403
    else:
        return jsonify(error={"Error": "Could not find cafe"}),404



if __name__ == '__main__':
    app.run(debug=True)
