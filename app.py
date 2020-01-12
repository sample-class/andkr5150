from flask import Flask, render_template
from mk_data import *

app = Flask(__name__)


@app.route('/')
def main():
    return render_template('index.html',
                             title=title,
                             subtitle=subtitle,
                             description=description,
                             tours=tours.items())


@app.route('/from/<direction>')
def direction(direction):
    departure = departures[direction]
    return render_template('direction.html',
                             departures=departures.items(),
                             departure=departure,
                             direction=direction,
                             tours=tours.items())


@app.route('/tours/<id>/')
def tour(id):
    id_tour = tours[int(id)]
    return render_template('tour.html',
                             title=id_tour['title'],
                             stars=id_tour['stars'],
                             country=id_tour['country'],
                             dep=departures[id_tour['departure']],
                             nights=id_tour['nights'],
                             picture=id_tour['picture'],
                             desc=id_tour['description'],
                             price=str(id_tour['price']))

app.run()
# if __name__ == '__main__':
#     app.run()

