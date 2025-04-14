# MSc Thesis: Multimodal Agentic System for Highway Safety Monitoring

First, clone this repository and navigate to `agentic_highway_safety_monitoring` folder:

```
git clone https://github.com/Abdulla-Almarzooqi/agentic_highway_safety_monitoring.git
cd agentic_highway_safety_monitoring
```

### Setup Instructions
    
1. Create a conda environment:

     ```
     conda create -n monitoring
     conda activate monitoring
     ```

2. Install PyTorch v[[[[[[[1.13.1 with CUDA 11.6:

   ```
   conda install pytorch==2.0.0 torchvision==0.15.0 torchaudio==2.0.0 pytorch-cuda=11.7 -c pytorch -c nvidia
   ```

3. Install Ultralytics:

   ```
   pip install ultralytics
   ```

## I) Driving Scene Description System


1. Install the dataset [from this link](https://www.cityscapes-dataset.com/downloads/). Choose the download option `leftImg8bit_trainvaltest.zip (11GB)`.
