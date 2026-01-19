# Flask Real Estate Website (Structured)

# Folder structure:
# flask_real_estate/
# ├── app.py
# ├── templates/
# │   └── home.html
# └── static/
#     └── style.css

# app.py
from flask import Flask, render_template, request

app = Flask(__name__)

# Sample property data
PROPERTIES = [
    {
        "id": 1,
        "title": "Modern 2-Bedroom Condo",
        "price": 1200000,
        "location": "Singapore",
        "type": "Condo",
        "image": "https://via.placeholder.com/400x250",
        "description": "Near MRT, fully furnished, great view"
    },
    {
        "id": 2,
        "title": "Landed House with Garden",
        "price": 3500000,
        "location": "Singapore",
        "type": "Landed",
        "image": "https://via.placeholder.com/400x250",
        "description": "Quiet neighborhood, large space"
    }
]

@app.route("/")
def home():
    q = request.args.get("q", "").lower()
    t = request.args.get("type", "")

    filtered = [p for p in PROPERTIES
                if (q in p["location"].lower() or not q)
                and (p["type"] == t or not t)]

    return render_template("home.html", properties=filtered, request=request)

if __name__ == "__main__":
    app.run(debug=True)


