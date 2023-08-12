#!/bin/bash

PYTHON_VER=$1
CPU=$(uname -m)


# Installing prerequisites
apt-get update && \
    apt-get install -y \
    --no-install-recommends \
    python310-venv


# # Install miniconda
# apt update && apt-get install -y --no-install-recommends \
#     software-properties-common \
#     && add-apt-repository -y ppa:deadsnakes/ppa \
#     && apt update 

# wget --quiet https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-${CPU}.sh -O ~/miniconda.sh \
#     && /bin/bash ~/miniconda.sh -b -p /opt/conda \
#     && export PATH=/opt/conda/bin:$PATH \
#     && conda init bash \
#     && conda install conda-build

# # Set environment
# . /root/.bashrc \
#     && conda create -y --name $CONDA_ENV python=$PYTHON_VER 

python3.10 -m venv $HOME/venv

echo "source $HOME/venv/bin/activate" >> ~/.bashrc

source ~/.bashrc

# Install the Python packages
pip install -U pip
pip install -r requirements/requirements.txt
