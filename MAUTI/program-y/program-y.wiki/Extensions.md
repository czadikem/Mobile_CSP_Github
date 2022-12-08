# Overview
Extensions are a way of showing what Program-Y can do, they are domain specific combinations of grammar, configuration and Python code which demonstrate how to extend Program-Y for your own business. They are obviously starting points that get you started, but if you want to contact us about building a professional extension, feel free to email us on the details at the bottom of the page. We can either build the extension in its entirety or work with your development team to get them up to speed on Program-Y, AIML and Extension development.

## Available extensions

Program-Y ships with a number of extensions which are additional grammars that provide a specific set of questions and answers. A number of the extensions such as Banking, Energy etc provide a framework to build your own more detailed platform specific to the extension, whereas the more generic ones such as Weather and News provide fully constructed grammars and a range of questions and answers.

* [Banking](./Y-Bot-Banking-Extensions)
* [Energy](./Y-Bot-Energy-Extensions)
* [GeoCoding](./Y-Bot-GeoCode-Extensions)
* [Maps](./Y-Bot-Maps-Extensions)
* [News](./Y-Bot-NewsAPI-Extensions)
* [Survey](./Y-Bot-Surveys-Extensions)
* [Telecoms](./Y-Bot-Telecoms-Extensions)
* [Weather](./Y-Bot-Weather-Extensions)

## Building Your Own Extension

Inherit from the abstract base class

```python
    programy.extensions.Extension
```

This class provides a single method to implement, execute, which takes bot, clientid and data as parameters. The data parameter is a space separated set of data that comes directly from the grammar calling the extension

```python
    class Extension(object):
        __metaclass__ = ABCMeta

        @abstractmethod
        def execute(self, bot, clientid, data):
            raise NotImplemented()
```
An extension is called from within an 'extension' template tag. All text contained as child elements are passed to the Python method 'execute' as a string of words separated by spaces in the data parameter. 

The execute method returns the same, a string of words separated by spaces. This is typically passed through an srai tag the result returned words matched to a suitable pattern.
 
```xml
<category>
    <pattern>
        BANK BALANCE *
    </pattern>
    <template>
        <srai>
            SHOW_BALANCE
            <extension path="programy.extensions.banking.balance.BankingBalanceExtension">
                <star />
            </extension>
        </srai>
    </template>
</category>
```