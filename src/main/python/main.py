#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Spencer Norris

from rdflib import Graph
import csv
import json
import requests
import sys, os
from endpoint import Stardog

#Local modules
import regress

#Globals
os.environ['EG_HOME'] = '.'
energy_graph = Stardog()
state_model = Graph()
source_model = Graph()

#Main processing methods
def regression():
	return 0

def process():
	return 0

def main(): 
	#Import ontologies
	state_model.parse(os.environ['EG_HOME'] + '/data/ontology/us-state-model.owl', format="rdf/xml")
	source_model.parse(os.environ['EG_HOME'] + '/data/ontology/energy-source-model.owl', format="rdf/xml")
	return 0

if __name__ == '__main__':
	sys.exit(main())
