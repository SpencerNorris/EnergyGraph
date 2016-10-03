Setlr files use following prefix to denote references to classes defined in energy-source-model.owl:
@prefix eg:  <http://semanticweb.org/energysources> .


RECORD OF PROCESSING STEPS

1) Tabular data initially represented as Excel workbooks. Stripping the different sheets out into their own files.

2) Blowing away comments, colors, etc. in tables to prevent any wonkiness when exporting to csv.

3) Changing "TYPE OF PRODUCER" to "SECTOR_NAME" for consistency between sheets, make Setlr files cleaner when defining pipeline.

4) Removing commas from "CONSUMPTION", "SECTOR_NAME" columns to make sure CSV is well-formed.


ONTOLOGY
Generating model for different types of energy sources
Generating instance data for different states in the US
