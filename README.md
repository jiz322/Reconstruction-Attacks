# Reconstruction-Attacks

## Dataset Used
[olivetti_faces](https://www.kaggle.com/code/serkanpeldek/face-recognition-on-olivetti-dataset)

## Motivation
A well-trained machine learning model contains information of training data. If this model is disclosed to malicous users, they can retrieve these information which results in privacy leakage. By attacking a very simple face-recognizion model, we aim for a better understanding of this "Reconstruction Attack." 

## Methods

* Generative adversarial network

* Sampling Diffusion model 

## Result Using GAN
Images in the Training Set             |  Reconstructed Result
:-------------------------:|:-------------------------:
![](https://github.com/jiz322/Reconstruction-Attacks/blob/main/examples/exmaple_real_image.png) |  ![](https://github.com/jiz322/Reconstruction-Attacks/blob/main/examples/exmaple_result_gan.png)
![](https://github.com/jiz322/Reconstruction-Attacks/blob/main/examples/exmaple2_real_image.png) |  ![](https://github.com/jiz322/Reconstruction-Attacks/blob/main/examples/exmaple2_result_gan.png)


## Result of Sampling Pre-trained Diffusion
Images in the Training Set             |  Reconstructed Result
:-------------------------:|:-------------------------:
![](https://github.com/jiz322/Reconstruction-Attacks/blob/main/examples/exmaple_real_image.png) |  ![](https://github.com/jiz322/Reconstruction-Attacks/blob/main/examples/diff8.png)
![](https://github.com/jiz322/Reconstruction-Attacks/blob/main/examples/real7.png) |  ![](https://github.com/jiz322/Reconstruction-Attacks/blob/main/examples/diff7.png)
![](https://github.com/jiz322/Reconstruction-Attacks/blob/main/examples/real2.png) |  ![](https://github.com/jiz322/Reconstruction-Attacks/blob/main/examples/diff2.png)
