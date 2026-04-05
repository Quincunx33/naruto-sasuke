# Naruto & Sasuke Hand Tracking Power Effects - Powered by Gemini AI

This project transforms your webcam feed into an interactive experience, allowing you to wield the iconic powers of Naruto Uzumaki (Rasengan) and Sasuke Uchiha (Chidori) using hand tracking. Built with MediaPipe for hand detection and powered by Google's Gemini AI for intelligent effect generation, this application overlays dynamic visual and audio effects in real-time.

## Features

### 1. Real-Time Hand Tracking
*   **MediaPipe Hands**: Accurate detection of hand landmarks and gestures using MediaPipe's state-of-the-art hand tracking model.
*   **Dual Hand Support**: Track both hands simultaneously for enhanced interactivity.
*   **Premium Glow Skeleton**: Hand joints are rendered with neon-colored glows for a professional appearance.

### 2. AI-Powered Visual Effects (Gemini Integration)
*   **Intelligent Effect Generation**: Gemini AI analyzes video frames in real-time to generate contextually appropriate visual effects.
*   **Dynamic Chidori (Sasuke)**: Purple and blue lightning effects with crackling energy particles that respond to hand position and power level.
*   **Dynamic Rasengan (Naruto)**: Orange and yellow spiral effects with swirling wind particles that intensify with power buildup.
*   **Particle System**: Smooth particle animations that follow hand movement and power intensity.

### 3. Audio & Immersion
*   **Sound Effects (SFX)**: Authentic 'Rasengan' charging sounds for Naruto and 'Chidori' chirping sounds for Sasuke.
*   **Background Music (BGM)**: A Naruto fight theme plays in the background when a power is activated.
*   **Voice Lines**: Signature character dialogues are played upon power activation.

### 4. User Interface (UI/UX)
*   **Character Selection Menu**: Choose between playing as Naruto or Sasuke at startup.
*   **Camera Filters**: Screen shake effects and color grading (purple for Sasuke, orange for Naruto) when powers are active.
*   **Real-Time Status Display**: Monitor API connection and power activation status.

### 5. Technical Optimization
*   **Offline Support**: Service Worker integration for offline functionality.
*   **Frame Skipping**: Intelligent frame processing to optimize API calls without sacrificing responsiveness.
*   **CORS Support**: Backend configured for cross-origin requests from the frontend.

## Architecture

### Frontend (`index-gemini.html`)
*   HTML5 Canvas for rendering hand tracking and effects
*   MediaPipe Hands for real-time hand detection
*   Particle system for visual effects
*   Async API calls to backend for Gemini-powered effect generation

### Backend (`server.py`)
*   Flask server with CORS support
*   Gemini Vision API integration for frame analysis
*   Effect data generation based on hand position and power level
*   JSON response format for easy frontend integration

## Installation & Setup

### Prerequisites
*   Python 3.8+
*   Node.js (optional, for local development server)
*   Google Gemini API Key ([Get it here](https://ai.google.dev/))

### Step 1: Clone the Repository
```bash
git clone https://github.com/Quincunx33/naruto-sasuke-power-fx.git
cd naruto-sasuke-power-fx
```

### Step 2: Set Up Environment Variables
```bash
cp .env.example .env
# Edit .env and add your GEMINI_API_KEY
```

### Step 3: Install Python Dependencies
```bash
pip install -r requirements.txt
```

### Step 4: Start the Backend Server
```bash
python server.py
```
The server will run on `http://localhost:5000`

### Step 5: Open the Application
*   Open `index-gemini.html` in your web browser
*   Allow webcam access when prompted
*   Select your character (Naruto or Sasuke)
*   Show your palm to activate powers!

## API Endpoints

### POST `/api/generate-effect`
Generates visual effect data based on video frame and hand position.

**Request Body:**
```json
{
  "frame": "base64_encoded_image",
  "character": "naruto" | "sasuke",
  "hand_position": {
    "x": 0.5,
    "y": 0.5,
    "z": 0.1
  },
  "power_level": 0.75
}
```

**Response:**
```json
{
  "effect_description": "Description of the effect",
  "intensity": 0.75,
  "color_palette": ["#ff6600", "#ffcc00", "#ffffff"],
  "particle_count": 50,
  "animation_speed": 1.25
}
```

## How to Use

1.  **Select Your Character**: Choose between Naruto (Rasengan) or Sasuke (Chidori)
2.  **Show Your Palm**: Open your hand to the camera to activate the power
3.  **Control Power Level**: The longer you hold your palm open, the more powerful the effect becomes
4.  **Watch the Magic**: Gemini AI generates unique effects based on your hand position and the video frame

## Troubleshooting

### Backend Connection Issues
*   Ensure the Flask server is running on `http://localhost:5000`
*   Check that your GEMINI_API_KEY is correctly set in the `.env` file
*   Verify CORS is enabled in the backend

### Webcam Not Working
*   Check browser permissions for camera access
*   Ensure your camera is not being used by another application
*   Try a different browser if issues persist

### Effects Not Showing
*   Make sure you're using `index-gemini.html` (not the basic `index.html`)
*   Check browser console for API errors
*   Verify that the backend is responding to requests

## Future Enhancements

*   Advanced gesture recognition for ninja signs
*   Multi-user multiplayer mode
*   Custom effect creation with Gemini
*   Mobile app version
*   Performance optimization for low-end devices

## Technologies Used

*   **Frontend**: HTML5, CSS3, JavaScript, Canvas API
*   **Hand Tracking**: MediaPipe Hands
*   **AI/ML**: Google Gemini Vision API
*   **Backend**: Flask, Flask-CORS
*   **Image Processing**: Pillow

## License

This project is open-source and available under the MIT License.

## Credits

*   Naruto series by Masashi Kishimoto
*   MediaPipe by Google
*   Gemini AI by Google DeepMind

---

**Enjoy wielding your ninja powers! 🥋⚡**
