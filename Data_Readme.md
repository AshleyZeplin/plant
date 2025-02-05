# Plant Village Dataset

This is an open-sourced data set containing ~70,000 leaf-level images representing both diseased and healthy plants. This dataset consists of 9 species and each species is broken up into train-val-test data.

```
@article{hughes2015open,
  title={An open access repository of images on plant health to enable the development of mobile disease diagnostics},
  author={Hughes, David and Salath{\'e}, Marcel and others},
  journal={arXiv preprint arXiv:1511.08060},
  year={2015}
}
```

## Data Download

1. Navigate to https://www.kaggle.com/datasets/tushar5harma/plant-village-dataset-updated
2. Select the **Download** button
3. Choose the *Download dataset as zip* option
4. Once downloaded, copy the zip file path
5. Navigate to terminal
6. In local environment paste this command `scp [paste local path] cloudy:/home/[unityid]/.` 
    * fill in `[]` parts with correct information
7. Login to `cloudy`
8. Once transfer is complete, execute `unzip plant-village-dataset-updated.zip -d plant_village_dataset`

## Creating Conda Enviornment

1. Download Anaconda from here: https://www.anaconda.com/distribution/#download-section
2. Use the same secure transfer command as previously `scp [paste local path] cloudy:/home/[unityid]/.`
    * Copy the local path from Downloads folder
3. Login to `cloudy`
4. `chmod +x Anaconda3-2019.03-Linux-x86_64.sh`
    * Update with the correct file name
5. `./Anaconda3-2019.03-Linux-x86_64.sh`
    * Update with the correct file name
6. `conda config --set auto_activate_base false`
7. `conda create -n plant_vill -c pytorch -c nvidia pytorch torchvision torchaudio pytorch-cuda=11.7 seaborn matplotlib`

Then to access new environment
* `conda activate plant_vill`



## Accessing Data

Look at `data_preview.ipynb`

* Start by reviewing how the data is structured and how the PyTorch Dataset items are created
* Then start exploring the data
* Start developing!