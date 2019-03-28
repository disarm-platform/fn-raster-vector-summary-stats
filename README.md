## Running locally

`echo "{\"subject\": $(cat points.geojson), \"raster\": \"$(base64 tiny_raster.tif)\"}" | python3 index.py
` or `cat ./fn-raster-vector-summary-stats/function/test_req.json | python3 index.py`
 or similar is helpful.
