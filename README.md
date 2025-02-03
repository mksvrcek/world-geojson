Work in Progress - Data based on [georgique/world-geojson](https://github.com/georgique/world-geojson) and [janic0/world-geojson](https://github.com/janic0/world-geojson)

# World boundaries in GeoJSON format
Countries based on UN data, including all territories with assigned ISOA2 codes.

Project Progress & Planned Updates:
- All countries (inc. Properties)
- All territories (inc. Properties)
- Swift Package for apple development
- JS Package

Properties included with countries & territories:
- "sov" (required): UN designated sovreignty in ISOA2 format. In case of country = country itself, in case of territory = parent country unless independent.
- "type" (required): UN / Dep - Describes wheter the entry is a country or a dependency.
- "name" (required): Full length name of the country/territory in English  
- "capital" (required): The capital city of the country (if multiple first alphabetically others will be included in a separate variable later on)
- "continent" (required): The geographical continent it is located in (Asia / Africa / Europe / North America / South America / Oceania)
- "label_x" (required): The longitude of the country / territory label, consistent with Apple Maps.
- "label_y" (required): The latitude of the country / territory label, consistent with Apple Maps.
- "version" (required): Version of the country / territory file.
