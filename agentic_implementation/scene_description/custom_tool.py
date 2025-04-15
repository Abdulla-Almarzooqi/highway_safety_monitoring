import os
import base64
from typing import Type, Dict, Any
from pydantic import BaseModel, Field, PrivateAttr
from crewai.tools import BaseTool

class YoloDetectionInput(BaseModel):
    image_path: str = Field(..., description="Local path to the driving scene image.")

# List of objects of interest
objects_of_interest = [
    'car', 'person', 'traffic_light', 'bicycle', 'bus', 'truck',
    'motorcycle', 'bench', 'stop_sign', 'cat', 'dog', 'parking_meter',
    'fire_hydrant', 'train'
]

class YoloV11DetectionTool(BaseTool):
    name: str = "yolov11_detection_tool"
    description: str = (
        "A tool that uses YOLOv11 to detect objects in an image. It filters the detections "
        "to include only objects of interest and returns a dictionary of object counts."
    )
    args_schema: Type[BaseModel] = YoloDetectionInput

    # Declare a private attribute for the YOLO model
    _model: Any = PrivateAttr()

    def __init__(self, model_path: str, **kwargs):
        super().__init__(**kwargs)

        if not os.path.isfile(model_path):
            raise FileNotFoundError(f"YOLO model not found at {model_path}")

        from ultralytics import YOLO
        # Store the YOLO model in the private attribute
        self._model = YOLO(model_path)

    def _run(self, image_path: str) -> str:
        if not os.path.isfile(image_path):
            return f"Error: Image file not found: {image_path}"

        results = self._model.predict(source=image_path, conf=0.25)
        result = results[0]  # single image
        counts: Dict[str, int] = {}
        for box in result.boxes:
            cls_id = int(box.cls[0]) if hasattr(box.cls, '__iter__') else int(box.cls)
            cls_name = result.names.get(cls_id, "unknown")
            cls_name = cls_name.replace(" ", "_")
            if cls_name in objects_of_interest:
                counts[cls_name] = counts.get(cls_name, 0) + 1
        return str(counts)
