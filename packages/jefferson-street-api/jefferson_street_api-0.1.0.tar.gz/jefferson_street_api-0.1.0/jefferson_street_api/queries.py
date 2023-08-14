from pypika import Query, Parameter, Database

def fred_observations(obs, start_date=None, end_date=None, id_filter=None, limit=None, offset=None, version_filter=None, **kwargs):
    '''
    Cookiecutter query for 
    '''
    cols = [
        obs.series_id,
        obs.observation_date,
        obs.realtime_start.as_('release_date'),
        obs.value
    ]

    q = Query.from_(obs).select(*cols)
    query_params = []

    if start_date is not None:
        q = q.where(obs.observation_date >= Parameter('@start_date'))
        query_params.append(bigquery.ScalarQueryParameter("start_date", "STRING", start_date))

    if end_date is not None:
        q = q.where(obs.observation_date <= Parameter('@end_date'))
        query_params.append(bigquery.ScalarQueryParameter("end_date", "STRING", end_date))

    if id_filter is not None:
        ids = [x.replace(' ', '') for x in id_filter.split(',')]
        q = q.where(obs.series_id.isin(ids))

    if version_filter == 'original':
        q = q.where(obs.earliest_observation_flag == True)
    else:
        q = q.where(obs.latest_observation_flag == True)

    if limit is None:
        limit = 1000

    q = q.limit(Parameter('@limit'))
    query_params.append(bigquery.ScalarQueryParameter('limit', 'INT64', limit))

    if offset is not None:
        q = q.offset(Parameter('@offset'))
        query_params.append(bigquery.ScalarQueryParameter('offset', 'INT64', offset))

    return q, query_params
