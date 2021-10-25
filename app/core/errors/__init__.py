"""
Error Module
"""

def handle_app_error(error):
    from flask import jsonify
    
    response = jsonify(error.to_dict())
    return response


class AppBaseException(Exception):
    def __init__(self, exception=None, status_code=None, msg=None):
        super().__init__(self)
        self.status_code = status_code if status_code else self.status_code
        self.msg = msg if msg else self.msg
        self.exception = exception

    def to_dict(self):
        return dict(status_code=self.status_code, message=self.msg)
