import os
from datetime import datetime
from flask import Flask, render_template, request, jsonify

app = Flask(__name__, template_folder="../templates")

@app.get("/")
def home():
    return render_template("index.html")

@app.post("/submit")
def submit():
    name = request.form.get("name", "").strip()
    message = request.form.get("message", "").strip()

    if not name or not message:
        return render_template(
            "result.html",
            ok=False,
            error="Name dan Message must diisi!",
            name=name,
            message=message,
            timestamp=datetime.utcnow().isoformat() + "Z",
        ), 400
    
    return render_template(
        "result.html",
        ok=True,
        name=name,
        message=message,
        timestamp=datetime.utcnow().isoformat() + "Z",
    )

@app.get("/api/health")
def health():
    return jsonify(status="ok", service="basic-flask-apps")

@app.get("/api/info")
def info():
    return jsonify(
        app_name=os.environ.get("APP_NAME", "Basic Flask Apps"),
        environment=os.environ.get("VERCEL_ENV", "unknown"),
    )