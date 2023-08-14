from google.cloud import bigquery
from flask import Request
import datetime as dt
from collections import namedtuple
import json
from typing import List, Tuple

HTTPStatus = namedtuple('HTTPStatus', ['code', 'text'], defaults=("Ok.",))

class ValidationMixIn:

    def __init__(self, request: Request, valid_methods=None):
        self._request = request
        self.methods = valid_methods
        self._status_text = 'Ok.'
        self._status_code = 200

    @property
    def request(self):
        return self._request

    @property
    def args(self):
        return self.request.args

    def is_valid_method(self):
        if self.methods is None:
            return HTTPStatus(200)
        method = self.request.method 
        if method not in self.methods:
            return HTTPStatus(405, f"Method not allowed: {method}")
        return HTTPStatus(200)

    def has_valid_api_key(self, **kwargs) -> HTTPStatus:
        args = self.args
        if "api_key" not in args:
            return HTTPStatus(401,"Unauthorized. Variable api_key is not set") 
    
        return HTTPStatus(200) 

    def validate_date(self, key, required=False, format_str="%Y-%m-%d",  min_date=None, max_date=None):
        date = self.args.get(key)
        if date is None:
            if required:
                return HTTPStatus(
                    400,
                    f"Missing required parameter '{key}'"
                )
            else:
                return HTTPStatus(200)
        try:
            date_obj = dt.strptime(date, format_str)
        except:
            return HTTPStatus(
                400,
                f"Invalid date format: {date}"
            )

        if min_date is not None:
            if date_obj < min_date:
                return HTTPStatus(
                    400,
                    f"Invalid date: {date}"
                )

        if max_date is not None:
            if date_obj > max_date:
                return HTTPStatus(
                    400,
                    f"Invalid date: {date}"
                )

        return HTTPStatus(200)

    def limit_is_valid(self):
        limit = self.args.get('limit')

        if limit is not None:
            limit_is_valid = limit in range(1001)
            if not limit_is_valid:
                return HTTPStatus(400, f"Invalid limit: {limit}")

        return HTTPStatus(200)

    def offset_is_valid(self):
        offset = self.args.get('offset')

        if offset is not None:
            if isinstance(offset, int):
                if offset <= 0:
                    return HTTPStatus(400, f"Invalid offset: {offset}")
            else:
                return HTTPStatus(400, f"Invalid offset: {offset}")
        
        return HTTPStatus(200)

    def validate(self) -> bool:
        validation_checks = [
            self.has_valid_api_key(),
            self.is_valid_method(),
            self.limit_is_valid(),
            self.offset_is_valid()
        ]

        for c in validation_checks:
            if c.status_code != 200:
                self._status_code = c.status_code
                self._status_text = c.status_text
                return False

        return True

class QueryMixIn:

    def __init__(self, request, project_id=None):
        self._project_id = project_id
        self._request = request

    @property
    def project_id(self):
        """
        Returns the Google Cloud Project ID associated with 
        the query.

        If `self._project_id` was not set in the constructor, then 
        it's searched for in the environment variables under the 
        key "PROJECT_ID".
        """

        if self._project_id is not None:
            return self._project_id

        elif "PROJECT_ID" in os.environ:
            return os.environ['PROJECT_ID']

        else:
            raise ValueError("project_id was not set in constructor")
    
    @property
    def query(self) -> str:
        return self.generate_query().get_sql(quote_char='`')

    @property
    def query_params(self) -> List[Tuple]:
        return self.generate_query_params()

    def response_as_dataframe(self):
        client = bigquery.Client(project=self._project_id)
        job_config = bigquery.JobConfig(query_parameters=self.query_params)
        job = client.query(self.query, job_config=job_config)
        return job.to_dataframe()

    def response_as_json(self):
        df = self.response_as_dataframe()
        data = df.to_dict(orient='records')
        ts = dt.datetime.utcnow()
        response = json.dumps(
            {
                'timestamp': dt.datetime.utcnow().strftime('%Y-%M-%d %H"%M:%S'),
                'data': data
            }
        )
        return json.dumps(response)
        

    def generate_query(self) -> str:
        raise NotImplementedError()

    def generate_query_params(self) -> List[Tuple]:
        raise NotImplementedError()

class RequestHandlerBase(ValidationMixIn, QueryMixIn):

    def __init__(self, request: Request, **kwargs):
        project_id = kwargs.get('project_id')
        validation_methods = kwargs.get('validation_methods')
        ValidationMixIn.__init__(self, request, validation_methods)
        QueryMixIn.__init__(self, request, project_id)

