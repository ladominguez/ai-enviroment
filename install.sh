#!/bin/bash

set -e

echo "===================================="
echo "Creating AI environment"
echo "===================================="

mamba env create -f environment.yml

source "$(conda info --base)/etc/profile.d/conda.sh"

conda activate ai

pip install -r requirements.txt

python -m ipykernel install \
    --user \
    --name ai \
    --display-name "Python (AI)"

echo
echo "Installation complete."
