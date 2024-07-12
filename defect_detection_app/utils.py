from defect_detection_app.models import DefectClassification
import cv2
import numpy as np
import matplotlib.pyplot as plt
from keras.models import load_model

# Load the trained model
model = load_model(r"D:\CODER\Pythonpro\Painted_Surface_Robot_Defect_Detection\surface_defect_detection\surface_defect_detection_trained_model2.h5")


def detect_defect(image_path):
    # Load the image
    img = cv2.imread(image_path)
    if img is None:
        print("Error loading image.")
        return None

    # Resize and normalize the image
    img_resized = cv2.resize(img, (224, 224))
    img_normalized = img_resized / 255.0
    img_array = np.expand_dims(img_normalized, axis=0)

    # Make a prediction
    prediction = model.predict(img_array)

    # Display the input image
    plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    plt.axis('off')

    if prediction[0][0] > 0.5:
        plt.title("Defective")
        classification = "Defective"

        # Find contours and calculate max width
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        # Apply Gaussian blur
        blurred = cv2.GaussianBlur(gray, (3, 3), 0)
        # Perform edge detection
        edges = cv2.Canny(blurred, 100, 200)
        # Find contours
        contours, _ = cv2.findContours(edges, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

        max_width = []
    
        # Iterate through each contour
        for contour in contours:
            for i in range(len(contour)):
                # Calculate distance between points on opposite sides of the crack
                pt1 = contour[i][0]
                pt2 = contour[(i + 1) % len(contour)][0]
                width = np.sqrt((pt2[0] - pt1[0])**2 + (pt2[1] - pt1[1])**2)
                width_mm = width * 0.265  # Assuming pixel to mm conversion factor of 0.265

                # Calculate perpendicular line
                angle = np.arctan2(pt2[1] - pt1[1], pt2[0] - pt1[0])
                x_offset = int(width * np.sin(angle))
                y_offset = int(width * np.cos(angle))
                pt1_perpendicular_1 = (pt1[0] + x_offset, pt1[1] - y_offset)
                pt2_perpendicular_1 = (pt1[0] - x_offset, pt1[1] + y_offset)
                pt1_perpendicular_2 = (pt2[0] + x_offset, pt2[1] - y_offset)
                pt2_perpendicular_2 = (pt2[0] - x_offset, pt2[1] + y_offset)

            
                # Store the width for comparison
                max_width.append((pt1_perpendicular_1, pt2_perpendicular_1, width_mm))
                max_width.append((pt1_perpendicular_2, pt2_perpendicular_2, width_mm))

        if max_width:  # Check if max_width is not empty
            max_width = max(max_width, key=lambda x: x[2])
            maximum_width = np.max(max_width[2])
            #print(f"Max Width: {maximum_width:.2f} mm\n")

            severity = ""
            if maximum_width <= 5:
                severity = "Low"
            elif maximum_width <= 25:
                severity = "Moderate"
            else:
                severity = "High"

            return classification, maximum_width, severity

    else:
        plt.title("Not Defective")
        classification = "Defect-Free"
        maximum_width = 0.000
        severity = "No Defect" 
        return classification, maximum_width, severity
    



import cv2
import threading
import numpy as np
from django.core.serializers.json import DjangoJSONEncoder
from django.http import JsonResponse
import base64

# Lock for thread-safe access to global variables
results_lock = threading.Lock()

# Global variables to control threading
stop_event = threading.Event()

results = {
    'classification': '',
    'max_width': '',
    'severity': ''
}

live_frame = None 

# Function for Live Defect Detection
def live_defect_detection():
    global stop_event
    global results
    global live_frame

    # Start the webcam
    cap = cv2.VideoCapture(0)

    while not stop_event.is_set():
        ret, frame = cap.read()
        if not ret:
            break

        # Initialize classification outside the prediction block
        classification = ""

        # Resize and normalize the frame
        img_resized = cv2.resize(frame, (224, 224))
        img_normalized = img_resized / 255.0
        img_array = np.expand_dims(img_normalized, axis=0)

        # Make a prediction
        prediction = model.predict(img_array)

        if prediction[0][0] > 0.5:
            classification = "Defective"
        

            # Convert the frame to grayscale
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            # Apply Gaussian blur
            blurred = cv2.GaussianBlur(gray, (3, 3), 0)

            # Perform edge detection
            edges = cv2.Canny(blurred, 100, 200)

            # Find contours
            contours, _ = cv2.findContours(edges, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

            max_width = []

            # Iterate through each contour
            for contour in contours:
                for i in range(len(contour)):
                    # Calculate distance between points on opposite sides of the crack
                    pt1 = contour[i][0]
                    pt2 = contour[(i + 1) % len(contour)][0]
                    width = np.sqrt((pt2[0] - pt1[0])**2 + (pt2[1] - pt1[1])**2)
                    width_mm = width * 0.265  # Assuming pixel to mm conversion factor of 0.265

                    # Calculate perpendicular line
                    angle = np.arctan2(pt2[1] - pt1[1], pt2[0] - pt1[0])
                    x_offset = int(width * np.sin(angle))
                    y_offset = int(width * np.cos(angle))
                    pt1_perpendicular_1 = (pt1[0] + x_offset, pt1[1] - y_offset)
                    pt2_perpendicular_1 = (pt1[0] - x_offset, pt1[1] + y_offset)
                    pt1_perpendicular_2 = (pt2[0] + x_offset, pt2[1] - y_offset)
                    pt2_perpendicular_2 = (pt2[0] - x_offset, pt2[1] + y_offset)

                    # Draw perpendicular lines
                    """
                    cv2.line(frame, pt1_perpendicular_1, pt2_perpendicular_1, (255, 0, 0), 2)
                    cv2.line(frame, pt1_perpendicular_2, pt2_perpendicular_2, (255, 0, 0), 2)
                    """
                    # Store the width for comparison
                    max_width.append((pt1_perpendicular_1, pt2_perpendicular_1, width_mm))
                    max_width.append((pt1_perpendicular_2, pt2_perpendicular_2, width_mm))

            if max_width:  # Check if max_width is not empty
                max_width = max(max_width, key=lambda x: x[2])
                cv2.line(frame, max_width[0], max_width[1], (0, 0, 255), 2)
                maximum_width = np.max(max_width[2])

                severity = ""
                if maximum_width <= 5:
                    severity = "Low"
                elif maximum_width <= 25:
                    severity = "Moderate"
                else:
                    severity = "High"
                
                # Display the severity and max width
                if max_width is not None and severity is not None:
                    cv2.putText(frame, f"Max Width(in mm): {maximum_width:.2f}", (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
                    cv2.putText(frame, f"Severity: {severity}", (10, 90), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
                    with results_lock:
                        results = {
                            'classification': classification,
                            'max_width': f'{maximum_width:.2f}',
                            'severity': severity
                        }
        else:
            classification = "Defect-Free"
            maximum_width = 0.000
            severity = "No Defect"
            with results_lock:
                results = {
                    'classification': classification,
                    'max_width': f'{maximum_width:.2f}',
                    'severity': severity
                }                                                                                                                           
        # Display the classification, max width, and severity on the frame
        cv2.putText(frame, f"Classification: {classification}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

        # Update the live frame
        ret, buffer = cv2.imencode('.jpg', frame)
        live_frame = base64.b64encode(buffer).decode('utf-8')

        # Display the frame
        cv2.imshow('Live Detection', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    cap.release()
    cv2.destroyAllWindows()
    # Clear the stop event for next detection
    stop_event.clear()


def start_live_detection():
    global stop_event
    stop_event.clear()  # Clear the event to start the detection
    threading.Thread(target=live_defect_detection).start()

def stop_live_detection():
    global stop_event
    stop_event.set() 

def get_results(request):
    global results
    return JsonResponse(results, encoder=DjangoJSONEncoder)



