# MSc Thesis: Multimodal Agentic System for Highway Safety Monitoring

First, clone this repository and navigate to `highway_safety_monitoring` folder:

```
git clone https://github.com/Abdulla-Almarzooqi/highway_safety_monitoring.git
cd highway_safety_monitoring
```

### Setup Instructions
    
1. Create a conda environment:

     ```
     conda create -n monitoring
     conda activate monitoring
     ```

2. Install PyTorch v2.5.1 with CUDA 12.4:

   ```
   conda install pytorch==2.5.1 torchvision==0.20.1 torchaudio==2.5.1 pytorch-cuda=12.4 -c pytorch -c nvidia
   ```

3. Install Ultralytics:

   ```
   pip install ultralytics
   ```

4. Install Hugging Face Transformers:

   ```
   pip install transformers
   ```

5. For the CrewAI installation, follow the guide [on their website](https://docs.crewai.com/installation).

## I) Driving Scene Description System

1. Download the Cityscapes dataset [from this link](https://www.cityscapes-dataset.com/downloads/). Choose the download option `leftImg8bit_trainvaltest.zip (11GB)`.

2. Download the `yolo11x.pt` model using [this direct link](https://github.com/ultralytics/assets/releases/download/v8.3.0/yolo11x.pt).

3. To run the system with all models, run the notebook `scene-description-all-models.ipynb`, which can be found under the folder `normal_implementation`.

4. To run the agentic system, use the files under the folder `agentic_implementation/scene_description` in your CrewAI directory (Note: make sure to name the CrewAI directory `scene_description`).

5. Before executing the code, make sure to adjust the paths accordingly to match your local environment.

*Note: The evaluation for this system was conducted manually.*

## II) Automatic Accident Report Generation System

1. Download the Car Crash Dataset (CCD) [from this link](https://www.kaggle.com/datasets/asefjamilajwad/car-crash-dataset-ccd).

2. To run the system with both models, run the notebooks `accident-report-gpt.ipynb` and `accident-report-internvl.ipynb`,  which can be found under the folder `normal_implementation`.

3. To run the agentic system, use the files under the folder `agentic_implementation/accident_report` in your CrewAI directory (Note: make sure to name the CrewAI directory `accident_report`). You can use the sample scenario images under the folder `sample_imgs` for testing the system.

4. Similarly, before executing the code, make sure to adjust the paths accordingly to match your local environment.

*Note: The evaluation for this system was also conducted manually.*
