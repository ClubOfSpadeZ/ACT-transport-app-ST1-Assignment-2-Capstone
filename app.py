from flask import Flask, render_template, url_for

ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

app = Flask('my_flask_app')

@app.route("/")
def map_created_in_view():
    stopsURL = url_for('static', filename='Bus_Stops.xml')
    return render_template("Index.html", stopsURL=stopsURL,)


if __name__ == "__main__":
    app.run(debug=True)
