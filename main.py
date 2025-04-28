import cv2
import time
from utils.detection import ObjectDetector
from utils.tracker import Tracker
from utils.monitor import ObjectMonitor

# Initialize models
detector = ObjectDetector()
tracker = Tracker()
monitor = ObjectMonitor()

# Open camera or video
cap = cv2.VideoCapture(0)

# Confidence threshold to filter weak detections
CONFIDENCE_THRESHOLD = 0.5

# Minimum bounding box area
MIN_BBOX_AREA = 500

# Sequential ID counter
sequential_id = 1
id_mapping = {}

# For FPS calculation
prev_time = 0

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Calculate FPS
    current_time = time.time()
    fps = 1 / (current_time - prev_time) if prev_time else 0
    prev_time = current_time

    # 1. Detect objects
    detections_raw, labels, scores = detector.detect(frame)

    # 2. Filter detections
    detections = []
    if detections_raw:
        for bbox, score in zip(detections_raw, scores):
            if score < CONFIDENCE_THRESHOLD:
                continue
            
            x1, y1, x2, y2 = bbox
            w = x2 - x1
            h = y2 - y1
            if w * h < MIN_BBOX_AREA:
                continue
            
            detections.append([[x1, y1, w, h], float(score)])

    # 3. Track objects
    tracks = tracker.update(detections, frame)

    current_ids = set()
    for track in tracks:
        if not track.is_confirmed():
            continue
        track_id = track.track_id
        bbox = track.to_ltrb()

        current_ids.add(track_id)

        # Assign sequential ID
        if track_id not in id_mapping:
            id_mapping[track_id] = sequential_id
            sequential_id += 1

        display_id = id_mapping[track_id]

        # 4. Draw bounding boxes and display object IDs
        cv2.rectangle(frame, (int(bbox[0]), int(bbox[1])), (int(bbox[2]), int(bbox[3])), (0, 255, 0), 2)
        cv2.putText(frame, f'ID:{display_id}', (int(bbox[0]), int(bbox[1]) - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)

    # 5. Monitor missing and new objects
    missing, new = monitor.update(current_ids)

    for m in missing:
        mapped_missing_id = id_mapping.get(m, m)
        print(f"Missing Object ID: {mapped_missing_id}")
    for n in new:
        mapped_new_id = id_mapping.get(n, n)
        print(f"New Object ID: {mapped_new_id}")

    # 6. Display FPS on frame
    cv2.putText(frame, f'FPS: {fps:.2f}', (20, 30),
                cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 255), 2)

    # 7. Show frame
    cv2.imshow('Object Tracking', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
