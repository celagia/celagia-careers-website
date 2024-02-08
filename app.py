from flask import Flask, render_template

app = Flask(__name__)

JOBS = [{
    'id': 1,
    'title': 'Mountain Climber',
    'location': 'Cairngorms',
    'salary': '£30,000'
}, {
    'id': 2,
    'title': 'Group Hike Leader',
    'location': 'Lake District',
    'salary': '£40,000'
}, {
    'id': 3,
    'title': 'Scrambler',
    'location': 'Snowdonia',
    'salary': '£50,000'
}, {
    'id': 4,
    'title': 'Car Park Barista',
    'location': 'Peak District',
    'salary': '£26,000'
}]


@app.route("/")
def hello_world():
  return render_template('home.html', jobs=JOBS)


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
