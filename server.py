from flask import Flask, request, jsonify
from flask_cors import CORS
import ollama
import json

app = Flask(__name__)
CORS(app)  # allow all origins


# ------------------ COMMON OLLAMA FUNCTION ------------------ #
def ask_ollama(messages):
    try:
        response = ollama.chat(
            model='phi3:mini',
            messages=messages
        )
        return response['message']['content']
    except Exception as e:
        print("Ollama Error:", e)
        return "AI server error. Please try again."


# ------------------ CHATBOT (USED BY BOTH PAGES) ------------------ #
@app.route('/chat', methods=['POST'])
def chat():
    try:
        data = request.get_json()
        user_message = data.get("message", "")
        preferences = data.get("preferences", {})

        prompt = f"""
User Message: {user_message}

Preferences:
- Interests: {preferences.get('interests')}
- Budget: {preferences.get('budget')}
- Style: {preferences.get('style')}

Give a helpful travel-related response.
Keep it simple and friendly.
"""

        reply = ask_ollama([
            {"role": "system", "content": "You are an expert travel assistant."},
            {"role": "user", "content": prompt}
        ])

        return jsonify({"reply": reply})

    except Exception as e:
        print("CHAT ERROR:", e)
        return jsonify({"reply": "Server error occurred."})


# ------------------ AI RECOMMENDATIONS ------------------ #
@app.route('/recommendations', methods=['POST'])
def recommendations():
    try:
        data = request.get_json()
        preferences = data.get("preferences", {})

        prompt = f"""
User Preferences:
- Interests: {preferences.get('interests')}
- Budget: {preferences.get('budget')}
- Style: {preferences.get('style')}

Suggest 4 travel destinations.

Return ONLY JSON:
[
  {{
    "name": "Place",
    "reason": "Why recommended",
    "match": 90,
    "image": "https://source.unsplash.com/featured/?place"
  }}
]
"""

        result = ask_ollama([
            {"role": "user", "content": prompt}
        ])

        try:
            parsed = json.loads(result)
        except:
            parsed = []

        return jsonify(parsed)

    except Exception as e:
        print("RECOMMENDATION ERROR:", e)
        return jsonify([])


# ------------------ AI ITINERARY ------------------ #
@app.route('/itinerary', methods=['POST'])
def itinerary():
    try:
        data = request.get_json()
        destination = data.get("destination", "your destination")
        days = int(data.get("days", 3))

        prompt = f"""
Create a {days}-day travel itinerary for {destination}.

Return ONLY a valid JSON array with exactly {days} objects. Each object must have "title" and "activities" keys.

Format example:
[
  {{
    "title": "Day 1: Arrival",
    "activities": [
      {{
        "title": "Check into hotel",
        "description": "Rest after travel",
        "icon": "fa-bed"
      }}
    ]
  }}
]

Do not include any text outside the JSON.
"""

        result = ask_ollama([
            {"role": "user", "content": prompt}
        ])

        print(f"Raw itinerary response: {result}")

        try:
            parsed = json.loads(result)
            if isinstance(parsed, list) and len(parsed) == days:
                return jsonify(parsed)
        except:
            pass

        # Try to extract JSON from response
        import re
        json_match = re.search(r'\[.*\]', result, re.DOTALL)
        if json_match:
            try:
                parsed = json.loads(json_match.group(0))
                if isinstance(parsed, list):
                    return jsonify(parsed)
            except:
                pass

        # Fallback
        fallback = []
        for i in range(1, days + 1):
            fallback.append({
                "title": f"Day {i}: Explore {destination}",
                "activities": [
                    {"title": "Visit local attractions", "description": f"Discover the highlights of {destination}", "icon": "fa-map-marker-alt"},
                    {"title": "Try local cuisine", "description": f"Enjoy authentic food in {destination}", "icon": "fa-utensils"}
                ]
            })
        return jsonify(fallback)

    except Exception as e:
        print("ITINERARY ERROR:", e)
        return jsonify([])


# ------------------ SMART SEARCH ------------------ #
@app.route('/smart-search', methods=['POST'])
def smart_search():
    try:
        data = request.get_json()
        query = data.get("query", "")

        prompt = f"""
User query: {query}

Give short travel insights, tips, and best places.
"""

        reply = ask_ollama([
            {"role": "user", "content": prompt}
        ])

        return jsonify({"reply": reply})

    except Exception as e:
        print("SMART SEARCH ERROR:", e)
        return jsonify({"reply": "Error fetching results"})


# ------------------ SERVER RUN ------------------ #
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)