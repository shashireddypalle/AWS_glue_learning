import os
import sys
import cx_Oracle
import numpy as np

class Oracle():
    def __init__(self, creds):

        self._user = creds['user']
        self._pw = creds['pw']
        self._connstr = creds['connection_string']
        self._port = creds['port']
        self._service_name = creds['service_name']

        self._connection = None