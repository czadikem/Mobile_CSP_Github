# File Storage Engine


File Storage Engine is the default way of storing and loading data into a Program-Y, its been the defacto
storage mechanism since day 1. Each entity or groups of entities are stored in seperate text files, typically
directories specific to their data type e.g categories, maps, sets or rdf

For a list of all the entity types that are handle by storage engines see [Storage Entities](./Storage_Entities.md)

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
          defaults: file

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

Each entry is configured for either single or multiple files as follows

## Single File
For a single file, the only attribute is 'file' which is a path to the file containing the data to load

```yaml
                usergroups_storage:
                    file: ./storage/security/usergroups.yaml
```

## Multiple Files
For multiple files, there are 3 attributes
* dirs - List of directories to load all files from
* subdirs - Whether to scan all sub directories for files
* extension - Extension of the file types to load

```yaml
                categories_storage:
                  dirs: ./storage/categories
                  subdirs: true
                  extension: .aiml
```