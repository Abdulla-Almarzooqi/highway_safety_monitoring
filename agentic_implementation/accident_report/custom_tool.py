import os
import base64
from typing import Type, Dict, Any, List
from pydantic import BaseModel, Field, PrivateAttr
from crewai.tools import BaseTool

###############################
# Image Encoding (Base64)
###############################
def encode_image(image_path: str) -> str:
    """Encode a local image as a base64 string."""
    with open(image_path, "rb") as f:
        return base64.b64encode(f.read()).decode("utf-8")

###############################
# Frame Sampling Tool
###############################
def sample_frames(video_id: str) -> Dict[str, Any]:
    """
    Given a video ID (e.g., "000001"), sample frames from the accident footage directory.
    Assumes images are named as: C_{video_id}_{frame}.jpg, where frame is two-digit (01 to 50).
    Uses a fixed accident frame of 25.
    Sampling:
      - Every 5 frames before frame 25,
      - Frame 25,
      - Every 2 frames after frame 25.
    Returns a dictionary with keys "frames" (list of file paths) and "accident_frame" (integer).
    """
    accident_frame = 25
    footage_dir = "/home/abdulla.almarzooqi/Desktop/Thesis/datasets/car-crash-dataset-ccd/CrashBest"
    
    before_frames = list(range(1, accident_frame, 5))
    after_frames = list(range(accident_frame + 2, 51, 2))
    sampled_frames = before_frames + [accident_frame] + after_frames
    
    frames_list: List[str] = []
    for frame in sampled_frames:
        frame_str = f"{frame:02}"
        filename = f"C_{video_id}_{frame_str}.jpg"
        full_path = os.path.join(footage_dir, filename)
        if os.path.exists(full_path):
            frames_list.append(full_path)
    return {"frames": frames_list, "accident_frame": accident_frame}

class FrameSamplerInput(BaseModel):
    video_id: str = Field(..., description="Video ID, zero-padded to 6 digits (e.g., '000001').")

class FrameSamplerTool(BaseTool):
    name: str = "frame_sampler_tool"
    description: str = (
        "A tool that samples frames from accident footage based on a video ID. "
        "Returns a dictionary with 'frames' (list of file paths) and 'accident_frame' (an integer)."
    )
    args_schema: Type[BaseModel] = FrameSamplerInput
    _dummy: Any = PrivateAttr()
    
    def _run(self, video_id: str) -> str:
        result = sample_frames(video_id)
        return str(result)

###############################
# Base64 Image Classifier Tool
###############################
class ImageClassifierInput(BaseModel):
    image_path: str = Field(..., description="Local path to the image")
    instructions: str = Field(..., description="Instructions for classification (one-liner)")

class Base64ImageClassifierTool(BaseTool):
    name: str = "base64_image_classifier_tool"
    description: str = (
        "A tool that encodes a local image in base64 and calls GPT-4o to classify the image "
        "based on provided instructions."
    )
    args_schema: Type[BaseModel] = ImageClassifierInput
    _dummy: Any = PrivateAttr()
    
    def _run(self, image_path: str, instructions: str) -> str:
        # Encode the image
        base64_data = encode_image(image_path)
        data_url = f"data:image/jpeg;base64,{base64_data}"
        # Construct the message for GPT-4o
        import litellm
        try:
            response = litellm.completion(
                model="gpt-4o",
                messages=[
                    {
                        "role": "system",
                        "content": (
                            "You are an image classification assistant. "
                            "Follow user instructions strictly and output the classification result."
                        )
                    },
                    {
                        "role": "user",
                        "content": [
                            {"type": "text", "text": instructions},
                            {"type": "image_url", "image_url": {"url": data_url}}
                        ]
                    }
                ],
                temperature=0.0,
            )
            return response.choices[0].message.content.strip()
        except Exception as e:
            return f"Error in classification: {str(e)}"
