from application import app
from flask import request, jsonify

statistics = dict(CaptainAmerica='ShieldSlam', IronMan='CombatSuit', TheHulk='SMASH', DoctorDoom='DoomAndGloom', Thor='TastemyLightning!')

@app.route('/stats', methods=['POST'])
def stats():
    name_json = request.get_json()
    name = name_json["name"]
    return jsonify(stat=statistics[name])