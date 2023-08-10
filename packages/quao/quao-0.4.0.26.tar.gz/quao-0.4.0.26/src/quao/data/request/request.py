"""
    QuaO Project request.py Copyright © CITYNOW Co. Ltd. All rights reserved.
"""
from ..response.authentication import Authentication
from ...data.callback.callback_url import CallbackUrl


class Request:
    def __init__(self, request_data):
        self.provider_job_id = request_data.get("providerJobId")
        self.authentication = Authentication(user_token=request_data.user_token,
                                             user_identity=request_data.user_identity)
        self.user_token = request_data.get("userToken")
        self.user_identity = request_data.get("userIdentity")
        self.analysis = CallbackUrl(request_data.get("analysis"))
        self.finalization = CallbackUrl(request_data.get("finalization"))
