#!/usr/bin/env bash

#Creates a conda environment, sets it up and runs the main script for the regression analyses


#Check if conda environment exists, make one if it doesn't
#Substring check from http://stackoverflow.com/questions/229551/string-contains-in-bash
if [[ ! $(conda info --envs) == *"EnergyGraph"* ]]
then
  conda create -n EnergyGraph
fi

#Activate and set up environment
source activate EnergyGraph
pip install rdflib
easy_install SPARQLWrapper
conda install statsmodels --yes
conda install requests --yes

#Execute script and deactivate environment
python ./src/main/python/main.py
source deactivate
