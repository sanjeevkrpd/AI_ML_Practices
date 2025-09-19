# from flask import Flask, request, render_template

# app = Flask(__name__)

# @app.route("/")
# def index():
#     return render_template("index.html")

# @app.route("/submit", methods=["POST"])
# def submit():
#     maths = int(request.form["maths"])
#     science = int(request.form["science"])
#     sst = int(request.form["sst"])
#     english = int(request.form["english"])
#     hindi = int(request.form["hindi"])

#     total = maths + science + sst + english + hindi
#     percentage = round(total / 5, 2)

#     if percentage >= 90:
#         grade = "A+"
#     elif percentage >= 75:
#         grade = "A"
#     elif percentage >= 60:
#         grade = "B"
#     elif percentage >= 45:
#         grade = "C"
#     else:
#         grade = "Fail"

#     return render_template("result.html", total=total, percentage=percentage, grade=grade)

# if __name__ == "__main__":
#     app.run(debug=True)



from flask import Flask


app = Flask(__name__)

@app.route("/")
def index():
    return "hello python"



@app.route("/login")
def login():
    return "login page"

if __name__=="__main__":
    app.run()