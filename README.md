## fn-raster-vector-summary-stats
This algorithm allows users to pass in a raster and a set of points/polygons at which to extract values. See `SPECS.md` for more details.


## Run locally
`echo "{\"subject\": $(cat points.geojson), \"raster\": \"$(base64 tiny_raster.tif)\"}" | python3 index.py
` or `cat ./fn-raster-vector-summary-stats/function/test_req.json | python3 index.py`
 or similar is helpful.
