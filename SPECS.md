# Raster vector summary stats (fn-raster-vector-summary-stats)

Extract summary statistics from raster data for given polygons or points.

## Parameters

JSON object containing:

- `raster`: **Required** _{string: Base64-encoded image file or URL}_ Source raster containing values to extract.
- `subject`: **Required** _{GeoJSON FeatureCollection of Polygons or Points, URL}_ GeoJSON of polygons or points.
- `stats`: **Optional** Defaults to `mean` _{string}_ For _polygons_, pass one or more of `mean`, `max`, `min`, `mode`, `sum`, `count` separated by spaces e.g. `max mean`. Not required (and ignored) for _points_.
- `geojson_out`: **Optional** Defaults to `true` _{boolean}_. 
  - For _polygons_: If `true`, return the incoming GeoJSON with additional properties named as given in `stats`. If `false`, return an array of extracted values named as given in `stats`.
  - For _points_: If `true`, return the incoming GeoJSON with an additional property of `value`. If `false`, return an array of the extracted values.

## Constraints

- Maximum size of `polygons` is ~XX MB or ~YY polygons or ~ZZ total area in kms. Currently being determined.

## Response

See `geojson_out` above.

## Example input
An example JSON input can be found [here](https://raw.githubusercontent.com/disarm-platform/fn-raster-vector-summary-stats/master/fn-raster-vector-summary-stats/function/test_req.json)