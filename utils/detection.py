from ultralytics import YOLO
import cv2

IMPORTANT_CLASSES = ['person', 'bottle', 'laptop', 'cell phone']

class ObjectDetector:
    def __init__(self, model_path='yolov8n.pt'):
        self.model = YOLO(model_path)

    def detect(self, frame):
        
        frame_resized = cv2.resize(frame, (640, 480))

       
        results = self.model.predict(source=frame_resized, imgsz=640, conf=0.5, verbose=False)

        detections = []
        labels = []
        scores = []

        if len(results) > 0:
            for box in results[0].boxes:
                x1, y1, x2, y2 = box.xyxy[0].cpu().numpy()
                conf = float(box.conf[0])
                cls = int(box.cls[0])
                label = self.model.names[cls]

                if label not in IMPORTANT_CLASSES:
                    continue  

                detections.append([x1, y1, x2, y2])
                labels.append(label)
                scores.append(conf)

        return detections, labels, scores
