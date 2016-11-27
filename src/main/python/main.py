#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Spencer Norris

from rdflib import Graph, RDF
from scipy import stats, polyfit
import csv
import json
import requests
import sys, os
from endpoint import Stardog

#Local modules
#import regress

#Globals
os.environ['EG_HOME'] = '.'
energy_graph = Stardog()
state_model = Graph()
source_model = Graph()
state_model.parse(os.environ['EG_HOME'] + '/data/ontology/us-state-model/us-state-model.owl')
#source_model.parse(os.environ['EG_HOME'] + '/data/ontology/energy-source-model/energy-source-model.owl')
CONSUMPTION_URI = "http://www.semanticweb.org/energysources/EnergyConsumption"
GENERATION_URI = "http://www.semanticweb.org/energysources/EnergyGeneration"
prices = csv.reader(open('./data/tabular/PriceData_Monthly_Price_Data.csv', "r"))

#Main processing methods
'''
Perform linear regression on input arrays.
Pulled from https://docs.scipy.org/doc/scipy-0.14.0/reference/generated/scipy.stats.linregress.html
'''
def regression(x, y):
	slope, intercept, r_value, p_value, std_err = stats.linregress(x,y)
	return {
		'slope': slope,
		'intercept': intercept,
		'r_value': r_value,
		'p_value': p_value,
		'std_err': std_err	
	}

def calculate_national_green_energy_generation_price_regressions():
	source_uris = [
		"http://www.semanticweb.org/energysources/WindEnergySource",
		"http://www.semanticweb.org/energysources/SolarEnergySource",
		"http://www.semanticweb.org/energysources/GeothermalEnergySource"
	]
	month_state_price = {}
	month_state_generation = {}

	#Compile all states into list
	states = [state for state, p, o in state_model.triples( (None, RDF.type, "http://www.semanticweb.org/us-state-model/State") ) ]

	#Query EnergyGraph for all available generation data for that state
	for state in states:
		#Sum all state generation for the month
		for uri in source_uris:
			res = energy_graph.query_by_energy_source(uri, state, GENERATION_URI)
			for process, source, state, date, amount in res:
				month_state_generation[date][state] = amount

	#Read prices into dictionary
	for row in prices:
		if(int(row[1]) < 10):
			date = str(row[0]) + "-0" + str(row[1])
		else:
			date = str(row[0]) + "-" + str(row[1])
		state = energy_graph.get_state(row[2])[0]
		month_state_price[date][state] += row[3]


	#Perform regressions between price and generation for each state
	regressions = {}
	for state in states:
		x = []
		y = []

		#Iterate over dates
		year = 2005
		while year <= 2015:
			month = 1
			while month <= 12:
				if(month < 10):
					date = str(year) + "-0" + str(month)
				else:
					date = str(year) + "-" + str(month)
				#Extract generation amount and price, generate arrays for regression
				x = np.append(x, [month_state_generation[date][state]])
				y = np.append(y, [month_state_price[date][state]])
				month += 1
			year += 1
		regressions[state] = regression(x, y)
		print(regressions[state])
	return regressions


def main():
	price_generation_regressions = calculate_national_green_energy_generation_price_regressions()
	return 0

if __name__ == '__main__':
	sys.exit(main())
