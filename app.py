from flask import Flask, render_template, request, jsonify
from datetime import datetime

app = Flask(__name__)

# Edit these details to personalize your portfolio.
PROFILE = {
    "name": "Shubham Sarraf",
    "role": "Student Developer · Builder · Curious Mind",
    "location": "Nepal",
    "email": "your-email@example.com",
    "intro": (
        "I’m a student developer who enjoys turning ideas into useful software. "
        "I explore web development, Python, robotics, and AI by building projects "
        "and learning how things work under the hood."
    ),
    "github": "https://github.com/Mr-shroff",
    "linkedin": "",
}

PROJECTS = [
    {
        "number": "01",
        "name": "Shram Surakshya",
        "category": "AI · Social impact",
        "description": (
            "A concept for helping people verify foreign-employment agencies "
            "and report suspicious activity."
        ),
        "stack": ["Python", "Web", "AI"],
        "link": "https://github.com/Mr-shroff/Shram-Surakshya",
    },
    {
        "number": "02",
        "name": "Hand Gesture Controller",
        "category": "Computer vision · Hardware",
        "description": (
            "A hand-gesture project exploring camera input, landmark detection, "
            "and controlling outputs through gestures."
        ),
        "stack": ["Python", "MediaPipe", "Arduino"],
        "link": "https://github.com/Mr-shroff/hand-gesture-project",
    },
    {
        "number": "03",
        "name": "Ultrasonic Radar",
        "category": "Robotics · IoT",
        "description": (
            "An Arduino-based distance-detection project using an ultrasonic sensor, "
            "servo movement, LEDs, and a live radar-style interface."
        ),
        "stack": ["Arduino", "Python", "JavaScript"],
        "link": "",
    },
]

SKILLS = [
    ("Web", "HTML, CSS, JavaScript"),
    ("Programming", "Python, C"),
    ("Tools", "Git, GitHub, PowerShell"),
    ("Exploring", "Robotics, AI, cybersecurity"),
]

@app.get("/")
def home():
    return render_template(
        "index.html",
        profile=PROFILE,
        projects=PROJECTS,
        skills=SKILLS,
        year=datetime.now().year,
    )

@app.post("/api/contact")
def contact():
    """Demo contact endpoint. It validates input but does not send or store messages."""
    data = request.get_json(silent=True) or {}
    name = str(data.get("name", "")).strip()
    email = str(data.get("email", "")).strip()
    message = str(data.get("message", "")).strip()

    if not name or not email or not message:
        return jsonify(ok=False, error="Please complete every field."), 400
    if len(name) > 100 or len(email) > 254 or len(message) > 3000:
        return jsonify(ok=False, error="One of the fields is too long."), 400
    if "@" not in email or "." not in email.rsplit("@", 1)[-1]:
        return jsonify(ok=False, error="Please enter a valid email address."), 400

    # This starter intentionally does not email or persist contact messages.
    # Connect a trusted email provider or database when you are ready to deploy.
    app.logger.info("Portfolio contact form validated for %s <%s>", name, email)
    return jsonify(
        ok=True,
        message="Thanks! The demo form works, but it does not send or save messages yet."
    )

if __name__ == "__main__":
  app.run(host="0.0.0.0", port=5000, debug=True)