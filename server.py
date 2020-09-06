from flask import Flask, render_template, request, redirect
import csv
app = Flask(__name__)
print(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/<string:page_name>')
def html(page_name):
    return render_template(page_name)


def write_to_csv(data, file_name):
    with open(file_name, 'a', newline='') as csv_file:
        print(data.values())
        writer = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(data.values())
        print('wrote successfully')


def write_to_file(data, file_name):
    file = open(file_name, 'a')
    file.csv_writer(str(data) + '\n')
    file.close()
    print('wrote successfully')


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_to_csv(data, 'database.csv')
            return redirect('/thenkyou.html')
        except:
            return "Did not sate to database"
    else:
        return 'something went wrong. Try again'


# render_template('login.html', error=error)
# @app.route('/about.html')
# def about():
#     return render_template("about.html")
#
#
# @app.route('/contact.html')
# def contact():
#     return render_template("contact.html")
#
#
# @app.route('/components.html')
# def components():
#     return render_template("components.html")
#
#
# @app.route('/index.html')
# def index():
#     return render_template("index.html")
#
#
# @app.route('/work.html')
# def work():
#     return render_template("works.html")
#
#


# print('1adr')

# @app.route('/blog')
# def blog():
#     return 'I am blog'
#
# @app.route('/<name_of_user>/<int:post_id>')
# def username(name_of_user=None, post_id=None):
#     return render_template("./index.html", name=name_of_user, post_id=post_id)
