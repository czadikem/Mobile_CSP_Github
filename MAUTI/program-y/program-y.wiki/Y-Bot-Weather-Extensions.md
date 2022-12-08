# Overview
Uses the UK Met Office Weather API to pull together a variety of weather-related information.

## Core Grammars

* `# WEATHER # IN * #` - Ask what the weather is like in a specific location ( also supports postcodes )
* `# WEATHER TODAY` - Simplified version of the question above

The data returned can be parsed with the following pattern

```xml
    <category>
        <pattern>
            SHOW_WEATHER WEATHER * TEMP * * VISIBILITY V * VF * WIND D * DF * S * PRESSURE P * PT * PTF * HUMIDITY * *
        </pattern>
        <template>
            <think>
                <set name="weather"><star index="1" /></set>
                <set name="temp_dec"><star index="2" /></set>
                <set name="temp_frac"><star index="3" /></set>
                <set name="vis"><star index="4" /></set>
                <set name="vis_full"><star index="5" /></set>
                <set name="wind_dir"><star index="6" /></set>
                <set name="wind_dir_full"><star index="7" /></set>
                <set name="wind_speed"><star index="8" /></set>
                <set name="pressure"><star index="9" /></set>
                <set name="press_tend"><star index="10" /></set>
                <set name="press_tend_full"><star index="11" /></set>
                <set name="humid_dec"><star index="12" /></set>
                <set name="humid_frac"><star index="13" /></set>
            </think>

            <!-- User defined procecssing of above data goes here -->

        </template>
    </category>

```