#!/home/abdulla.almarzooqi/Desktop/Thesis/scene_description/.venv/bin/python

def run():
    """
    Entry point for CrewAI CLI.
    Initializes the crew, passes necessary inputs, and prints the result.
    """
    from scene_description.crew import SceneDescriptionCrew
    image_path = "/home/abdulla.almarzooqi/Desktop/Thesis/datasets/leftImg8bit/train/aachen/aachen_000000_000019_leftImg8bit.png"
    
    inputs = {
        "exterior_image": image_path,
        "object_detection_task": ""  # Provide a default value to satisfy the placeholder
    }

    crew_instance = SceneDescriptionCrew().crew()
    result = crew_instance.kickoff(inputs=inputs)
    print("=== Final Result ===")
    print(result)
