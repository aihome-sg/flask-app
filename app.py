# Flask Real Estate Website – Singapore Listings

# Folder structure:
# flask_real_estate/
# ├── app.py
# ├── templates/
# │   └── home.html
# └── static/
#     └── style.css

# =====================
# app.py
# =====================
from flask import Flask, render_template, request

app = Flask(__name__)

# Singapore property sample data
PROPERTIES = [
    {
        "id": 1,
        "title": "4-Room HDB at Bishan",
        "price": 780000,
        "district": "Bishan",
        "type": "HDB",
        "image": "https://via.placeholder.com/400x250",
        "description": "High floor, near MRT, renovated"
    },
    {
        "id": 2,
        "title": "2-Bedroom Condo at Bugis",
        "price": 1450000,
        "district": "Bugis",
        "type": "Condo",
        "image": "https://via.placeholder.com/400x250",
        "description": "City fringe, pool & gym"
    },
    {
        "id": 3,
        "title": "Landed Terrace at Serangoon",
        "price": 3200000,
        "district": "Serangoon",
        "type": "Landed",
        "image": "https://via.placeholder.com/400x250",
        "description": "Quiet estate, 2-storey"
    }
]

@app.route("/")
def home():
    q = request.args.get("q", "").lower()
    t = request.args.get("type", "")

    filtered = [p for p in PROPERTIES
                if (q in p["district"].lower() or not q)
                and (p["type"] == t or not t)]

    return render_template("home.html", properties=filtered, request=request)

if __name__ == "__main__":
    app.run(debug=True)







