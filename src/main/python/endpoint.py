#!/usr/bin/env python3

from rdflib import SPARQLStore


class Stardog(SPARQLStore):
	def __init__(self):
		continue		
	def query_by_energy_source(self):
		return 0

	def query_by_energy_category(self):
		return 0

	'''
	Returns the energy sources responsible for the largest generation amount 
	per state per year
	'''
	def get_largest_production_by_source():    

