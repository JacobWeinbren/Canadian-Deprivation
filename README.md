# Canadian Deprivation Map

## Sources

-   [Canadian Community Classification](https://www150.statcan.gc.ca/n1/pub/45-20-0001/452000012023001-eng.htm)
-   [Explanation](https://www150.statcan.gc.ca/n1/pub/45-20-0001/452000012023002-eng.htm)
-   [Map Tool](https://www12.statcan.gc.ca/census-recensement/2021/geo/sip-pis/boundary-limites/index2021-eng.cfm?year=21)
-   [Map Download](https://www12.statcan.gc.ca/census-recensement/alternative_alternatif.cfm?l=eng&dispext=zip&teng=lda_000b21a_e.zip&k=%20%20%20192424&loc=//www12.statcan.gc.ca/census-recensement/2021/geo/sip-pis/boundary-limites/files-fichiers/lda_000b21a_e.zip)
-   [Buildings](https://github.com/microsoft/CanadianBuildingFootprints)

## Commands

````bash
    node --max-old-space-size=20000 /usr/local/bin/mapshaper output/merged.geojson -simplify weighted 20% -filter-islands -o output/simplified_buildings.geojson

    mapshaper output/updated_canada.geojson -simplify weighted 10% -o output/simplified_canada.geojson
```

```bash
tippecanoe --output="output/canada.pmtiles" --generate-ids --force --no-feature-limit --no-tile-size-limit --detect-shared-borders --coalesce-fraction-as-needed --coalesce-densest-as-needed --coalesce-smallest-as-needed --coalesce --reorder --minimum-zoom=0 --maximum-zoom=15 -x DAUID -x DGUID -x LANDAREA -x PRUID "output/simplified_canada.geojson"
````

```bash
tippecanoe --output="output/buildings.pmtiles" --generate-ids --force --no-feature-limit --no-tile-size-limit --detect-shared-borders --coalesce-fraction-as-needed --coalesce-densest-as-needed --coalesce-smallest-as-needed --coalesce --reorder --minimum-zoom=0 --maximum-zoom=15 "output/buildings_2.geojson"
```
