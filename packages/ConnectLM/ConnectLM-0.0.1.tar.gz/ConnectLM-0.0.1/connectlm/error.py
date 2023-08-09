class ConnectLMError(Exception):
    def __init__(
        self,
        message=None
    ):
        super(ConnectLMError, self).__init__(message)
        

class ServiceAPIError(ConnectLMError):
    def __init__(
        self,
        service_error,
        message=None
    ):
        super(ServiceAPIError, self).__init__(message)
        self._message = message
        self.service_error = service_error

    def __str__(self):
        msg = self._message or ""
        if self.service_error:
            return "ERROR: {0} {1}".format(self.service_error, msg)
        else:
            return msg
