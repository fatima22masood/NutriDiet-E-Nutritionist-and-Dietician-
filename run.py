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


class Contact(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(20), nullable=False)
    phone_num = db.Column(db.String(12), nullable=False)
    msg = db.Column(db.String(80), nullable=False)
    date = db.Column(db.String, nullable=False)


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
    breakfast = db.Column(db.String(100), nullable=False)
    snack1 = db.Column(db.String(100), nullable=False)
    lunch = db.Column(db.String(100), nullable=False)
    snack2 = db.Column(db.String(100), nullable=False)
    dinner = db.Column(db.String(100), nullable=False)
    snack3 = db.Column(db.String(100), nullable=False)
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
        gender = request.form["gender"]
        phys_act = request.form["physical_activity"]

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
            id=user_id,  # Assign the user_id directly to id
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
    breakfast = algo.bfcalc(tdee)
    snack1 = algo.s1calc(tdee)
    lunch = algo.lcalc(tdee)
    snack2 = algo.s2calc(tdee)
    dinner = algo.dcalc(tdee)
    snack3 = algo.s3calc(tdee)

    user_login = UserLogin.query.get(session["id"])
    dietplan = DietPlanModel(
        tdee=tdee,
        breakfast=breakfast,
        snack1=snack1,
        lunch=lunch,
        snack2=snack2,
        dinner=dinner,
        snack3=snack3,
        id=user_login.id,
    )

    db.session.add(dietplan)
    db.session.commit()

    return render_template(
        "result.html",
        title="Result",
        breakfast=breakfast,
        snack1=snack1,
        lunch=lunch,
        snack2=snack2,
        dinner=dinner,
        snack3=snack3,
        tdee=tdee,
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

    # Retrieve the diet plans for the user ID
    user_login = UserLogin.query.get(session["id"])
    diet_plans = DietPlanModel.query.filter_by(id=user_login.id).all()

    if not diet_plans:
        abort(404, "No diet plans found.")

    # Create a PDF with the diet plan content
    pdf = PDF()
    pdf.add_page()

    for diet_plan in diet_plans:
        breakfast = diet_plan.breakfast
        snack1 = diet_plan.snack1
        lunch = diet_plan.lunch
        snack2 = diet_plan.snack2
        dinner = diet_plan.dinner
        snack3 = diet_plan.snack3

        pdf.chapter_title("Diet Plan")
        pdf.chapter_body(f"TDEE: {diet_plan.tdee}")
        pdf.chapter_title("Breakfast")
        pdf.chapter_body(breakfast)
        pdf.chapter_title("Snack 1")
        pdf.chapter_body(snack1)
        pdf.chapter_title("Lunch")
        pdf.chapter_body(lunch)
        pdf.chapter_title("Snack 2")
        pdf.chapter_body(snack2)
        pdf.chapter_title("Dinner")
        pdf.chapter_body(dinner)
        pdf.chapter_title("Snack 3")
        pdf.chapter_body(snack3)
        pdf.add_page()

    # Save the PDF to a temporary file
    filename = "diet_plans.pdf"
    pdf.output(filename)

    # Send the file for download
    return send_file(filename, as_attachment=True)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        phone_num = request.form.get("phone_num")
        msg = request.form.get("msg")

        entry = Contact(name=name, phone_num=phone_num, msg=msg, email=email)
        db.session.add(entry)
        db.session.commit()

    return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=True)
