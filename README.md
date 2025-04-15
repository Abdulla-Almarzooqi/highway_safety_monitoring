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

1. Install the Cityscapes dataset [from this link](https://www.cityscapes-dataset.com/downloads/). Choose the download option `leftImg8bit_trainvaltest.zip (11GB)`.
