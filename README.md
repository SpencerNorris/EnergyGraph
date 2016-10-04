The following namespaces are used to refer to elements in ```energy-source-model.owl``` and ```us-state-model.owl```, respectively:
```
@prefix eg:  <http://www.semanticweb.org/energysources/> .
@prefix state: <http://www.semanticweb.org/us-state-model/> .
```

RECORD OF PROCESSING STEPS

1) Split workbook of national energy consumption statistics into individual spreadsheets
2) Clean spreadsheets of formatting, such as colors, comment boxes and other artifacts
3) Delete commas present in numbers and titles contained in spreadsheet
4) Change column headers to single-word strings so they can be accessed with a templating engine
5) Format time representations to appear such that they can be templated into a particular specification (e.g. translate months to numbers with one leading ‘0’ to support conformance to the xsd:gYearMonth specification)
6) Export spreadsheet content to .csv file
7) Generate .setl.ttl file to provide workflow and template to Setlr ETL capability
8) Run Setlr to generate final RDF dataset

I've already done all of this but recorded the steps for the sake of reproducibility. To perform the Setlr extract again (step 8), do the following:

```
$ cd /path/to/EnergyGraph/data/
$ python /path/to/Setlr/setlr.py ./setlr/consumption_monthly2001-2006_FINAL.setl.ttl
```
