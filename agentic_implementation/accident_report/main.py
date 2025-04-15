#!/home/abdulla.almarzooqi/Desktop/Thesis/accident_report/.venv/bin/python

from accident_report.crew import AccidentReportCrew

def run():
    """
    Entry point for running the accident report generation system.
    """
    # Prepare inputs:
    inputs = {
        "airbag_image": "/home/abdulla.almarzooqi/Desktop/Thesis/airbag-status.jpg",
        "seatbelt_image": "/home/abdulla.almarzooqi/Desktop/Thesis/seatbelt-status.jpg",
        "accident_video_id": "000001",
        "weather_condition_task": "Normal",   # default value
        "seatbelt_status_task": "fastened",     # default value (or "not fastened" as appropriate)
        "video_preprocess_task": "{}",           # default empty JSON (or an empty string)
        "airbag_signal_task": "deployed"  # A default value so the interpolation succeeds
    }

    crew_instance = AccidentReportCrew().crew()
    result = crew_instance.kickoff(inputs=inputs)
    print("=== Final Accident Report ===")
    print(result)
