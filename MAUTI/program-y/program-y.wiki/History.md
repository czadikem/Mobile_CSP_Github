In a previous life I help build a chatbot for an energy company to help answer basic customer questions and a limited number of interactions I was hugely proud of the work myself and the team did, the bot was hugely successfully, saving the company £1000's in customer support costs and was also nominated for a number of awards, once only being beaten by the Intel Team who created Stephen Hawkings voice system at the 2015 V3 Awards

That bot was based on a Python 2.x version of an AIML 1.0 interpreter that I converted to Python 3 and then heavily modified to support a wide range of additional features and capabilities. Most of which have now been added to AIML 2.0 spec. However no one has yet built a fully functional Python 3.x interpreter, hence this project.

Unfortunately, the people in charge did not see ( or comprehend ) the value of long-term investment in the platform both to keep it relevant as new conversations were needed as the business grew and also as a team we became more experience in how our customers interacted with our platform. It's now a shadow of its former self, with poor comprehension and responsiveness

So I started from scratch and decided it was be a great experience to build an AIML 2.x fully compliant Bot, again in Python but built using proper software engineering standards and covered from day 1 by comprehensive unit and integration tests. This is Program-Y

Right now it implements about 100% of the AIML spec. This version also supports one additional grammar < extension >, which allows you to call native Python classes, similar in a way that the sraix tag works.

Over time I intend to write a full AIML 2.0 tutorial as well as comprehensive documentation for using this version of program-y

Enjoy and please leave any feedback for me and I'll get back to you. Keiff