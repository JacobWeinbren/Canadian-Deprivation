# Canadian Deprivation Map

## Sources

-   [Canadian Community Classification](https://www150.statcan.gc.ca/n1/pub/45-20-0001/452000012023001-eng.htm)
-   [Explanation](https://www150.statcan.gc.ca/n1/pub/45-20-0001/452000012023002-eng.htm)
-   [Map Tool](https://www12.statcan.gc.ca/census-recensement/2021/geo/sip-pis/boundary-limites/index2021-eng.cfm?year=21)
-   [Map Download](https://www12.statcan.gc.ca/census-recensement/alternative_alternatif.cfm?l=eng&dispext=zip&teng=lda_000b21a_e.zip&k=%20%20%20192424&loc=//www12.statcan.gc.ca/census-recensement/2021/geo/sip-pis/boundary-limites/files-fichiers/lda_000b21a_e.zip)
-   [Buildings](https://github.com/microsoft/CanadianBuildingFootprints)

## Commands

````bash
    mapshaper output/updated_canada.geojson -simplify weighted 15% -o output/simplified_canada.geojson


    node --max-old-space-size=25000 /usr/local/bin/mapshaper output/simplified_canada.geojson -clip output/merged.geojson -o precision=0.000001 output/canada_intersect.geojson
```

```bash
tippecanoe --output="output/canada-background.pmtiles" \
           --layer="maplayer" \
           --no-feature-limit \
           --no-tile-size-limit \
           --detect-shared-borders \
           --coalesce-fraction-as-needed \
           --coalesce-densest-as-needed \
           --coalesce-smallest-as-needed \
           --increase-gamma-as-needed \
           --coalesce \
           --reorder \
           --minimum-zoom=0 \
           --maximum-zoom=16 \
           --force \
           --simplification=20 \
           -x DAUID -x DGUID -x LANDAREA -x PRUID -x A -x B -x C -x D \
           "output/simplified_canada.geojson"
````

```bash
tippecanoe --output="output/canada-foreground.pmtiles" \
           --layer="maplayer" \
           --no-feature-limit \
           --no-tile-size-limit \
           --detect-shared-borders \
           --coalesce-fraction-as-needed \
           --coalesce-densest-as-needed \
           --coalesce-smallest-as-needed \
           --increase-gamma-as-needed \
           --coalesce \
           --reorder \
           --minimum-zoom=0 \
           --maximum-zoom=16 \
           --force \
           --simplification=20 \
           -x DAUID -x DGUID -x LANDAREA -x PRUID -x A_Q -x B_Q -x C_Q -x D_Q \
           "output/canada_intersect.geojson"
```
