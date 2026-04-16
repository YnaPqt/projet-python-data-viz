from flask import Flask, request, jsonify
from src.models import Session, Player

app = Flask(__name__)


@app.route("/api/data")
def get_players():
    session= Session()

    query = session.query(Player)


    # Filtres
    country = request.args.get("country")
    if country:
        query = query.filter(Player.country == country)
    
    player_name = request.args.get("player_name")
    if player_name:
        query = query.filter(Player.player_name == player_name)

    players = query.all()

    data = [
        {
            "id":p.id,
            "player_name":p.player_name,
            "player_height":p.player_height,
            "player_weight":p.player_weight,

            "college":p.college,
            "country": p.country,
            "age":p.age,
            "team_abbreviation":p.team_abbreviation,

            "draft_year":p.draft_year,
            "draft_round ": p.draft_round,
            "draft_number":p.draft_number,
            "season":p.season,
            
            "games played":p.gp,
            "points":p.pts,
            "rebounds":p.reb,
            "assists":p.ast,
            "net_rating":p.net_rating,
            "usg_pct":p.usg_pct,
            "ts_pct":p.ts_pct,


        }
        for p in players
    ]

    return jsonify(data)

if __name__== "__main__":
    app.run(debug=True,port=5000)