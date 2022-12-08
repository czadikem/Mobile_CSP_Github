Version 3 introduces a completely new storage system. Prior to this version, all data was stored in text files on the local bot file system. This is the standard for most Chatbots, however, Program-Y now allows you to store your data in a number of storage engines, specifically

  * [File](./Storage_File) - Stores all data as files on the file system
  * [SQL](./Storage_SQL) - Stores all data in a series of SQL tables
  * [Mongo](./Storage_Mongo) - Stores all data as a series of JSON documents
  * [Redis](./Storage_Redis) - Used to cache user properties only
  * [Logger](./Storage_Logger) - Allows conversations to be written to system log files

Some engines such as File, SQL and Mongo allow all data to be stored in them, while others such as Redis or Logger only allow a specific data type. See each storage type for what it can store.

Each engine ships with scripts and tools to allow you to upload your text-based files into their respective storage engines. See each engine for details of how this works

# Configuration
The choice of storage is driven by configuration, for each entity type you define what storage engine to use, you then use the specific storage engine configuration to specify the specific storage options for the entity itself. 

An example is probably the best way to describe how this works. In the example below, we have a client named 'console'. In its configuration, there should be a section called 'storage', and in this section, there should then be a subsection called 'entities'. For each entity type, we specify the storage engine as 'file'

```yaml
console:
  storage:
      entities:
          categories: file
          errors: file
          duplicates: file
          learnf: file
          conversations:   file

          maps: file
          sets: file
          rdf: file

          denormal: file
          normal: file
          gender: file
          person: file
          person2: file
          regex_templates: file

          properties: file
          variables: file

          twitter: file

          spelling_corpus: file
          license_keys: file

          template_nodes: file
          pattern_nodes: file

          binaries: file
          braintree: file

          preprocessors: file
          postprocessors: file

          usergroups: file
```

In the same 'storage' section we then specify the storage engine 'file'. The name MUST match the same name as the entity storage type as above. For each entity type you specify the specific config in the 'config' subsection as follows

```yaml
      stores:

          file:
              type:   file
              config:
                categories_storage:
                  dirs: ./storage/categories
                  subdirs: true
                  extension: .aiml
                errors_storage:
                  file: ./storage/debug/errors.txt
                duplicates_storage:
                  file: ./storage/debug/duplicates.txt
                learnf_storage:
                  dirs: ./storage/categories/learnf

                conversation_storage:
                  dirs: ./storage/conversations

                sets_storage:
                  dirs: ./storage/sets
                  extension: txt
                maps_storage:
                  dirs: ./storage/maps
                  extension: txt
                rdf_storage:
                  dirs: ./storage/rdfs
                  subdirs: true
                  extension: txt

                denormal_storage:
                  file: ./storage/lookups/denormal.txt
                normal_storage:
                  file: ./storage/lookups/normal.txt
                gender_storage:
                  file: ./storage/lookups/gender.txt
                person_storage:
                  file: ./storage/lookups/person.txt
                person2_storage:
                  file: ./storage/lookups/person2.txt
                regex_storage:
                  file: ./storage/regex/regex-templates.txt

                properties_storage:
                  file: ./storage/properties/properties.txt
                defaults_storage:
                  file: ./storage/properties/defaults.txt
                variables_storage:
                  dirs: ./storage/variables

                twitter_storage:
                  dirs: ./storage/twitter

                spelling_storage:
                  file: ./storage/spelling/corpus.txt

                license_storage:
                  file: ./storage/licenses/license.keys

                pattern_nodes_storage:
                  file: ./storage/nodes/pattern_nodes.conf
                template_nodes_storage:
                  file: ./storage/nodes/template_nodes.conf

                binaries_storage:
                  file: ./storage/braintree/braintree.bin
                braintree_storage:
                  file: ./storage/braintree/braintree.xml

                preprocessors_storage:
                  file: ./storage/processing/preprocessors.conf
                postprocessors_storage:
                  file: ./storage/processing/postprocessors.conf

                usergroups_storage:
                  file: ./storage/security/usergroups.yaml
```