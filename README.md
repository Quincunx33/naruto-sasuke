# Naruto & Sasuke Hand Tracking Power Effects

This project transforms your webcam feed into an interactive experience, allowing you to wield the iconic powers of Naruto Uzumaki (Rasengan) and Sasuke Uchiha (Chidori) using hand tracking. Built with MediaPipe, this application detects hand gestures and overlays dynamic visual and audio effects, bringing the world of Naruto to life right on your screen.

## Features

### 1. Visual Effects
*   **Dynamic Scaling**: The size of the power effects (Rasengan/Chidori) dynamically adjusts based on the distance of your hand from the camera, creating a realistic sense of depth.
*   **Hand Glow**: Subtle neon-colored glows are added to hand landmarks, enhancing the visual tracking and giving a premium feel.
*   **Smooth Transitions**: Power effects now fade in gradually using opacity, providing a more immersive and less abrupt activation.

### 2. Audio & Immersion
*   **Sound Effects (SFX)**: Authentic 'Rasengan' charging sounds for Naruto and 'Chidori' chirping sounds for Sasuke are integrated.
*   **Background Music (BGM)**: A low-volume Naruto fight theme plays in the background when a power is activated, intensifying the experience.
*   **Voice Lines**: Signature character dialogues are played upon power activation, adding to the character immersion.

### 3. Advanced Tracking (Planned for Future Updates)
*   **Hand Sign Detection**: Future updates will include detection of specific 'Ninja Signs' (e.g., two-finger cross) to trigger new powers.
*   **Movement Tracking**: Rapid hand movements will create visual trails or blur effects behind the video.
*   **Dual Hand Combo**: Specific two-hand gestures will activate powerful 'Final Valley' or 'Six Paths' level abilities.

### 4. User Interface (UI/UX)
*   **Character Selection Menu**: A user-friendly menu at startup allows you to choose between playing as Naruto or Sasuke.
*   **Camera Filters**: When a power is active, the entire screen gets a subtle shake effect and color grading (e.g., red or purple tint) to signify the intensity.
*   **Performance Mode**: (Planned) Options to toggle glow and high-resolution video for low-end devices.

### 5. Technical Optimization
*   **Offline Support**: Integrated Service Worker ensures the application loads even without an internet connection.
*   **Custom Video Assets**: High-quality green screen effects are used for power visuals, optimized for `mix-blend-mode` for clearer rendering.

## How to Use

1.  **Clone the repository**:
    ```bash
    git clone https://github.com/Quincunx33/naruto-sasuke-power-fx.git
    ```
2.  **Navigate to the project directory**:
    ```bash
    cd naruto-sasuke-power-fx
    ```
3.  **Open `index.html` in your web browser**.
    *   Ensure your browser allows webcam access.
    *   You might need to interact with the page (click, touch) to enable audio playback due to browser autoplay policies.

## Technologies Used

*   **MediaPipe Hands**: For real-time hand tracking and landmark detection.
*   **HTML5, CSS3, JavaScript**: Core web technologies for structure, styling, and interactivity.

## Contribution

Feel free to fork the repository, suggest features, or contribute to the project. Your feedback is highly appreciated!

## License

This project is open-source and available under the MIT License.
