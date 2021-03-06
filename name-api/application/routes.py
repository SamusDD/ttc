from application import app
from flask import jsonify
from random import choice

names = ['CaptainAmerica', 'IronMan', 'TheHulk', 'DoctorDoom', 'Thor']


@app.route('/get-name', methods=['GET'])
def get_name():
    name = choice(names)
    return jsonify(name=name)