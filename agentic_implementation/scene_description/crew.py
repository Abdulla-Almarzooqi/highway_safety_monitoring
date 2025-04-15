#!/home/abdulla.almarzooqi/miniconda3/envs/llama/bin/python

from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, task, crew
from typing import Any

@CrewBase
class SceneDescriptionCrew:
    """Crew for generating a driving scene description using object detection and GPT-4o."""
    
    agents_config = "config/agents.yaml"
    tasks_config = "config/tasks.yaml"
    
    @agent
    def object_detection_agent(self) -> Agent:
        # Import the custom YOLOv11 tool
        from scene_description.tools.custom_tool import YoloV11DetectionTool
        return Agent(
            config=self.agents_config["object_detection_agent"],
            verbose=True,
            tools=[YoloV11DetectionTool(model_path="/home/abdulla.almarzooqi/Desktop/Thesis/yolo11x.pt")]
        )
    
    @agent
    def scene_description_agent(self) -> Agent:
        return Agent(
            config=self.agents_config["scene_description_agent"],
            verbose=True,
            llm="gpt-4o"
        )
    
    @task
    def object_detection_task(self) -> Task:
        return Task(
            config=self.tasks_config["object_detection_task"]
        )
    
    @task
    def scene_description_task(self) -> Task:
        return Task(
            config=self.tasks_config["scene_description_task"]
        )
    
    @crew
    def crew(self) -> Crew:
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True,
        )
