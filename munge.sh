#!bin/bash
SETLR_HOME=~/setlr
EG_HOME=~/courses/datasci/EnergyGraph
source ${SETLR_HOME}/venv/bin/activate

for setl in $(ls ${EG_HOME}/data/setlr/); do
	python ${SETLR_HOME}/setlr.py ${EG_HOME}/data/setlr/$setl
done
deactivate
