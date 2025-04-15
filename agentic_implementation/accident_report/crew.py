from crewai import Agent, Task, Crew, Process
from crewai.project import CrewBase, agent, task, crew
from accident_report.tools.custom_tool import Base64ImageClassifierTool, FrameSamplerTool
import random

@CrewBase
class AccidentReportCrew:
    agents_config = "config/agents.yaml"
    tasks_config = "config/tasks.yaml"

    @agent
    def airbag_status_agent(self):
        # Uses GPT-4o via Base64ImageClassifierTool to analyze the airbag image.
        return Agent(
            config=self.agents_config["airbag_status_agent"],
            verbose=True,
            tools=[Base64ImageClassifierTool()]
        )

    @agent
    def weather_condition_agent(self):
        # Always returns "Normal" for demonstration.
        return Agent(
            config=self.agents_config["weather_condition_agent"],
            verbose=True
        )

    @agent
    def seatbelt_status_agent(self):
        # Uses GPT-4o via Base64ImageClassifierTool to analyze the seatbelt image.
        return Agent(
            config=self.agents_config["seatbelt_status_agent"],
            verbose=True,
            tools=[Base64ImageClassifierTool()]
        )

    @agent
    def video_preprocess_agent(self):
        # Uses FrameSamplerTool to sample frames from accident footage.
        return Agent(
            config=self.agents_config["video_preprocess_agent"],
            verbose=True,
            tools=[FrameSamplerTool()]
        )

    @agent
    def accident_report_generation_agent(self):
        # Uses GPT-4o to synthesize inputs and generate a final accident report.
        return Agent(
            config=self.agents_config["accident_report_generation_agent"],
            verbose=True,
            llm="gpt-4o"
        )

    @task
    def airbag_signal_task(self):
        return Task(
            config=self.tasks_config["airbag_signal_task"]
        )

    @task
    def video_preprocess_task(self):
        return Task(
            config=self.tasks_config["video_preprocess_task"]
        )

    @task
    def weather_condition_task(self):
        # Simulate always returning "Normal"
        agent_instance = self.weather_condition_agent()
        object.__setattr__(agent_instance, "execute_task", lambda task, context=None, tools=None: "Normal")
        return Task(
            config=self.tasks_config["weather_condition_task"]
        )

    @task
    def seatbelt_status_task(self):
        return Task(
            config=self.tasks_config["seatbelt_status_task"]
        )

    @task
    def accident_report_task(self):
        return Task(
            config=self.tasks_config["accident_report_task"]
        )

    @crew
    def crew(self) -> Crew:
        return Crew(
            agents=[
                self.airbag_status_agent(),
                self.weather_condition_agent(),
                self.seatbelt_status_agent(),
                self.video_preprocess_agent(),
                self.accident_report_generation_agent()
            ],
            tasks=[
                self.airbag_signal_task(),
                self.video_preprocess_task(),
                self.weather_condition_task(),
                self.seatbelt_status_task(),
                self.accident_report_task()
            ],
            process=Process.sequential,
            verbose=True,
        )
