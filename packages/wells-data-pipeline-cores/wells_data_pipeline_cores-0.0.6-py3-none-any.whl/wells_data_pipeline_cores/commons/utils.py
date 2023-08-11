from datetime import datetime
from dateutil import parser
import pytz

from typing import (
    Text,
    Any
)

import warnings
import contextlib

import requests
from urllib3.exceptions import InsecureRequestWarning

old_merge_environment_settings = requests.Session.merge_environment_settings

@contextlib.contextmanager
def no_ssl_verification():
    opened_adapters = set()

    def merge_environment_settings(self, url, proxies, stream, verify, cert):
        # Verification happens only once per connection so we need to close
        # all the opened adapters once we're done. Otherwise, the effects of
        # verify=False persist beyond the end of this context manager.
        opened_adapters.add(self.get_adapter(url))

        settings = old_merge_environment_settings(self, url, proxies, stream, verify, cert)
        settings['verify'] = False

        return settings

    requests.Session.merge_environment_settings = merge_environment_settings

    try:
        with warnings.catch_warnings():
            warnings.simplefilter('ignore', InsecureRequestWarning)
            yield
    finally:
        requests.Session.merge_environment_settings = old_merge_environment_settings

        for adapter in opened_adapters:
            try:
                adapter.close()
            except:
                pass
            
class Utils():
    
    @staticmethod
    def get_dict_val(data:dict, key:str=None, key_path:str=None, default=None):
        """
        Params:
            - data: is dict object
            - key (optional): get dict value by key
            - key_path (optional): get value of nested dict object. e.g.: key1.key2.key3
        Returns:
            - Value if found, None othewise
        """
        if data is not None and key is not None:
            try:
                return data.get(key, default)
            except:
                pass

        if data is not None and key_path is not None:
            try:
                keys = key_path.split(".")
                value = default
                obj_value = data
                for key in keys:
                    if isinstance(obj_value, dict):
                        value = obj_value.get(key)
                        obj_value = value
                    else:
                        return default
                return value
            except Exception as ex:
                pass

        return default
    
    @staticmethod
    def to_datetime(dtime:Text) -> datetime:
        """
        Params:
            - dtime: string date time
        Return:
            - datetime object. It will convert to UTC if there is no timezone in dtime text
        """
        if dtime is None or len(dtime) == 0:
            return None

        try:           
            if isinstance(dtime, datetime):
                obj_dtime = dtime
            else:
                obj_dtime = parser.parse(dtime)

            if obj_dtime.tzinfo is None:
                utc = pytz.UTC
                obj_dtime = utc.localize(obj_dtime)

            return obj_dtime
        except:
            pass

        return None

    @staticmethod
    def to_timestamp(dtime:datetime):
        """
        Inputs:
            - dtime: datetime object
        Return:
            - unix timestamp in millis seconds
        """
        try:
            if dtime is not None:
                unix_timestamp = datetime.timestamp(dtime)*1000
                return unix_timestamp

        except Exception as ex:
            pass
        return None