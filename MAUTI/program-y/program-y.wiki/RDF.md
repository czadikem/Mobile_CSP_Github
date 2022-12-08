# Resource Descriptor Framework (RDF) Support

This is probably one of the most poorly understood parts of any AIML chat bot. Added by Pandora bots and visible in the Alice2 AIML set, there is little or no documentation on the tags available to support RDF, but is one of the most powerful features once you get your head around it.

AIML implements RDF support in the form of triples, and Alice2 shops with a files triples.txt as part of the overall substitution files. It also shops with a number of aiml grammars that make use of the triples.txt and associated aiml tags addtriple, deletetriple, select, tuple and uniq.

This section of the Wiki is initially my notes on trying to decypher how it works, and also once implemented how you can make use of it.

## What is RDF
Resource Descriptor Framework or RDF is a W3C standard for representing information on the web. For details of the spec see [RDF Concepts And Abstract Syntax](https://www.w3.org/TR/2004/REC-rdf-concepts-20040210/)

An RDF entity consists of 3 elements, usually referred to as a Triple. Each triple represents a statement of a relationship between the things denoted by the nodes that it links. Each triple has three parts:

* a subject,
* an object, and
* a predicate (also called a property) that denotes a relationship.

## AIML Triples File
AIML allows the user to store RDF data in the form of triples. Triple is a single line of text, containing the Subject, Predicate and Object seperated by colon ':'. e.g
```
AIRPLANE:hasPurpose:to transport us through the air
AIRPLANE:hasSize:9
AIRPLANE:hasSpeed:12
AIRPLANE:hasSyllables:1
AIRPLANE:isa:Aircraft
AIRPLANE:isa:Transportation
AIRPLANE:lifeArea:Physical
```
In this example, we see the RDF definition of an airplane, which has a number of properties (predicates), each of which has a value (object)

In this format, we can create a body of knowledge about any entity for which we can identify a range of properties and their values

See config\triples.txt for many more examples of the format and content of the data

## AIML RDF Tags
AIML2 introduces a number of tags that support the creation, deletion, and querying of RDF data
* addtriple
* deletetriple
* select
* uniq
As well as modifying the get tag to handle the data, RDF support also seems to have introduced 2 new tags to handle list processing
* first
* rest

### Loading Data
As described above AIML 2 and therefore Program-Y uses the triples file define in the config as follows
```yaml
brain:
    files:
        triples: $BOT_ROOT/config/triples.txt
```

### Creating Data
In addition to loading data at startup you can dynamically create new triples during program exeuction with the add triple tag
```xml
<addtriple>
  <subj>Subject</subj><pred>Predicate</pred><obj>Object</obj>
</addtriple>
```
The follow example shows how to add characteristics of animals to the RDF set
```xml
<addtriple>
  <subj>cow</subj><pred>sound</pred><obj>moo</obj>
</addtriple>
<addtriple>
  <subj>dog</subj><pred>sound</pred><obj>woof</obj>
</addtriple>
```
Warning, this data is not persistent and will be list when the program exits

### Deleting Data
You can delete any RDF triple stored in memory with the deletetriple tag. This can delete not just those added with addtriple, but also those loaded through the triples file.
```xml
<deletetriple>
  <subj></subj><pred></pred><obj></obj>
</deletetriple>
```
If specify all three element it will delete that specific triple only if all three elements match
If specify only subject and predicate then it will still delete that single triple, but regardless of the value of the object
If you specify just the subject then all triples for that subject will be deleted

### Querying Data

#### Simple Query
The simplest form of query is define the values of all three elements of the RDF triple; subject, predicate and object.
```xml
<select>
    <q><subj></subj><pred></pred><obj></obj></q>
</select>
```
If match if made, then the Subject is returned as proof of discovery

#### Simple Query with Variables
If you want to return more than a single variable or receive a list of elements which match you need to use variables.Variables are defined between the var tag and are always proceeded with the ?. The variables are then specified in the query. 
```xml
<select>
    <vars>?x ?y .... </vars>
    <q><subj></subj><pred></pred><obj></obj></q>
</select>
```
A variable allows you to get all combinations of triples that match the specified data and then the variables allow you to see every combination of data that matched

As an example, we want to query all animals and how many legs they have
```xml
<select>
    <vars>?x ?y</vars>
    <q><subj>?x</subj><pred>legs</pred><obj>?y</obj></q>
</select>
```
If the appropriate data is available we might receive the following data
MONKEY 2
BIRD 2
LION 4
ZEBRA 4
This would actually be returned as a single string as follows, to enable further SRAI processing to take place.
```xml
MONKEY 2 BIRD 2 LION 4 ZEBRA 4
```

#### Complex Queries
If you need to form more complex queries then RDF support allows you to chain multiple queries together, each one is combined as an 'and' query. We can also see below that there are 2 types of queries
* q - Returns results that match the parameters
* notq - Returns results that do not match the parameters
```xml
<select>
    <vars>?x ?y .... </vars>
    <q><subj></subj><pred></pred><obj></obj></q>
    <notq><subj></subj><pred></pred><obj></obj></notq>
</select>
```

#### Fetching Data
The 'tuple' element is always a child of the 'get' element as follows, and allows you to query data that was previously generated from an RDF 'select' element

```xml
<get var="?x">
    <tuple>
        <first><get var="tuples" /></first>
    </tuple>
</get>
```

If this instance, the 'vars' attribute of get defines which variables to return from elements of the tuple list

The <tuple> tag then tells the parser to conver the value of the text data from a json/pickle encoding of the array of objects returned into an actual array

The encoding to json/pickle is done in the <select> tag, which takes the array of objects found in the search and converts them to either a json representation or a binary version via pickle

A select element is used like an SQL SELECT statement to create a data set This is typically included inside a 'set' element to set a variable as defined above and shown as an example below

```xml
<set var="tuples>
    <select>
        <vars>?x ?y</vars>
        <q><subj></subj><pred></pred><obj></obj></q>
    </select>
</set>
```

## Sources of RDF Data
There are lots of sources of RDF data on the web, the following are a few links that I have found. The data is in many different raw formats, but the intention is to provide a suite of tools to convert them into subject:predicate:object file format to load into Program-Y

* [DataSetRDFDumps](https://www.w3.org/wiki/DataSetRDFDumps)
* [RDFDATA.org](http://www.rdfdata.org/)
* [Mozilla RDF Sources](https://www-archive.mozilla.org/docs/ora-oss2000/chatzilla/rdfds.html)

Most of these are index pages which references lots of different rdf files of data.