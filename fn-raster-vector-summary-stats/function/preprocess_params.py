from preprocess_helpers import write_temp_from_url_or_base64, required_exists


def preprocess(params: dict):
    required_exists('subject', params)
    write_temp_from_url_or_base64('subject', params)

    required_exists('raster', params)
    write_temp_from_url_or_base64('raster', params)

    if 'geojson_out' in params:
        if type(params['geojson_out']) is not bool:
            raise ValueError('`geojson_out` needs to be a boolean')

    # params['stats'] if exists must match the possible options
    if 'stats' in params:
        stats = params['stats']
        all_possible_options = ['min', 'max', 'mean', 'count', 'sum', 'std', 'median', 'majority', 'minority', 'unique', 'range', 'nodata']

        for stat in stats.split(' '):
            if stat not in all_possible_options:
                raise ValueError(f'Unsupported `stat` parameter of "{stat}"')
