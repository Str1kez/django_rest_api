from rest_framework.exceptions import APIException


class ExistsInDatabase(APIException):
    status_code = 405
    default_detail = 'Similar item exists in database'
    default_code = 'exists_in_database'
