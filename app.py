from flask import Flask, render_template
import cv2
from deepface import DeepFace
import os

app = Flask(__name__)

# Initialize video capture
cap = cv2.VideoCapture(0)
capturing = True

# Function to analyze frame and display emotion
def analyze_frame():
    global capturing
    while capturing:
        ret, frame = cap.read()

        if ret:
            try:
                # Perform sentiment analysis
                result = DeepFace.analyze(frame, actions=['emotion'])

                # Check if any face is detected
                if len(result) > 0:
                    dominant_emotion = result[0]['dominant_emotion']
                else:
                    dominant_emotion = "No Face Detected"

                # Display emotion label
                cv2.putText(frame, f'Emotion: {dominant_emotion}', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

            except Exception as e:
                print(f"Error: {e}")
                dominant_emotion = "Error Occurred"

            # Display video feed
            cv2.imshow('Emotion Analysis', frame)

            # Break the loop if 'q' is pressed
            if cv2.waitKey(1) & 0xFF == ord('q'):
                capturing = False
                break

# Route to display video feed with emotion analysis
@app.route('/')
def video_feed():
    return render_template('video_feed.html')

# Start analyzing frames
analyze_frame()

# Release video capture and close any open windows
cap.release()
cv2.destroyAllWindows()

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)


