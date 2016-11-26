#!/usr/bin/env bash
SETLR_HOME=~/setlr
EG_HOME=/home/spencer/courses/datasci/EnergyGraph
source ${SETLR_HOME}/venv/bin/activate
cd ${EG_HOME}/data
for setl in $(ls ${EG_HOME}/data/setlr/); do
	echo "Munging" $setl
	python ${SETLR_HOME}/setlr.py ${EG_HOME}/data/setlr/$setl
done
deactivate
