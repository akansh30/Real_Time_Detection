from deep_sort_realtime.deepsort_tracker import DeepSort

class Tracker:
    def __init__(self):
        
        self.tracker = DeepSort(
            max_age=30,  
            n_init=3,    
            max_iou_distance=0.7,  
            nn_budget=100 
        )

    def update(self, detections, frame):
        tracks = self.tracker.update_tracks(detections, frame=frame)
        return tracks
