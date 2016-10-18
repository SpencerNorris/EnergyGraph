<h2>Prerequisites</h2>
<ul>
<li>Python 2.7+</li>
<li>A shell or bash</li>
<li>Setlr: The Semantic Extract, Transform, and Load-er (Github repo <a href=https://github.com/tetherless-world/setlr>here</a>)
</ul>

<h2>Namespaces</h2>
The following namespaces are used to refer to elements in ```energy-source-model.owl``` and ```us-state-model.owl```, respectively:
```
@prefix eg:  <http://www.semanticweb.org/energysources/> .
@prefix state: <http://www.semanticweb.org/us-state-model/> .
```
<h2>Naming Conventions</h2>
The name of the source Excel sheet is used as the prefix for all conversion products. For example, ```consumption_monthly.xls``` was cleaned of formatting separated out into separate files for each sheet; the sheet ```consumption_monthly2001-2006_FINAL.xls``` is one of the resulting files. This is then exported to ```consumption_monthly2001-2006_FINAL.csv```. Lastly, the file ```consumption_monthly2001-2006_FINAL.setl.ttl``` is used to perform the conversion of ```consumption_monthly2001-2006_FINAL.csv``` to ```consumption_monthly2001-2006_FINAL.setl.ttl```. Got it?

<h2>Energy Source Model (energy-source-model.owl)</h2>
The Energy Source Model provides a basis for defining terminology pertaining to the national energy grid. It defines class hierarchies for energy sources, sectors of consumption, and other concepts important for the domain application. It imports the Extensible Observation Ontology (OBOE) in order to provide a base model. At the moment, the class hierarchies are very barebones and don't have any additional rich semantic information beyond ```rdfs:subClassOf```; this will change as the model expands with new information.


<h2>USA State Model (us-state-model.owl)</h2>
The state model contains an OWL description of United States geography derived from the US Census Bureau's classification of states, divisions, and regions within the United States. According to this model, the US can be broken down into four regions, each of which can be broken down further into divisions and then into each of the 50 states. The model introduces the concepts Nation, Region, Division and State and uses ```state:isPartOf``` to define containment relations between instances of these classes.

<h2>RECORD OF PROCESSING STEPS</h2>
The following are steps that were performed in order to preprocess the tabular datasets and generate the final RDF.
```
1) Split workbook of national energy consumption statistics into individual spreadsheets

2) Clean spreadsheets of formatting, such as colors, comment boxes and other artifacts

3) Delete commas present in numbers and titles contained in spreadsheet

4) Change column headers to single-word strings so they can be accessed with a templating engine

5) Format time representations to appear such that they can be templated into a particular specification (e.g. translate months to numbers with one leading ‘0’ to support conformance to the xsd:gYearMonth specification)

6) Export spreadsheet content to .csv file

7) Generate .setl.ttl file to provide workflow and template to Setlr ETL capability

8) Run Setlr to generate final RDF dataset
```
I've already done all of this but recorded the steps for the sake of reproducibility. To perform the Setlr extract again (step 8), do the following:

```
$ cd /path/to/EnergyGraph/data/
$ python /path/to/Setlr/setlr.py ./setlr/consumption_monthly2001-2006_FINAL.setl.ttl
```
