As an AIML developer, there will be times when there is not a Pattern or Template node that does what you want, or you may want to add functionality either specific to your implementation or as a short cut for one of the more verbose node types.

Program-Y provides a very extensible model for both replacing the functionality of existing nodes and also adding new nodes to further extend the functionality of AIML.

Both Pattern and Template nodes configuration are stored within a configuration file

* pattern_nodes.conf - Stores all available Pattern nodes
* template_nodes.conf - Store all available Template nodes

The system carries its own internal version of these files in case they are not included in the /config directory. Thes files should never be modifed as they can affect the operation of the program.  However, all provided core bots, Rose, Alice2, Professor and Y-Bot ship with these files. Its these files you should modify or add your own nodes as needed.

  * [Pattern Nodes](./Custom-Pattern-Nodes)
  * [Template Nodes](./Custom-Template-Nodes)


