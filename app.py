from flask import Flask, Response, render_template
from chessdotcom import get_player_stats
from chessdotcom import Client
from dotenv import load_dotenv
import os

load_dotenv()

Client.request_config["headers"]["User-Agent"] = (
    "Chess.com Github ReadMe Badge, Contact me at {}".format(email)
)

def rating(time_control):
    username = os.getenv("username")
    response = get_player_stats(username)
    if time_control == "blitz":
        time_control = "chess_blitz"
    elif time_control == "rapid":
        time_control = "chess_rapid"
    elif time_control == "bullet":
        time_control = "chess_bullet"
    return response.json['stats'][time_control]['last']['rating']

def generate_card():
    time_control = os.getenv("time_control")
    elo = rating(time_control)
    if time_control == "chess_blitz":
        time_control = "Chess.com Blitz"
    elif time_control == "chess_rapid":
        time_control = "Chess.com Rapid"
    elif time_control == "chess_bullet":
        time_control = "Chess.com Bullet"

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
