

## Example File Based Storage
```yaml
        console:
            storage:
                entities:
                    users: sqlite
                    linked_accounts: sqlite
                    links: sqlite
                    
                    categories: file
                    errors: file
                    duplicates: file
                    learnf: file

                    conversations: file

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
                
                stores:
                    sqlite:
                        type:   sql
                        config:
                            url: sqlite:///:memory
                            echo: false
                            encoding: utf-8
                            create_db: true
                            drop_all_first: true
            
                    mongo:
                        type:   mongo
                        config:
                            url: mongodb://localhost:27017/
                            database: programy
                            drop_all_first: true
            
                    redis:
                        type:   redis
                        config:
                            host: localhost
                            port: 6379
                            password: None
                            db: 0
                            prefix: programy
                            drop_all_first: True            
                
                    file:
                        type:   file
                        config:
                            properties_storage: 
                                dir: ./storage/properties
                            conversation_storage: 
                                dir: ./storage/conversations
            
                    logger:
                        type:   logger
                        config:
                            conversation_logger: conversation

```