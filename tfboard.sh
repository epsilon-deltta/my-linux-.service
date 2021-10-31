#!bin/bash
source /home/yp/anaconda3/etc/profile.d/conda.sh

conda activate tor1.9
conda env list
tensorboard --logdir=~/workspace/hdd0/tfboard/ --bind_all --port 8887