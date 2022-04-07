from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    users = [
        {'first_name' : 'Joe', 'last_name' : 'Mama'},
        {'first_name' : 'Karen', 'last_name' : 'Kate'},
        {'first_name' : 'Alma', 'last_name' : 'Walberg'},
        {'first_name' : 'Barack', 'last_name' : 'Obama'}
    ]
    return render_template("index.html",users=users)



if __name__=="__main__":
    app.run(debug=True)