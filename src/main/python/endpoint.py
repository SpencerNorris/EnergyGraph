#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Spencer Norris

'''
An implementation of a SPARQLStore interface for interacting with a Stardog endpoint.
This version contains queries aimed at utilizing the EnergyGraph dataset.
Solution derived from https://lawlesst.github.io/notebook/rdflib-stardog.html .
'''


from rdflib.plugins.stores.sparqlstore import SPARQLStore


class Stardog(SPARQLStore):
	def __init__(ep=None):
		#Define the Stardog store
		if(ep is None):
			ep = 'http://localhost:5820/demo/query'
		endpoint = sparqlstore.SPARQLStore()
		endpoint.open((ep, ep))

    	#set prefix bindings
		endpoint.bind('eg', 'http://semanticweb.org/EnergyGraph/')
		endpoint.bind('state', 'http://semanticweb.org/us-state-model/')
		endpoint.bind('source', 'http://semanticweb.org/energysources/')


	'''
	Will retrieve instances of process_type, where process_type is expected to be
	source:EnergyConsumption or source:EnergyGeneration.
	source_concept identifies the class of energy source (eg:FossilFuelEnergySource, eg:Petroleum, etc).
	If num is provided, it will be the upper limit on the number of results.
	'''
    #TODO: FIX OBO PREFIX
	def query_by_energy_source(self, source_concept_uri, state_uri, process_type_uri, num=None):
		rq = """
		prefix state:  <http://www.semanticweb.org/us-state-model/>
		prefix eg:	   <http://www.semanticweb.org/EnergyGraph/>
		prefix source: <http://www.semanticweb.org/energysources/>
		prefix obo:	   <OBO_PREFIX>
		SELECT ?process ?source ?state ?date ?amount WHERE{
			?process a %s ;
					 eg:ofEnergySource ?source ;
					 state:ofState	   %s ;
					 obo:hasMeasurement ?measurement ;
					 eg:date 		   ?date .
			?measurement obo:value	   ?amount .
			?source  a 				   %s .
		}
		""" % process_type_uri, state_uri, source_concept_uri
		if not(num is None):
			rq += " LIMIT %d" % num
		return [{
			'process': process,
			'source': source,
			'state': state,
			'date': date,
			'amount': amount
		} for process, source, state, date, amount in endpoint.query(rq)]


	'''
	Returns the energy sources responsible for the largest generation amount 
	per state per year
	'''
	def get_largest_production_by_source(self, source_concept_uri):    
		pass
