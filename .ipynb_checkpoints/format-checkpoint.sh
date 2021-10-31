#!bin/bash

source /home/yp/anaconda3/etc/profile.d/conda.sh
conda activate p36
jupyter lab --port=8888 --ip=* --notebook-dir=/home/yp/workspace
