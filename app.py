#!/usr/bin/env python3

from flask import Flask, render_template, request


app = Flask(__name__)


class Person:

    def __init__(self, username, first_name, last_name):
        self.username = username
        self.first_name = first_name
        self.last_name = last_name


DATA = {
    'justinnhli': Person('justinnhli', 'Justin', 'Li'),
    'kliu4': Person('kliu4', 'Kathy', 'Liu'),
    'aphillips2': Person('aphillips2', 'Alec', 'Phillips'),
    'clinscott': Person('clinscott', 'Chris', 'Linscott'),
}


@app.route('/form/', defaults={'username': None}, methods=('GET', 'POST'))
@app.route('/form/<username>', methods=('GET', 'POST'))
def form(username=None):
    print('form() called with username=' + str(username))
    if request.method == 'POST':
        print('form submitted with data:')
        print('   username = ' + request.form['username'])
        print('   first_name = ' + request.form['first_name'])
        print('   last_name = ' + request.form['last_name'])
    context = {}
    context['data'] = DATA
    return render_template('form.html', **context)


def main():
    app.run(debug=True)


if __name__ == '__main__':
    main()
