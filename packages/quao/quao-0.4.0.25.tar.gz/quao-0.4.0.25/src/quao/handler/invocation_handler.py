"""
    QuaO Project invocation_handler.py Copyright © CITYNOW Co. Ltd. All rights reserved.
"""

from ..component.backend.backend import Backend
from ..data.request.invocation_request import InvocationRequest
from ..handler.handler import Handler


class InvocationHandler(Handler):
    def __init__(self, request_data: dict):
        super().__init__(request_data)

    def invoke(self, circuit_preparation_fn, post_processing_fn):
        """

        @param post_processing_fn: post processing function
        @param circuit_preparation_fn: circuit preparation function
        @return:
        """

        invocation_request = InvocationRequest(self.request_data)

        backend = Backend(invocation_request)

        backend.submit_job(circuit_preparation_fn=circuit_preparation_fn,
                           post_processing_fn=post_processing_fn)
