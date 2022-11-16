# Reconstruction-Attacks

## Dataset Used
[olivetti_faces](https://www.kaggle.com/code/serkanpeldek/face-recognition-on-olivetti-dataset)

## Motivation
A well-trained machine learning model contains information of training data. If this model is disclosed to malicous users, they can retrieve these information which results in privacy leakage. 

## Methods

* GAN

* Diffusion

## Result Using GAN

The image below is a target to attack. \
Solarized dark             |  Solarized Ocean
:-------------------------:|:-------------------------:
![](https://github.com/jiz322/Reconstruction-Attacks/blob/main/examples/exmaple_real_image.png) |  ![](https://github.com/jiz322/Reconstruction-Attacks/blob/main/examples/exmaple_result_gan.png)



The image below is generated by our generator by maximizing the target possibility of predictive model. \



Below is another pairs of result. \

![alt text](https://github.com/jiz322/Reconstruction-Attacks/blob/main/examples/exmaple2_result_gan.png)

![alt text](https://github.com/jiz322/Reconstruction-Attacks/blob/main/examples/exmaple2_real_image.png)