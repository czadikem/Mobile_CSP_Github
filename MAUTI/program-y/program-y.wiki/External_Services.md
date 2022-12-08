## Overview
External services are those services which can be called from the `sraix` tag. How to use the tag is described in [SRAIX Tag](./Template-Tags#sraix). The sraix tag was originally designed to only called other bots but I felt that this was a short-sighted limitation as the interface is about making a REST API call to an appropriate end point. Therefore with a little refactoring and better documentation you can use the sraix tag to call any external service exposed as a REST GET or POST endpoint.

** Please note that Services in 5.0 have been completely rewritten. Documentation is underway, but for now I would look at the code for services to understand how each works and how to build your own **

## Available External Services
The list of available endpoints that have been implemented and tested with Program-Y are currently 

  * Met Office
  * Wikipedia
  * Accu Weather
  * Cocktail DB
  * Dark Sky
  * Duck Duck Go
  * Generic
  * Geo Names
  * Get Guidelines
  * GNews
  * Good Reads
  * Google Distance
  * Google Directions
  * Google Geo Code
  * Microsoft News
  * Microsoft Search
  * News API
  * OMDB
  * Pandora
  * Wolfram Alpha
  * World Trading Data
  * Yelp
  * UK National Railway Enquiries



