import os
import base64
import json
from flask import Flask, request, jsonify
from flask_cors import CORS
import google.generativeai as genai
from PIL import Image
import io

app = Flask(__name__)
CORS(app)

# Configure Gemini API
GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')
if not GEMINI_API_KEY:
    raise ValueError("GEMINI_API_KEY environment variable not set")

genai.configure(api_key=GEMINI_API_KEY)

@app.route('/api/generate-effect', methods=['POST'])
def generate_effect():
    """
    Generate visual effects for Naruto/Sasuke powers using Gemini Vision API
    """
    try:
        data = request.json
        frame_base64 = data.get('frame')
        character = data.get('character')  # 'naruto' or 'sasuke'
        hand_position = data.get('hand_position')  # {x, y, z}
        power_level = data.get('power_level')  # 0-1

        if not frame_base64 or not character:
            return jsonify({'error': 'Missing frame or character'}), 400

        # Decode base64 frame
        frame_data = base64.b64decode(frame_base64)
        frame_image = Image.open(io.BytesIO(frame_data))

        # Prepare prompt based on character
        if character == 'sasuke':
            prompt = f"""Analyze this video frame and generate a description for a CHIDORI (Lightning Release) effect overlay.
            
            The hand position is at coordinates: x={hand_position.get('x', 0.5)}, y={hand_position.get('y', 0.5)}, z={hand_position.get('z', 0.5)}
            Power level (0-1): {power_level}
            
            Generate a JSON response with:
            1. "effect_description": Detailed description of the chidori effect (purple/blue lightning, chirping sound intensity, crackling energy)
            2. "intensity": How intense the effect should be (0-1)
            3. "color_palette": Array of hex colors for the effect (e.g., ["#0066ff", "#9900ff", "#ffffff"])
            4. "particle_count": Suggested number of particles for the effect
            5. "animation_speed": Speed of animation (0.5-2.0)
            
            Make the effect look like authentic Naruto chidori power."""
        else:  # naruto
            prompt = f"""Analyze this video frame and generate a description for a RASENGAN (Spiral Sphere) effect overlay.
            
            The hand position is at coordinates: x={hand_position.get('x', 0.5)}, y={hand_position.get('y', 0.5)}, z={hand_position.get('z', 0.5)}
            Power level (0-1): {power_level}
            
            Generate a JSON response with:
            1. "effect_description": Detailed description of the rasengan effect (orange/yellow spiral, swirling energy, wind effect)
            2. "intensity": How intense the effect should be (0-1)
            3. "color_palette": Array of hex colors for the effect (e.g., ["#ff6600", "#ffcc00", "#ffffff"])
            4. "particle_count": Suggested number of particles for the effect
            5. "animation_speed": Speed of animation (0.5-2.0)
            
            Make the effect look like authentic Naruto rasengan power."""

        # Call Gemini Vision API
        model = genai.GenerativeModel('gemini-2.5-flash')
        response = model.generate_content([
            prompt,
            frame_image
        ])

        # Parse response
        response_text = response.text
        
        # Try to extract JSON from response
        try:
            # Find JSON in response
            json_start = response_text.find('{')
            json_end = response_text.rfind('}') + 1
            if json_start != -1 and json_end > json_start:
                json_str = response_text[json_start:json_end]
                effect_data = json.loads(json_str)
            else:
                effect_data = {
                    'effect_description': response_text,
                    'intensity': power_level,
                    'color_palette': ['#0066ff', '#9900ff', '#ffffff'] if character == 'sasuke' else ['#ff6600', '#ffcc00', '#ffffff'],
                    'particle_count': int(50 * power_level) + 20,
                    'animation_speed': 1.0 + (power_level * 0.5)
                }
        except json.JSONDecodeError:
            effect_data = {
                'effect_description': response_text,
                'intensity': power_level,
                'color_palette': ['#0066ff', '#9900ff', '#ffffff'] if character == 'sasuke' else ['#ff6600', '#ffcc00', '#ffffff'],
                'particle_count': int(50 * power_level) + 20,
                'animation_speed': 1.0 + (power_level * 0.5)
            }

        return jsonify(effect_data)

    except Exception as e:
        print(f"Error: {str(e)}")
        return jsonify({'error': str(e)}), 500

@app.route('/health', methods=['GET'])
def health():
    return jsonify({'status': 'ok'})

if __name__ == '__main__':
    app.run(debug=True, port=5000)
