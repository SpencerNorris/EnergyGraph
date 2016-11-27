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
	def __init__(self, ep=None):
		#Define the Stardog store
		if(ep is None):
			ep = 'http://localhost:5820/EnergyGraph/query'
		self.endpoint = SPARQLStore()
		self.endpoint.open((ep, ep))

    	#set prefix bindings
		self.endpoint.bind('eg', 'http://semanticweb.org/EnergyGraph/')
		self.endpoint.bind('state', 'http://semanticweb.org/us-state-model/')
		self.endpoint.bind('source', 'http://semanticweb.org/energysources/')


	'''
	Will retrieve instances of process_type, where process_type is expected to be
	source:EnergyConsumption or source:EnergyGeneration.
	source_concept identifies the class of energy source (eg:FossilFuelEnergySource, eg:Petroleum, etc).
	If num is provided, it will be the upper limit on the number of results.
	'''
	def query_by_energy_source(self, source_concept_uri, state_uri=None, process_type_uri, num=None):
		state_clause = ''
		limit_clause = ''
		if not(state_uri is None):
			state_clause = '?process prov:atLocation <%s> .' % state_uri.n3()
		if not(num is None):
			limit_clause = " LIMIT %d" % num
		rq = """
		prefix state:  <http://www.semanticweb.org/us-state-model/>
		prefix eg:	   <http://www.semanticweb.org/EnergyGraph/>
		prefix source: <http://www.semanticweb.org/energysources/>
		prefix obo:	   <http://ecoinformatics.org/oboe/oboe.1.0/oboe-core.owl#>
		prefix prov:
		SELECT ?process ?source ?state ?date ?amount WHERE{
			?process a <%s> ;
					 eg:ofEnergySource ?source .
			%s 
					 obo:hasMeasurement ?measurement ;
					 eg:date 		   ?date .
			?measurement obo:hasValue  ?amount .
			?source  a 				   <%s> .
		} %s 
		""" % process_type_uri, state_clause, source_concept_uri, limit_clause
		return [{
			'process': process,
			'source': source,
			'state': state,
			'date': date,
			'amount': amount
		} for process, source, state, date, amount in self.endpoint.query(rq)]

	#Return state URI for abbreviation
	def get_state(self, abbreviation):
		rq = """
		prefix state:  <http://www.semanticweb.org/us-state-model/>
		prefix eg:	   <http://www.semanticweb.org/EnergyGraph/>
		prefix source: <http://www.semanticweb.org/energysources/>
		prefix obo:	   <http://ecoinformatics.org/oboe/oboe.1.0/oboe-core.owl#>
		SELECT ?state WHERE{
			?state state:stateAbbreviation "%s" .
		}
		""" % abbreviation
		return [state for state in self.endpoint.query(rq)]

	'''
	Returns the energy sources responsible for the largest generation amount 
	per state per year
	'''

	'''
	def get_largest_production_by_source(self, source_concept_uri):    
		rq = """
		prefix state:  <http://www.semanticweb.org/us-state-model/>
		prefix eg:	   <http://www.semanticweb.org/EnergyGraph/>
		prefix source: <http://www.semanticweb.org/energysources/>
		prefix obo:	   <http://ecoinformatics.org/oboe/oboe.1.0/oboe-core.owl#>
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
		} for process, source, state, date, amount in self.endpoint.query(rq)]
	'''