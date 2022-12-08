# SQL Storage Engine

The SQL Storage engine is the one of the newer ways of storing and loading data into a Program-Y bot. Each entity type 
is stored in its own SQL table

For a list of all the entity types that are handle by storage engines see [Storage Entities](./Storage_Entities.md)

```yaml
  storage:
      entities:
          users: sql
          linked_accounts: sql
          links: sql

          categories: sql
          errors: sql
          duplicates: sql
          learnf: sql
          conversations:   sql

          maps: sql
          sets: sql
          rdf: sql

          denormal: sql
          normal: sql
          gender: sql
          person: sql
          person2: sql
          regex_templates: sql

          properties: sql
          defaults: sql

          twitter: sql

          spelling_corpus: sql
          license_keys: sql

          template_nodes: sql
          pattern_nodes: sql

          binaries: sql
          braintree: sql

          preprocessors: sql
          postprocessors: sql

          usergroups: sql

      stores:
          sql:
              type:   sql
              config:
                  url: mysql+pymysql://root:password123@localhost:32773/programy
                  echo: false
                  encoding: utf-8
                  create_db: false
                  drop_all_first: false

```

## Pre Loading SQL Database**

Typically you can start with a set of data files and when you are ready to load them into SQL tables and switch
to a SQL Storage Engine you can use the following scripts to load all the data from a file directory structure

```bash
#!/usr/bin/env bash

export PYTHONPATH=../../../program-y/src

# Categories
#python3 -m programy.storage.stores.sql.loader --entity categories --url mysql+pymysql://root:password123@localhost:32773/programy --dir ../../storage/categories --subdir --extension=.aiml --verbose

# Maps
#python3 -m programy.storage.stores.sql.loader --entity maps --url mysql+pymysql://root:password123@localhost:32773/programy --dir ../../storage/maps --subdir --extension=.txt --verbose

# Sets
#python3 -m programy.storage.stores.sql.loader --entity sets --url mysql+pymysql://root:password123@localhost:32773/programy --dir ../../storage/sets --subdir --extension=.txt --verbose

# RDFs
#python3 -m programy.storage.stores.sql.loader --entity rdfs --url mysql+pymysql://root:password123@localhost:32773/programy --dir ../../storage/rdfs --subdir --extension=.txt --verbose

# Lookups
#python3 -m programy.storage.stores.sql.loader --entity denormals --url mysql+pymysql://root:password123@localhost:32773/programy --file ../../storage/lookups/denormal.txt --verbose
#python3 -m programy.storage.stores.sql.loader --entity normals --url mysql+pymysql://root:password123@localhost:32773/programy --file ../../storage/lookups/normal.txt --verbose
#python3 -m programy.storage.stores.sql.loader --entity genders --url mysql+pymysql://root:password123@localhost:32773/programy --file ../../storage/lookups/gender.txt --verbose
#python3 -m programy.storage.stores.sql.loader --entity persons --url mysql+pymysql://root:password123@localhost:32773/programy --file ../../storage/lookups/person.txt --verbose
#python3 -m programy.storage.stores.sql.loader --entity person2s --url mysql+pymysql://root:password123@localhost:32773/programy --file ../../storage/lookups/person2.txt --verbose

# Properties
#python3 -m programy.storage.stores.sql.loader --entity properties --url mysql+pymysql://root:password123@localhost:32773/programy --file ../../storage/properties/properties.txt --verbose
#python3 -m programy.storage.stores.sql.loader --entity defaults --url mysql+pymysql://root:password123@localhost:32773/programy --file ../../storage/properties/defaults.txt --verbose

# Regex Templates
#python3 -m programy.storage.stores.sql.loader --entity regexes --url mysql+pymysql://root:password123@localhost:32773/programy --file ../../storage/regex/regex-templates.txt --verbose

# Nodes
#python3 -m programy.storage.stores.sql.loader --entity patternnodes --url mysql+pymysql://root:password123@localhost:32773/programy --file ../../storage/nodes/pattern_nodes.conf --verbose
#python3 -m programy.storage.stores.sql.loader --entity templatenodes --url mysql+pymysql://root:password123@localhost:32773/programy --file ../../storage/nodes/template_nodes.conf --verbose

# Processors
#python3 -m programy.storage.stores.sql.loader --entity postprocessors --url mysql+pymysql://root:password123@localhost:32773/programy --file ../../storage/processing/postprocessors.conf --verbose
#python3 -m programy.storage.stores.sql.loader --entity preprocessors --url mysql+pymysql://root:password123@localhost:32773/programy --file ../../storage/processing/preprocessors.conf --verbose

# Spelling
#python3 -m programy.storage.stores.sql.loader --entity spelling --url mysql+pymysql://root:password123@localhost:32773/programy --file ../../storage/spelling/corpus.txt --verbose

# License Keys
#python3 -m programy.storage.stores.sql.loader --entity licenses --url mysql+pymysql://root:password123@localhost:32773/programy --file ../../storage/licenses/license.keys --verbose

# UserGroups
#python3 -m programy.storage.stores.sql.loader --entity usergroups --url mysql+pymysql://root:password123@localhost:32773/programy --file ../../storage/security/usergroups.yaml --verbose

```