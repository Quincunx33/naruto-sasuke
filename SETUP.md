# Setup Guide - Naruto & Sasuke Power Effects with Gemini AI

## Quick Start (5 Minutes)

### 1. Get Your Gemini API Key
1. Go to [Google AI Studio](https://ai.google.dev/aistudio)
2. Click "Get API Key"
3. Create a new API key
4. Copy the key

### 2. Configure Environment
```bash
# Create .env file
cp .env.example .env

# Edit .env and paste your API key
# GEMINI_API_KEY=your_key_here
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the Backend
```bash
python server.py
```
You should see: `Running on http://127.0.0.1:5000`

### 5. Open the App
1. Open `index-gemini.html` in your browser
2. Allow camera access
3. Select Naruto or Sasuke
4. Show your palm to activate powers!

---

## Detailed Setup

### System Requirements
- **OS**: Windows, macOS, or Linux
- **Python**: 3.8 or higher
- **Browser**: Chrome, Firefox, Safari, or Edge (with webcam support)
- **Internet**: Required for Gemini API calls

### Installation Steps

#### Step 1: Clone Repository
```bash
git clone https://github.com/Quincunx33/naruto-sasuke-power-fx.git
cd naruto-sasuke-power-fx
```

#### Step 2: Create Virtual Environment (Recommended)
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

#### Step 3: Install Python Packages
```bash
pip install -r requirements.txt
```

#### Step 4: Set Up Gemini API
1. Visit [Google AI Studio](https://ai.google.dev/aistudio)
2. Sign in with your Google account
3. Click "Create API Key"
4. Select or create a project
5. Copy the generated API key

#### Step 5: Configure Environment
```bash
# Copy example file
cp .env.example .env

# Edit .env with your API key
# On Windows: notepad .env
# On macOS/Linux: nano .env
```

Add your API key:
```
GEMINI_API_KEY=your_actual_api_key_here
FLASK_ENV=development
FLASK_DEBUG=True
```

#### Step 6: Start Backend Server
```bash
python server.py
```

Expected output:
```
 * Running on http://127.0.0.1:5000
 * Debug mode: on
```

#### Step 7: Open Frontend
1. Open your browser
2. Navigate to the folder containing `index-gemini.html`
3. Open `index-gemini.html` (right-click → Open with Browser)
4. OR use a local server:
   ```bash
   # Python 3
   python -m http.server 8000
   # Then visit http://localhost:8000
   ```

---

## Troubleshooting

### "ModuleNotFoundError: No module named 'google'"
**Solution**: Install dependencies
```bash
pip install -r requirements.txt
```

### "GEMINI_API_KEY not set"
**Solution**: Check your `.env` file
```bash
# Verify .env exists and contains your key
cat .env
```

### "Connection refused" when opening frontend
**Solution**: Make sure backend is running
```bash
# In a separate terminal, run:
python server.py
```

### Webcam not working
**Solution**: Check browser permissions
1. Click the camera icon in the address bar
2. Select "Allow" for camera access
3. Refresh the page

### Effects not appearing
**Solution**: Use the correct HTML file
- Use `index-gemini.html` (with AI effects)
- NOT `index.html` (basic version)

### API calls failing
**Solution**: Check network and API key
1. Verify GEMINI_API_KEY is correct
2. Check internet connection
3. Look at browser console (F12) for errors
4. Check server logs for API responses

---

## Performance Tips

### For Low-End Devices
1. Reduce frame processing frequency (increase `FRAME_SKIP` in HTML)
2. Disable particle effects if needed
3. Use lower resolution camera input

### For High-End Devices
1. Decrease `FRAME_SKIP` for more frequent updates
2. Increase particle count for better visuals
3. Enable higher resolution camera input

---

## File Structure
```
naruto-sasuke-power-fx/
├── index.html              # Basic version (no AI)
├── index-gemini.html       # AI-powered version (USE THIS)
├── server.py               # Flask backend with Gemini API
├── sw.js                   # Service Worker for offline support
├── requirements.txt        # Python dependencies
├── .env.example           # Environment template
├── README.md              # Project documentation
├── SETUP.md              # This file
└── assets/
    ├── naruto.mp4        # Naruto power video
    ├── sasuke.mp4        # Sasuke power video
    ├── naruto_bgm.mp3    # Background music
    ├── rasengan_sfx.mp3  # Rasengan sound effect
    ├── chidori_sfx.mp3   # Chidori sound effect
    ├── naruto_dialogue.wav   # Naruto voice line
    └── sasuke_dialogue.wav   # Sasuke voice line
```

---

## API Reference

### Gemini Effect Generation
**Endpoint**: `POST /api/generate-effect`

**Request**:
```json
{
  "frame": "base64_image_data",
  "character": "sasuke",
  "hand_position": {"x": 640, "y": 360, "z": 0.5},
  "power_level": 0.8
}
```

**Response**:
```json
{
  "effect_description": "Intense purple lightning with crackling energy",
  "intensity": 0.8,
  "color_palette": ["#0066ff", "#9900ff", "#ffffff"],
  "particle_count": 50,
  "animation_speed": 1.3
}
```

---

## Advanced Configuration

### Adjust API Call Frequency
Edit `index-gemini.html`:
```javascript
const FRAME_SKIP = 5; // Process every 5th frame
```
- Lower value = More frequent API calls (better effects, slower)
- Higher value = Fewer API calls (faster, less responsive)

### Customize Effect Colors
Edit `index-gemini.html`:
```javascript
const colors = character === 'sasuke' 
  ? ['#0066ff', '#9900ff', '#ffffff']  // Sasuke colors
  : ['#ff6600', '#ffcc00', '#ffffff']; // Naruto colors
```

### Adjust Particle System
Edit `index-gemini.html`:
```javascript
const particleCount = Math.floor(30 * powerLevel);
```
- Increase multiplier for more particles
- Decrease for better performance

---

## Support

For issues or questions:
1. Check the Troubleshooting section above
2. Review browser console (F12) for errors
3. Check server logs for API errors
4. Visit [GitHub Issues](https://github.com/Quincunx33/naruto-sasuke-power-fx/issues)

---

**Enjoy your ninja powers! ⚡🔥**
