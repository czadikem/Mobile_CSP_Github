#Mongo Storage Engine

The Mongo Storage engine is the one of the newer ways of storing and loading data into a Program-Y bot. Each entity type 
is stored in its own Mongo JSON document

For a list of all the entity types that are handle by storage engines see [Storage Entities](./Storage_Entities.md)

```yaml
  storage:
      entities:
          users: mongo
          linked_accounts: mongo
          links: mongo

          categories: mongo
          errors: mongo
          duplicates: mongo
          learnf: mongo
          conversations:   mongo

          maps: mongo
          sets: mongo
          rdf: mongo

          denormal: mongo
          normal: mongo
          gender: mongo
          person: mongo
          person2: mongo
          regex_templates: mongo

          properties: mongo
          defaults: mongo

          twitter: mongo

          spelling_corpus: mongo
          license_keys: mongo

          template_nodes: mongo
          pattern_nodes: mongo

          binaries: mongo
          braintree: mongo

          preprocessors: mongo
          postprocessors: mongo

          usergroups: mongo

      stores:

          mongo:
              type:   mongo
              config:
                  url: mongodb://localhost:32768/
                  database: programy
                  drop_all_first: false
```


## Pre Loading Mongo Database

Typically you can start with a set of data files and when you are ready to load them into Mongo documents and switch
to a Mongo Storage Engine you can use the following scripts to load all the data from a file directory structure


```bash
#!/usr/bin/env bash

export PYTHONPATH=../../../program-y/src

# Clear the entire database
#python3 -m programy.storage.stores.nosql.mongo.loader --url mongodb://localhost:32768/ -a -b programy --verboseX

# Categories
python3 -m programy.storage.stores.nosql.mongo.loader --entity categories --url mongodb://localhost:32768/ -b programy --dir ../../storage/categories --subdir --extension=.aiml --verboseX

# Maps
python3 -m programy.storage.stores.nosql.mongo.loader --entity maps --url mongodb://localhost:32768/ -b programy --dir ../../storage/maps --subdir --extension=.txt --verboseX

# Sets
python3 -m programy.storage.stores.nosql.mongo.loader --entity sets --url mongodb://localhost:32768/ -b programy --dir ../../storage/sets --subdir --extension=.txt --verboseX

# RDFs
python3 -m programy.storage.stores.nosql.mongo.loader --entity rdfs --url mongodb://localhost:32768/ -b programy --dir ../../storage/rdfs --subdir --extension=.txt --verboseX

# Lookups
python3 -m programy.storage.stores.nosql.mongo.loader --entity denormals --url mongodb://localhost:32768/ -b programy --file ../../storage/lookups/denormal.txt --verboseX
python3 -m programy.storage.stores.nosql.mongo.loader --entity normals --url mongodb://localhost:32768/ -b programy --file ../../storage/lookups/normal.txt --verboseX
python3 -m programy.storage.stores.nosql.mongo.loader --entity genders --url mongodb://localhost:32768/ -b programy --file ../../storage/lookups/gender.txt --verboseX
python3 -m programy.storage.stores.nosql.mongo.loader --entity persons --url mongodb://localhost:32768/ -b programy --file ../../storage/lookups/person.txt --verboseX
python3 -m programy.storage.stores.nosql.mongo.loader --entity person2s --url mongodb://localhost:32768/ -b programy --file ../../storage/lookups/person2.txt --verboseX

# Properties X
python3 -m programy.storage.stores.nosql.mongo.loader --entity properties --url mongodb://localhost:32768/ -b programy --file ../../storage/properties/properties.txt --verboseX

# Defaults X
python3 -m programy.storage.stores.nosql.mongo.loader --entity defaults --url mongodb://localhost:32768/ -b programy --file ../../storage/properties/defauls.txt --verboseX

# Regex Templates X
python3 -m programy.storage.stores.nosql.mongo.loader --entity regexes --url mongodb://localhost:32768/ -b programy --file ../../storage/regex/regex-templates.txt --verboseX

# Nodes
python3 -m programy.storage.stores.nosql.mongo.loader --entity patternnodes --url mongodb://localhost:32768/ -b programy --file ../../storage/nodes/pattern_nodes.conf --verboseX
python3 -m programy.storage.stores.nosql.mongo.loader --entity templatenodes --url mongodb://localhost:32768/ -b programy --file ../../storage/nodes/template_nodes.conf --verboseX

# Processors
python3 -m programy.storage.stores.nosql.mongo.loader --entity postprocessors --url mongodb://localhost:32768/ -b programy --file ../../storage/processing/postprocessors.conf --verboseX
python3 -m programy.storage.stores.nosql.mongo.loader --entity preprocessors --url mongodb://localhost:32768/ -b programy --file ../../storage/processing/preprocessors.conf --verboseX

# Spelling
python3 -m programy.storage.stores.nosql.mongo.loader --entity spelling --url mongodb://localhost:32768/ -b programy --file ../../storage/spelling/corpus.txt --verboseX

# License Keys
python3 -m programy.storage.stores.nosql.mongo.loader --entity licenses --url mongodb://localhost:32768/ -b programy --file ../../storage/licenses/license.keys --verboseX

# UserGroups
python3 -m programy.storage.stores.nosql.mongo.loader --entity usergroups --url mongodb://localhost:32768/ -b programy --file ../../storage/security/usergroups.yaml --verboseX
```