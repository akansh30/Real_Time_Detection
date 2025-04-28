# Real-Time Object Detection, Tracking, and Monitoring

This project implements a real-time video analytics system that can:
- Detect when objects go missing (leave the frame)
- Detect when new objects appear
- Track objects across frames with unique IDs

The system uses:
- **YOLOv8** for object detection
- **DeepSORT** for object tracking
- A **custom monitor** for identifying missing and new objects

## How to Run Locally

# Install the required dependencies:

```bash
pip install -r requirements.txt
```

# Running the application:
```
python main.py
```
# Running with Docker:

# Build the Docker image:
```
docker build -t real-time-detection .
```
# Run the Docker container:
```
docker run --gpus all -it real-time-detection
```
