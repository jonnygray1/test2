from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)

friend_list = [
    {"name": "Test", "flavor": "swirl", "read": "yes", "activities": "reading"}
]


@app.route("/", methods=["GET", "POST"])
def index():
    return render_template(
        "index.html", pageTitle="Web form template", friends=friend_list
    )

@app.route("/about", methods=["GET", "POST"])
def about():
    return render_template(
        "about.html", pageTitle="Web form template"
    )



@app.route("/add", methods=["POST"])
def add():
    print("inside add function")
    if request.method == "POST":

        form = request.form

        fname = form["fname"]
        flavor = form["flavor"]
        read = form["read"]
       
        activities=form.getlist("activities")
        print(fname)
        print(flavor)
        print(read)
        print(activities)
        activities_string = ", ".join(activities)  # make the Python list into a string
        print(activities_string)
        friend_dict = {
    
            "name": fname,
            "flavor": flavor,
            "read": read,
            "activities": activities_string,
        }
        print(friend_dict)
        friend_list.append(friend_dict)
        print(friend_list)
        return redirect(url_for("index"))
    else:
        return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True)

# Handling error 404 and displaying relevant web page
@app.errorhandler(404)
def not_found_error(error):
    return render_template("404.html"), 404

# Handling error 500 and displaying relevant web page
@app.errorhandler(500)
def internal_error(error):
    return render_template("500.html"), 500

# Define a list to store the data from the form
data_list = []

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Get the data from the form
        fname = request.form["name"]
        flavor = request.form["flavor"]
        read = request.form["read"]

        # Create a dictionary to store the data
        data_dict = {
            'name': fname,
            'flavor': flavor,
            'read': read
        }

        # Append the dictionary to the list
        data_list.append(data_dict)

        # Return a message to indicate that the data was successfully added
        return 'Data added to list!'
    else:
        return render_template('index.html')