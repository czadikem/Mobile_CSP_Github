# Teaching Programy 

 With AIML there are a number of different ways for the bot to learn ( and in some cases retain ) knowledge

 * Properties. A rage of variables maintained byt he system. There are 2 types
   *Global. Available to all users, a change ( dangerous ) by one user will be reflected by all users. However changes are not persisted during bot restart. Fixed number of values. Can only be added by the bot master
     *  Changing global properties
  * Local. Local in scope to an individual client. Values lost as soon as client conversation is terminated. Unlimited in number, added to and deleted as the client interacts
  * Learn. Allow you to teach the bot a new fact, not persisted after bot restart 
 Learnf. Allow you to teach the bot a new fact, and for the information to be written as aiml file so that the fact is availanle on restart
 RDF. Support for RDF, subject -> predicate -> object triple. Allows you to store predicates and values about a specific subject.
