from flask import Flask, Response, render_template
from chessdotcom import get_player_stats
from chessdotcom import Client
from dotenv import load_dotenv
import os

load_dotenv()

def rating(time_control):
    username = os.getenv("username")
    response = get_player_stats(username)
    
    if time_control == "blitz":
        time_control = "chess_blitz"
    elif time_control == "rapid":
        time_control = "chess_rapid"
    elif time_control == "bullet":
        time_control = "chess_bullet"

    if time_control:
        return response.json['stats'][time_control]['last']['rating']
    
    return [response.json['stats']['tactics']['highest']['rating'], response.json['stats']['tactics']['lowest']['rating']]

def generate_card():
    time_control = os.getenv("time_control")
    rating_level = os.getenv("rating_level")
    elo = rating(time_control)
    
    if time_control == "chess_blitz":
        time_control = "Chess.com Blitz"
    elif time_control == "chess_rapid":
        time_control = "Chess.com Rapid"
    elif time_control == "chess_bullet":
        time_control = "Chess.com Bullet"
    else:
        time_control = "Rating"

    if rating_level == "highest":
        elo = elo[0]
    elif rating_level == "lowest":
        elo = elo[1]
    else:
        elo = elo[0]

    svg = render_template(
        "card.html.j2",
        time_control = time_control,
        elo = elo
    )

    return svg

app = Flask(__name__)

@app.route("/")
def handle_all():
    svg = generate_card()
    resp = Response(svg, mimetype="image/svg+xml")
    resp.headers["Cache-Control"] = "s-maxage=1"

    return resp

if __name__ == "__main__":
    app.run(debug=True)
