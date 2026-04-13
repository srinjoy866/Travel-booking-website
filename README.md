# 🌍 AI Travel Guide

A professional, AI-powered travel planning web application with personalized recommendations, smart itineraries, and real-time travel assistance.

![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Python](https://img.shields.io/badge/python-3.8+-blue.svg)
![Flask](https://img.shields.io/badge/flask-2.0+-green.svg)

---

## ✨ Features

### 🤖 AI-Powered Capabilities
- **Smart Recommendations** - AI analyzes traveler reviews and preferences to suggest perfect destinations
- **Personalized Itineraries** - Custom day-by-day travel plans based on your interests and budget
- **AI Travel Assistant** - Chat with an intelligent bot for instant travel advice and information
- **Landmark Recognition** - Upload photos to identify landmarks and get information
- **Real-time Updates** - Live weather alerts and event notifications

### 🎨 User Experience
- **Responsive Design** - Works seamlessly on desktop, tablet, and mobile
- **Dark Mode** - Built-in theme toggle for comfortable viewing
- **Multi-language Support** - Interface available in English, Spanish, French, and German
- **User Authentication** - Secure sign-in via Firebase (email, Google, Facebook, Twitter)
- **Saved Destinations** - Bookmark and manage your favorite travel destinations

### 🗺️ Travel Planning
- **Interactive Maps** - Explore destinations with Leaflet-based mapping
- **Points of Interest** - Discover nearby hotels, restaurants, and attractions
- **Weather Integration** - Real-time weather data and forecasts
- **Activity Discovery** - AI-curated activities based on your preferences
- **Budget Planning** - Tools to plan and track travel expenses

---

## 🚀 Quick Start

### Prerequisites
- Python 3.8 or higher
- Modern web browser (Chrome, Firefox, Safari, Edge)
- (Optional) Ollama for AI chatbot features

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/ai-travel-guide.git
   cd ai-travel-guide
   ```

2. **Install Python dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Start the backend server**
   ```bash
   python server.py
   ```
   The API server will start on `http://localhost:5000`

4. **Open the application**
   - Simply open `index.html` in your web browser
   - Or use a local server: `python -m http.server 8080`
   - Visit `http://localhost:8080`

---

## 🤖 AI Chatbot Setup

The application includes an AI-powered travel assistant. You have two options:

### Option 1: Ollama (Recommended - Free & Local)

1. **Install Ollama**: https://ollama.ai
2. **Pull the Phi-3 model**:
   ```bash
   ollama pull phi3:mini
   ```
3. **Start Ollama server**:
   ```bash
   ollama serve
   ```
4. The chatbot will automatically connect to your local Ollama instance

### Option 2: OpenAI API (Optional)

1. Get an API key from https://platform.openai.com
2. Set the environment variable:
   ```bash
   # Windows PowerShell
   $env:OPENAI_API_KEY = "sk-..."
   
   # Linux/Mac
   export OPENAI_API_KEY="sk-..."
   ```
3. Start the API proxy server:
   ```bash
   python api.py
   ```

---

## 📁 Project Structure

```
ai-travel-guide/
├── index.html              # Home page with hero section and features
├── destinations.html       # Destination explorer with search and maps
├── plan-trip.html          # Interactive trip planner with AI assistance
├── travel-tips.html        # Travel advice and tips by category
├── about.html              # About page with team and mission
├── styles.css              # Main stylesheet with all styling
├── server.py               # Flask backend with Ollama integration
├── api.py                  # OpenAI API proxy (optional)
├── test_chat.py            # Local KB testing utility
├── kb.json                 # Knowledge base for local recommendations
├── kb-merged-paris.json    # Merged KB for Paris-specific data
├── kb-poi-paris.json       # Points of interest for Paris
├── requirements.txt        # Python dependencies
├── .gitignore             # Git ignore rules
└── README.md              # This file
```

---

## 🛠️ Technology Stack

### Frontend
- **HTML5** - Semantic markup
- **CSS3** - Modern styling with CSS variables, flexbox, and grid
- **JavaScript (ES6+)** - Interactive features and API integration
- **Libraries**:
  - TensorFlow.js - Client-side AI features
  - Leaflet - Interactive maps
  - Firebase - Authentication
  - Font Awesome - Icons

### Backend
- **Python 3.8+** - Server-side logic
- **Flask** - Web framework
- **Flask-CORS** - Cross-origin resource sharing
- **Ollama** - Local AI model integration

### APIs & Services
- **Open-Meteo** - Weather data (free, no API key required)
- **Nominatim** - Geocoding (OpenStreetMap)
- **Overpass API** - OpenStreetMap points of interest
- **Firebase Auth** - User authentication
- **Unsplash** - Destination images

---

## 📖 Usage Guide

### Planning a Trip

1. **Browse Destinations**
   - Visit the Destinations page
   - Use filters (Beach, Mountain, City, Historical)
   - Search for any destination worldwide

2. **Use the Trip Planner**
   - Navigate to "Plan Trip"
   - Follow the 4-step process:
     1. Choose destination
     2. Select travel dates
     3. Pick activities
     4. Review and generate AI itinerary

3. **Chat with AI Assistant**
   - Click the robot icon in the bottom-right corner
   - Ask questions about destinations, packing, itineraries
   - Get personalized recommendations

4. **Generate AI Itineraries**
   - Click "Generate AI Itinerary" on any destination
   - AI creates a personalized day-by-day plan
   - Customize based on your preferences

### Saving Destinations

- Click the heart icon on any destination card
- Access saved destinations from your user profile
- Sign in to sync across devices

### Dark Mode

- Click the moon/sun icon in the header
- Preference is saved automatically

---

## 🔧 Configuration

### Firebase Setup (Optional)

The app includes Firebase authentication. To use your own Firebase project:

1. Create a project at https://console.firebase.google.com
2. Enable Authentication (Email/Password, Google, Facebook, Twitter)
3. Replace the Firebase config in each HTML file:
   ```javascript
   const firebaseConfig = {
       apiKey: "YOUR_API_KEY",
       authDomain: "YOUR_PROJECT.firebaseapp.com",
       projectId: "YOUR_PROJECT_ID",
       // ...
   };
   ```

### Customizing the Knowledge Base

Edit `kb.json` to add custom travel recommendations:
```json
{
  "id": "unique_id",
  "title": "Destination Name",
  "text": "Detailed description and recommendations..."
}
```

---

## 🧪 Testing

### Test the Local KB System
```bash
python test_chat.py --message "Paris museums"
```

### Test with Piped Input
```bash
echo "Tokyo itinerary" | python test_chat.py
```

### Interactive Mode
```bash
python test_chat.py
```

---

## 🌐 Deployment

### GitHub Pages (Static Frontend)

1. Push to GitHub
2. Go to Settings > Pages
3. Select your branch and save
4. Your site will be at `https://yourusername.github.io/ai-travel-guide/`

**Note**: Backend features (Ollama chatbot) require a running server.

### Heroku (Full Stack)

1. Create `Procfile`:
   ```
   web: python server.py
   ```

2. Deploy:
   ```bash
   heroku create your-app-name
   git push heroku main
   ```

### Railway/Render

Similar to Heroku - connect your repo and deploy!

---

## 📝 API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/chat` | POST | AI chatbot conversation |
| `/recommendations` | POST | Get personalized destination recommendations |
| `/itinerary` | POST | Generate AI travel itinerary |
| `/smart-search` | POST | AI-powered travel search |

### Example: Chat Endpoint
```bash
curl -X POST http://localhost:5000/chat \
  -H "Content-Type: application/json" \
  -d '{"message": "Best time to visit Paris?", "preferences": {}}'
```

---

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

---

## 🙏 Acknowledgments

- **OpenStreetMap** - Maps and geocoding data
- **Unsplash** - Beautiful travel photography
- **Open-Meteo** - Weather API
- **Ollama** - Local AI models
- **Firebase** - Authentication services
- **Font Awesome** - Icon library

---

## 📧 Contact

For questions, suggestions, or issues:
- Open an issue on GitHub
- Email: [your-email@example.com]
- Twitter: [@yourhandle]

---

## 🗺️ Roadmap

- [ ] Mobile app (React Native/Flutter)
- [ ] Social features (share trips, follow travelers)
- [ ] Booking integration (flights, hotels)
- [ ] Voice assistant support
- [ ] Offline mode
- [ ] More AI models (image recognition, translation)
- [ ] User reviews and ratings
- [ ] Travel expense tracker

---

**Made with ❤️ for travelers worldwide**
