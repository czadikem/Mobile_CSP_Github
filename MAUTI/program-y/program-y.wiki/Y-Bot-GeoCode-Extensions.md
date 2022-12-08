# Overview
Given a post code, zipcode or a location ( time, city, state, county etc ) these grammars return latitude and longitude in a string format that can be parsed by another grammar to extra the values needed

# Core Grammars

* `POSTCODE *` - Ask for the lat/lng for a post code with no spaces, e.g KY39UR
* `POSTCODE * *` - Ask for the lat/lng for a post code with a space, e.g KY3 9UR
* `ZIPCODE *` - Given a numeric zipcode, return the lat/lng
* `LOCATION *` - For any location, town, city, state, county etc, return the lat/lng

Each of the above responds with full longitude and latitude as follows

LATITUDE DEC 56 FRAC 0720397 LONGITUDE DEC -3 FRAC 1752001

A pattern to capture this would look like

```xml
<category>
    <pattern>LATITUDE DEC * FRAC * LONGITUDE DEC * FRAC *</pattern>
    <template>
        <think>
            <set name="lat_decimal"><star index="1" /></set>
            <set name="lat_fraction"><star index="2" /></set>
            <set name="lng_decimal"><star index="3" /></set>
            <set name="lng_fraction"><star index="4" /></set>
        </think>

        <!-- User defined template logic here... -->

    </template>
</category>
