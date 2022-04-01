import os
from flask import (
    Flask,
    render_template,
    request,
    redirect,
    url_for,
    flash,
    Blueprint,
    jsonify,
    json,
)
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv, find_dotenv
from flask_login import (
    LoginManager,
    UserMixin,
    login_user,
    login_required,
    logout_user,
    current_user,
)
from tmdb import get_movie_data

load_dotenv(find_dotenv())

app = Flask(__name__)

# set up a separate route to serve the index.html file generated
bp = Blueprint(
    "bp",
    __name__,
    template_folder="./static/react",
)

# Point SQLAlchemy to your Heroku database
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
# Gets rid of a warning
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
# Get secret key for sessions and flash messages
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")

db = SQLAlchemy(app)

# Login_manager for flask-login
login_manager = LoginManager()
login_manager.init_app(app)

# ---------------------------------------------------------------------------
# DATABASE MODELS
# ---------------------------------------------------------------------------

# Create a database table with id and username for login
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(120))


# Create a database table with id, username, MovieID,rate, and comment for review.
class Review(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120))
    movieID = db.Column(db.String(80))
    rate = db.Column(db.String(80))
    comment = db.Column(db.String(120))


db.create_all()

# ---------------------------------------------------------------------------
# REACT ROUTES
# ---------------------------------------------------------------------------

# route for serving React profile page
@bp.route("/profile")
@login_required
def index():
    return render_template("index.html")


# converts review object into JSON data
def review_serializer(review):

    return {
        "id": review.id,
        "name": review.name,
        "movieID": review.movieID,
        "rate": review.rate,
        "comment": review.comment,
    }


# get and display review data
@app.route("/MovieData", methods=["GET"])
def display_reviews():
    return jsonify(
        [
            *map(
                review_serializer,
                Review.query.filter_by(name=current_user.username).all(),
            )
        ]
    )


# delete review data based on id
@app.route("/MovieData/<int:id>", methods=["POST"])
def delete_review(id):
    request_data = json.loads(request.data)
    Review.query.filter_by(id=request_data["id"]).delete()
    db.session.commit()
    return {"204": "Updated successfully"}


# update review data based on id
@app.route("/MovieData/<int:id>", methods=["PUT"])
def update_review(id):
    review = Review.query.get(id)
    rate = request.json["rate"]

    if rate:
        review.rate = rate

    comment = request.json["comment"]
    if comment:
        review.comment = comment

    db.session.commit()

    return {"200": "Updated successfully"}


# ---------------------------------------------------------------------------
# LOGIN/REGISTER FUNCTIONS
# ---------------------------------------------------------------------------

# User loader callback to reload user ID stored in the session
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


# Login form - checks if a user is in the database
@app.route("/", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        data = request.form.get("username")
        user = User.query.filter_by(username=data).first()
        # If user is in the database login user and redirect to dashboard.
        if user:
            login_user(user)
            return redirect(url_for("dashboard"))
        # else flash wrong username and render login page
        else:
            flash("Wrong Username. Check your login details and try again!")
            return render_template("login.html")

    return render_template("login.html")


# register form - adds new user to database
@app.route("/register", methods=["GET", "POST"])
def register():
    # If method is post create a new User object and add it to the table.
    if request.method == "POST":
        data = request.form.get("username")
        new_user = User(username=data)
        db.session.add(new_user)
        db.session.commit()
        # redirect to login page
        return redirect(url_for("login"))

    return render_template("register.html")


# logs out the user from the session - login required to access this page
@app.route("/logout")
@login_required
def logout():
    logout_user()
    return render_template("logout.html")


# ---------------------------------------------------------------------------
# MAIN PAGE
# ---------------------------------------------------------------------------

# dashboard with movie data - login required to access this page
@app.route("/dashboard", methods=["GET", "POST"])
@login_required
def dashboard():
    title, genre, tagline, poster, wiki_url, id = get_movie_data()
    # If method is post create a new Review object and add it to the table.
    if request.method == "POST":

        new_review = Review(
            name=current_user.username,
            movieID=request.form.get("movieID"),
            rate=request.form.get("rate"),
            comment=request.form.get("comment"),
        )
        db.session.add(new_review)
        db.session.commit()
        return redirect(url_for("dashboard"))

    # Query all the table content and render the dashboard page
    reviews = Review.query.filter_by(movieID=id).all()
    num_reviews = len(reviews)

    return render_template(
        "dash.html",
        title=title,
        genre=genre,
        tagline=tagline,
        poster=poster,
        wiki_url=wiki_url,
        id=id,
        name=current_user.username,
        reviews=reviews,
        num_reviews=num_reviews,
    )


app.register_blueprint(bp)

app.run()
