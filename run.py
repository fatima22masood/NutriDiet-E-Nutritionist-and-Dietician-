from flask import Flask, render_template, request, redirect, url_for, session
from flask_sqlalchemy import SQLAlchemy
from fpdf import FPDF
import re
from forms import UserInfoForm
from flask import send_file, abort
import algo

app = Flask(__name__)
app.config["SECRET_KEY"] = "abcd"
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:@localhost/nutridieteshfa"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)


class UserLogin(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(20), nullable=False)
    password = db.Column(db.String(20), nullable=False)
    user_info = db.relationship("UserInfo", backref="user_login", uselist=False)
    diet_plan_model = db.relationship(
        "DietPlanModel", backref="user_login", uselist=False
    )


class UserInfo(db.Model):
    info_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    gender = db.Column(db.String(10), nullable=False)
    height = db.Column(db.Float, nullable=False)
    weight = db.Column(db.Float, nullable=False)
    phys_act = db.Column(db.String(50), nullable=False)
    id = db.Column(db.Integer, db.ForeignKey("user_login.id"), nullable=False)


class DietPlanModel(db.Model):
    plan_id = db.Column(db.Integer, primary_key=True)
    tdee = db.Column(db.Float, nullable=False)
    breakfast_Monday = db.Column(db.String(100), nullable=False)
    snack1_Monday = db.Column(db.String(100), nullable=False)
    lunch_Monday = db.Column(db.String(100), nullable=False)
    snack2_Monday = db.Column(db.String(100), nullable=False)
    dinner_Monday = db.Column(db.String(100), nullable=False)
    snack3_Monday = db.Column(db.String(100), nullable=False)
    breakfast_Tuesday = db.Column(db.String(100), nullable=False)
    snack1_Tuesday = db.Column(db.String(100), nullable=False)
    lunch_Tuesday = db.Column(db.String(100), nullable=False)
    snack2_Tuesday = db.Column(db.String(100), nullable=False)
    dinner_Tuesday = db.Column(db.String(100), nullable=False)
    snack3_Tuesday = db.Column(db.String(100), nullable=False)
    breakfast_Wednesday = db.Column(db.String(100), nullable=False)
    snack1_Wednesday = db.Column(db.String(100), nullable=False)
    lunch_Wednesday = db.Column(db.String(100), nullable=False)
    snack2_Wednesday = db.Column(db.String(100), nullable=False)
    dinner_Wednesday = db.Column(db.String(100), nullable=False)
    snack3_Wednesday = db.Column(db.String(100), nullable=False)
    breakfast_Thursday = db.Column(db.String(100), nullable=False)
    snack1_Thursday = db.Column(db.String(100), nullable=False)
    lunch_Thursday = db.Column(db.String(100), nullable=False)
    snack2_Thursday = db.Column(db.String(100), nullable=False)
    dinner_Thursday = db.Column(db.String(100), nullable=False)
    snack3_Thursday = db.Column(db.String(100), nullable=False)
    breakfast_Friday = db.Column(db.String(100), nullable=False)
    snack1_Friday = db.Column(db.String(100), nullable=False)
    lunch_Friday = db.Column(db.String(100), nullable=False)
    snack2_Friday = db.Column(db.String(100), nullable=False)
    dinner_Friday = db.Column(db.String(100), nullable=False)
    snack3_Friday = db.Column(db.String(100), nullable=False)
    breakfast_Saturday = db.Column(db.String(100), nullable=False)
    snack1_Saturday = db.Column(db.String(100), nullable=False)
    lunch_Saturday = db.Column(db.String(100), nullable=False)
    snack2_Saturday = db.Column(db.String(100), nullable=False)
    dinner_Saturday = db.Column(db.String(100), nullable=False)
    snack3_Saturday = db.Column(db.String(100), nullable=False)
    breakfast_Sunday = db.Column(db.String(100), nullable=False)
    snack1_Sunday = db.Column(db.String(100), nullable=False)
    lunch_Sunday = db.Column(db.String(100), nullable=False)
    snack2_Sunday = db.Column(db.String(100), nullable=False)
    dinner_Sunday = db.Column(db.String(100), nullable=False)
    snack3_Sunday = db.Column(db.String(100), nullable=False)
    id = db.Column(db.Integer, db.ForeignKey("user_login.id"), nullable=False)


@app.route("/")
@app.route("/login", methods=["GET", "POST"])
def login():
    msg = ""
    if (
        request.method == "POST"
        and "username" in request.form
        and "password" in request.form
    ):
        username = request.form["username"]
        password = request.form["password"]
        account = UserLogin.query.filter_by(
            username=username, password=password
        ).first()
        if account:
            session["loggedin"] = True
            session["id"] = account.id
            session["username"] = account.username
            msg = "Logged in successfully!"
            return render_template("index.html", msg=msg)
        else:
            msg = "Incorrect username / password!"
    return render_template("login.html", msg=msg)


@app.route("/logout")
def logout():
    session.pop("loggedin", None)
    session.pop("id", None)
    session.pop("username", None)
    return redirect(url_for("login"))


@app.route("/register", methods=["GET", "POST"])
def register():
    msg = ""
    if (
        request.method == "POST"
        and "username" in request.form
        and "password" in request.form
        and "email" in request.form
    ):
        email = request.form["email"]
        username = request.form["username"]
        password = request.form["password"]

        account = UserLogin.query.filter_by(username=username).first()
        if account:
            msg = "Account already exists!"
        elif not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            msg = "Invalid email address!"
        elif not re.match(r"[A-Za-z0-9]+", username):
            msg = "Username must contain only characters and numbers!"
        elif not username or not password or not email:
            msg = "Please fill out the form!"
        else:
            user_login = UserLogin(username=username, email=email, password=password)
            db.session.add(user_login)
            db.session.commit()

            # Get the id from the newly created UserLogin instance
            id = user_login.id

            msg = "You have successfully registered!"
    elif request.method == "POST":
        msg = "Please fill out the form!"

    return render_template("register.html", msg=msg)


@app.route("/index")
def index():
    return render_template("index.html")


@app.route("/home", methods=["GET", "POST"])
def home():
    form = UserInfoForm()
    if form.validate_on_submit():
        name = form.name.data
        weight = float(form.weight.data)
        height = float(form.height.data)
        age = int(form.age.data)
        gender = form.gender.data
        phys_act = form.physical_activity.data

        # Retrieve the logged-in user's ID from the session
        user_id = session.get("id")

        # Retrieve the UserLogin instance based on the ID
        user_login = UserLogin.query.get(user_id)

        # Create a new UserInfo instance for the user
        user_info = UserInfo(
            name=name,
            weight=weight,
            height=height,
            age=age,
            gender=gender,
            phys_act=phys_act,
            id=user_id,  # Assign the user_id directly to user_id
        )

        db.session.add(user_info)
        db.session.commit()

        tdee = algo.calc_tdee(name, weight, height, age, gender, phys_act)
        return redirect(url_for("result", tdee=tdee))

    return render_template("home.html", title="NutriDiet", form=form)


@app.route("/result", methods=["GET", "POST"])
def result():
    tdee = request.args.get("tdee")
    if tdee is None:
        return render_template("error.html", title="Error Page")

    tdee = float(tdee)
    diet_plan = {}

    days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    for day in days_of_week:
        breakfast = algo.bfcalc(tdee)
        snack1 = algo.s1calc(tdee)
        lunch = algo.lcalc(tdee)
        snack2 = algo.s2calc(tdee)
        dinner = algo.dcalc(tdee)
        snack3 = algo.s3calc(tdee)

        diet_plan[day] = {
            "breakfast": breakfast,
            "snack1": snack1,
            "lunch": lunch,
            "snack2": snack2,
            "dinner": dinner,
            "snack3": snack3,
        }

    user_login = UserLogin.query.get(session["id"])
    dietplan = DietPlanModel(
        tdee=tdee,
        breakfast_Monday=diet_plan["Monday"]["breakfast"],
        snack1_Monday=diet_plan["Monday"]["snack1"],
        lunch_Monday=diet_plan["Monday"]["lunch"],
        snack2_Monday=diet_plan["Monday"]["snack2"],
        dinner_Monday=diet_plan["Monday"]["dinner"],
        snack3_Monday=diet_plan["Monday"]["snack3"],
        breakfast_Tuesday=diet_plan["Tuesday"]["breakfast"],
        snack1_Tuesday=diet_plan["Tuesday"]["snack1"],
        lunch_Tuesday=diet_plan["Tuesday"]["lunch"],
        snack2_Tuesday=diet_plan["Tuesday"]["snack2"],
        dinner_Tuesday=diet_plan["Tuesday"]["dinner"],
        snack3_Tuesday=diet_plan["Tuesday"]["snack3"],
        breakfast_Wednesday=diet_plan["Wednesday"]["breakfast"],
        snack1_Wednesday=diet_plan["Wednesday"]["snack1"],
        lunch_Wednesday=diet_plan["Wednesday"]["lunch"],
        snack2_Wednesday=diet_plan["Wednesday"]["snack2"],
        dinner_Wednesday=diet_plan["Wednesday"]["dinner"],
        snack3_Wednesday=diet_plan["Wednesday"]["snack3"],
        breakfast_Thursday=diet_plan["Thursday"]["breakfast"],
        snack1_Thursday=diet_plan["Thursday"]["snack1"],
        lunch_Thursday=diet_plan["Thursday"]["lunch"],
        snack2_Thursday=diet_plan["Thursday"]["snack2"],
        dinner_Thursday=diet_plan["Thursday"]["dinner"],
        snack3_Thursday=diet_plan["Thursday"]["snack3"],
        breakfast_Friday=diet_plan["Friday"]["breakfast"],
        snack1_Friday=diet_plan["Friday"]["snack1"],
        lunch_Friday=diet_plan["Friday"]["lunch"],
        snack2_Friday=diet_plan["Friday"]["snack2"],
        dinner_Friday=diet_plan["Friday"]["dinner"],
        snack3_Friday=diet_plan["Friday"]["snack3"],
        breakfast_Saturday=diet_plan["Saturday"]["breakfast"],
        snack1_Saturday=diet_plan["Saturday"]["snack1"],
        lunch_Saturday=diet_plan["Saturday"]["lunch"],
        snack2_Saturday=diet_plan["Saturday"]["snack2"],
        dinner_Saturday=diet_plan["Saturday"]["dinner"],
        snack3_Saturday=diet_plan["Saturday"]["snack3"],
        breakfast_Sunday=diet_plan["Sunday"]["breakfast"],
        snack1_Sunday=diet_plan["Sunday"]["snack1"],
        lunch_Sunday=diet_plan["Sunday"]["lunch"],
        snack2_Sunday=diet_plan["Sunday"]["snack2"],
        dinner_Sunday=diet_plan["Sunday"]["dinner"],
        snack3_Sunday=diet_plan["Sunday"]["snack3"],
        id=user_login.id,
    )

    db.session.add(dietplan)
    db.session.commit()

    return render_template(
        "result.html", title="Result", diet_plan=diet_plan, tdee=tdee
    )


# Define a custom class for PDF generation
class PDF(FPDF):
    def header(self):
        self.set_font("Arial", "B", 12)
        self.cell(0, 10, "NutriDiet - Diet Plan", 0, 1, "C")

    def footer(self):
        self.set_y(-15)
        self.set_font("Arial", "I", 8)
        self.cell(0, 10, f"Page {self.page_no()}", 0, 0, "C")

    def chapter_title(self, title):
        self.set_font("Arial", "B", 12)
        self.cell(0, 10, title, 0, 1, "L")
        self.ln(5)

    def chapter_body(self, content):
        self.set_font("Arial", "", 12)
        self.multi_cell(0, 10, content)
        self.ln(10)


@app.route("/download", methods=["POST"])
def download():
    tdee = request.form.get("tdee")
    if not tdee:
        abort(404, "TDEE parameter is missing.")

    try:
        tdee = float(tdee)
    except ValueError:
        abort(404, "Invalid TDEE value.")

    # Retrieve the diet plan for the logged-in user ID
    user_id = session.get("id")
    diet_plan = DietPlanModel.query.filter_by(id=user_id).first()

    if not diet_plan:
        abort(404, "No diet plan found.")

    # Create a PDF with the diet plan content
    pdf = PDF()
    pdf.add_page()

    days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    for day in days_of_week:
        pdf.chapter_title(f"{day.capitalize()} Diet Plan")
        pdf.chapter_body(f"TDEE: {diet_plan.tdee}")
        pdf.chapter_title("Breakfast")
        pdf.chapter_body(getattr(diet_plan, f"breakfast_{day}"))
        pdf.chapter_title("Snack 1")
        pdf.chapter_body(getattr(diet_plan, f"snack1_{day}"))
        pdf.chapter_title("Lunch")
        pdf.chapter_body(getattr(diet_plan, f"lunch_{day}"))
        pdf.chapter_title("Snack 2")
        pdf.chapter_body(getattr(diet_plan, f"snack2_{day}"))
        pdf.chapter_title("Dinner")
        pdf.chapter_body(getattr(diet_plan, f"dinner_{day}"))
        pdf.chapter_title("Snack 3")
        pdf.chapter_body(getattr(diet_plan, f"snack3_{day}"))
        pdf.add_page()

    # Save the PDF to a temporary file
    filename = "diet_plan.pdf"
    pdf.output(filename)

    # Send the file for download
    return send_file(filename, as_attachment=True)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact", methods=["GET", "POST"])
def contact():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=True)
