# DELOS student prerequisites

## ML training

### Test Environment

| Module      | Type                                      |
| ----------- | ----------------------------------------- |
| CPU         | Intel(R) Core(TM) i7-7700HQ CPU @ 2.80GHz |
| GPU         | NVIDIA GeForce GTX 1060                   |
|             |                                           |
| Python      | 3.7.11                                    |
| cudatoolkit | 10.1.243                                  |
| cudnn       | 7.6.5                                     |



### Deployment

1.  Install Anaconda

2.  Create Python Virtual Environment

    `conda create -n tensorflow python=3.7`

3.  Install Tensorflow, cudatoolkit and cudnn

    `conda install tensorflow=2.3.0 cudatoolkit=10.1.243 cudnn=7.6.5`

4.  Train the model

    `python train.py`

5.  Predict new image

    `python predict.py`

6.  

