# Real-Time Object Detection, Tracking, and Monitoring

![Screenshot 2025-04-29 025028](https://github.com/user-attachments/assets/6e3681d5-1d16-4e46-8f0c-d173a0405bbb)
![Screenshot 2025-04-29 024938](https://github.com/user-attachments/assets/4311bd7a-f257-4e9a-a982-01731dc61789)

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
# Output

- Displays real-time object detection and tracking with unique IDs.
- Detects and logs missing and new objects.
  
