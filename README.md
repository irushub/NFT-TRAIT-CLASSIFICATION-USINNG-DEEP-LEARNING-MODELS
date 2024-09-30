# NFT Trait Classification using Deep Learning Models (CNN and ANN)

This project explores the application of Convolutional Neural Networks (CNNs) and Artificial Neural Networks (ANNs) for NFT trait classification. The goal is to evaluate and compare the effectiveness of these machine learning models in identifying and classifying distinct features within NFT images.

## Abstract

This repository contains code for NFT trait classification using CNNs and ANNs. The project investigates the ability of these models to classify traits from NFT images. By analyzing their performance, the project provides insights into which model is better suited for this task.

### Key Aspects
- **Data Acquisition and Preprocessing**: NFT images are collected, resized, normalized, and augmented for model training.
- **Model Architectures**: CNN and ANN models are developed for trait classification. The CNN leverages pre-trained architectures like VGG16, while the ANN is built with multiple hidden layers.
- **Model Training and Evaluation**: Both models are trained with appropriate optimizers and loss functions, and performance is evaluated on unseen NFT images.
- **Comparative Analysis**: The performance of CNN and ANN models is compared, highlighting their strengths and weaknesses.
- **Discussion and Future Work**: Insights into the models’ performance and suggestions for future research.

## Introduction

Non-Fungible Tokens (NFTs) represent unique digital assets, often with distinct visual traits contributing to their value. Identifying these traits accurately can support various NFT-related applications like market analysis or automated trading strategies.

This project applies CNNs, known for their superior image recognition abilities, and ANNs, for a broader approach to classification, to the task of NFT trait classification. By comparing the performance of these models, the project aims to provide insights into their effectiveness in this domain.

## Proposed Method

1. **Data Acquisition**:
   - **Target Blockchain**: NFTs are collected from networks like Ethereum or Solana.
   - **Collection Selection**: Specific NFT collections are selected based on popularity or traits of interest.
   - **Data Gathering**: Scripts are used to fetch NFT metadata (image URLs and trait details) using libraries like `requests` and `web3.py`.
   - **Image Downloading**: Images are downloaded, and error handling is implemented to manage missing URLs.

2. **Data Labeling**:
   - **Automated Labeling**: Metadata is parsed, and images are moved into folders based on their traits (e.g., "Eye Color" -> "Blue", "Brown").

3. **Data Preprocessing**:
   - Images are resized for consistency and normalized to improve model training.
   - Data augmentation is applied (cropping, flipping) to enhance generalization.

4. **Model Training**:
   - **Model Selection**: A CNN (e.g., VGG16) and an ANN with multiple hidden layers are used.
   - **Training**: The dataset is split into training/validation sets, and models are trained with optimizers like Adam and loss functions like categorical crossentropy.

5. **Model Evaluation**:
   - The models are evaluated on a test dataset using metrics like accuracy, precision, recall, and F1-score.

## Experimental Results

- **CNN Performance**: Achieved 99% accuracy, demonstrating its effectiveness in NFT trait classification.
![image](https://github.com/user-attachments/assets/55c56338-376a-4259-a967-a7c56b38fd44)


- **ANN Performance**: Achieved 60% accuracy, showing its limitations compared to CNNs.
![image](https://github.com/user-attachments/assets/8229a370-00ae-497d-bdce-b49b408aa23f)

## Conclusion

CNNs significantly outperform ANNs in NFT trait classification, achieving 99% accuracy compared to 60% for ANNs. The CNN's ability to extract visual features and leverage pre-trained models makes it the ideal choice for tasks with limited data, common in NFT collections.


