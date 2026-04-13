#!/usr/bin/env python3
"""
Simple Flask proxy for OpenAI Chat API for the local AI Travel Guide.

SECURITY NOTE: Do NOT hard-code your OpenAI API key in this file. Set the
OPENAI_API_KEY environment variable on the server where this runs.

Example (Windows PowerShell):
  $env:OPENAI_API_KEY = "sk-..."
  python api.py

This file intentionally reads the key from the environment and provides a
single /api/chat POST endpoint that the frontend (destinations.html) can
call. It forwards the request to OpenAI and returns the assistant reply.

Do not commit secrets to the repository.
"""

import os
import json
from flask import Flask, request, jsonify
from flask_cors import CORS
import requests

OPENAI_API_KEY = os.environ.get('OPENAI_API_KEY')
OPENAI_MODEL = os.environ.get('OPENAI_MODEL', 'gpt-3.5-turbo')

app = Flask(__name__)
CORS(app)  # allow all origins for local development; restrict in production


def call_openai_chat(messages, temperature=0.7, max_tokens=512):
    """Call OpenAI Chat Completions API and return assistant text.

    messages: list of {role: 'system'|'user'|'assistant', 'content': '...'}

    """
    if not OPENAI_API_KEY:
        raise ValueError("OPENAI_API_KEY environment variable not set")

    url = "https://api.openai.com/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {OPENAI_API_KEY}",
        "Content-Type": "application/json"
    }
    payload = {
        "model": OPENAI_MODEL,
        "messages": messages,
        "temperature": temperature,
        "max_tokens": max_tokens
    }

    resp = requests.post(url, headers=headers, json=payload, timeout=30)
    resp.raise_for_status()
    data = resp.json()

    # Defensive extraction
    return data.get('choices', [{}])[0].get('message', {}).get('content', '')


@app.route('/api/chat', methods=['POST'])
def chat():
    """Proxy endpoint for OpenAI chat completions."""
    try:
        data = request.get_json()
        messages = data.get('messages', [])
        temperature = data.get('temperature', 0.7)
        max_tokens = data.get('max_tokens', 512)

        reply = call_openai_chat(messages, temperature, max_tokens)
        return jsonify({"reply": reply})

    except ValueError as e:
        return jsonify({"error": str(e)}), 400
    except requests.exceptions.RequestException as e:
        return jsonify({"error": f"API request failed: {str(e)}"}), 502
    except Exception as e:
        return jsonify({"error": f"Internal server error: {str(e)}"}), 500


if __name__ == '__main__':
    print("Starting OpenAI API proxy on http://localhost:5001")
    print("Make sure OPENAI_API_KEY environment variable is set!")
    app.run(host="0.0.0.0", port=5001, debug=True)
