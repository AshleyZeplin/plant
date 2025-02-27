import os
import torch
import torchvision
import numpy as np
import matplotlib.pyplot as plt
from torchvision import transforms, datasets, models
from torch.utils.data import DataLoader, Dataset
import torch.nn as nn
import torch.optim as optim
from PIL import Image

plant = "/home/amzeplin/plant_village_dataset"

print(os.listdir(plant))



class PlantVillageDataset(plant):
    def __init__(self, root_dir, transform=None):
        self.root_dir = root_dir
        self.transform = transform
        self.image_paths = []
        self.labels = []

        self.species_to_idx = {}
        self.disease_to_idx = {}

        species_list = sorted(os.listdir(root_dir))  # Get species folders
        for species_idx, species in enumerate(species_list):
            self.species_to_idx[species] = species_idx  # Assign index to species
            species_path = os.path.join(root_dir, species, "train")  # Use 'train' folder as reference
            if not os.path.exists(species_path):
                continue
            
            # Process diseases under the species
            for disease in sorted(os.listdir(species_path)):
                disease_path = os.path.join(species_path, disease)
                if os.path.isdir(disease_path):
                    if disease not in self.disease_to_idx:
                        self.disease_to_idx[disease] = len(self.disease_to_idx)

        # Populate image paths and labels
        for split in ["train", "val", "test"]:  # Load all three splits
            for species in self.species_to_idx:
                species_path = os.path.join(root_dir, species, split)
                if not os.path.exists(species_path):
                    continue
                
                for disease in self.disease_to_idx:
                    disease_path = os.path.join(species_path, disease)
                    if os.path.isdir(disease_path):
                        for img_name in os.listdir(disease_path):
                            img_path = os.path.join(disease_path, img_name)
                            self.image_paths.append(img_path)
                            self.labels.append((self.species_to_idx[species], self.disease_to_idx[disease]))

    def __len__(self):
        return len(self.image_paths)

    def __getitem__(self, idx):
        img_path = self.image_paths[idx]
        image = Image.open(img_path).convert("RGB")
        
        if self.transform:
            image = self.transform(image)

        species_label, disease_label = self.labels[idx]
        return image, torch.tensor(species_label), torch.tensor(disease_label)

