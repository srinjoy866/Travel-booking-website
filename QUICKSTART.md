# 🚀 Quick Start Guide - AI Travel Guide

## Getting Started in 5 Minutes

### Step 1: Install Dependencies

**Option A: Using Setup Script (Recommended for Windows)**
```powershell
.\setup.ps1
```

**Option B: Manual Setup**
```bash
# Create virtual environment
python -m venv .venv

# Activate virtual environment (Windows)
.venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### Step 2: Start the Backend Server

```bash
python server.py
```

You should see:
```
Starting AI Travel Guide API server on http://0.0.0.0:5000
 * Running on http://127.0.0.1:5000
```

### Step 3: Open the Website

**Option A: Direct File Access**
- Simply double-click `index.html` in your file explorer

**Option B: Using Local Server (Recommended)**
```bash
# In a new terminal window
python -m http.server 8080

# Then visit: http://localhost:8080
```

---

## Optional: Enable AI Chatbot Features

### Using Ollama (Free & Local)

1. **Download Ollama**: https://ollama.ai
2. **Install and start Ollama**
3. **Pull the AI model**:
   ```bash
   ollama pull phi3:mini
   ```
4. **Start Ollama server**:
   ```bash
   ollama serve
   ```
5. The chatbot will automatically work!

### Using OpenAI API (Optional)

1. Get API key from https://platform.openai.com
2. Create `.env` file:
   ```bash
   OPENAI_API_KEY=sk-your-key-here
   ```
3. Start the API proxy:
   ```bash
   python api.py
   ```

---

## Navigation Checklist

Test all pages are working:

- ✅ **Home Page** → `index.html`
- ✅ **Destinations** → `destinations.html`
- ✅ **Plan Trip** → `plan-trip.html`
- ✅ **Travel Tips** → `travel-tips.html`
- ✅ **About** → `about.html`

All navigation buttons and links are working!

---

## Features to Try

### 1. Search for Destinations
- Go to Destinations page
- Type any city/country name
- See detailed information with weather and maps

### 2. Generate AI Itineraries
- Search for a destination
- Click "Generate AI Itinerary"
- Get a personalized day-by-day plan

### 3. Chat with AI Assistant
- Click the robot icon (bottom-right)
- Ask travel questions
- Get instant answers

### 4. Plan Your Trip
- Use the 4-step trip planner
- Select dates and activities
- Generate custom itinerary

### 5. Browse Travel Tips
- Filter by category
- Read detailed advice
- Get weather-based suggestions

---

## Troubleshooting

### Chatbot not working?
- Make sure Ollama is running: `ollama serve`
- Check that the model is downloaded: `ollama pull phi3:mini`
- Verify server is running on port 5000

### Navigation broken?
- Clear browser cache
- Make sure all HTML files are in the same folder
- Check browser console for errors (F12)

### Weather not showing?
- Check internet connection
- Open-Meteo API is free and doesn't need a key
- Try refreshing the page

### Maps not loading?
- Check internet connection (Leaflet loads from CDN)
- Disable ad blockers temporarily
- Try a different browser

---

## Ready for GitHub?

Your project is now GitHub-ready! Just:

1. **Initialize git repo**:
   ```bash
   git init
   ```

2. **Add files**:
   ```bash
   git add .
   ```

3. **Commit**:
   ```bash
   git commit -m "Initial commit: AI Travel Guide"
   ```

4. **Push to GitHub**:
   ```bash
   git remote add origin https://github.com/yourusername/ai-travel-guide.git
   git push -u origin main
   ```

---

## Next Steps

- Customize `kb.json` with your travel knowledge
- Add more destinations to the HTML files
- Customize the Firebase configuration
- Deploy to Heroku/Railway for production
- Add your own branding and colors

---

**Enjoy building your AI Travel Guide! 🌍✈️**
