import json
import time
from typing import Optional

from mlopscfg import struct_log
from mlopscfg.backend import (
    Backend,
    SSMParameterStore,
)
from mlopscfg.parameters import (
    InvalidParametersError,
    Parameters,
)


class ParameterCacheSingleton(type):
    """Class used as metaclass to enforce the ceration of a Singleton."""

    _instances = {}

    def __call__(cls, *args, **kwargs):
        cls_id = f"{cls.__class__.__name__}-{str(args)}"
        if cls_id not in cls._instances:
            cls._instances[cls_id] = super(ParameterCacheSingleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls_id]


class ParameterCache(metaclass=ParameterCacheSingleton):
    """Configuration is a singleton class that can be used to retrieve
    parameters by using a local state and persisting them via a Backend. It can
    be used to share state between two different services while they are
    running by using the name 'Namespace' The cache helps to make sure that the
    Backend is not queried over and over again. The client must call clear()
    after the cache is no longer needed.

    It automatically stores state on 2 separate tiers:

    * Tier 1 = local memory: values stored here live as long as the
      execution environment exists. Fast retrieval, short lifespan and
      only accessible by a single instance.
    * Tier 2 = Backend: values stored here live outside of the
      execution environment in persistent storage. Slow(er) retrieval,
      longer lifespan and shared between all services.

    Cached objects always have a TTL with a default of 1 hour.
    Expired objects are either overwritten automatically with a fresh object
    or by the client calling clear.
    """

    def __init__(self, namespace: str, backend: Optional[Backend] = None):
        self.namespace = namespace
        self._state = {}
        self.backend = Parameters(backend=backend) if backend else Parameters(backend=SSMParameterStore())
        self.logger = struct_log.get_logger(name=self.__class__.__name__, level=struct_log.DEBUG, verbose=True)

    def name(self, key: str) -> str:
        return f"{self.namespace}/state/{key}"

    def put(self, key: str, value: any, ttl: int = 600) -> any:
        co = {"ttl": int(time.time()) + ttl, "value": value}
        self.backend.put_parameter(path=self.name(key), value=json.dumps(co), overwrite=True)
        self._state[self.name(key)] = co
        return co

    def get(self, key: str) -> any:
        if self.name(key) in self._state:
            co = self._state[self.name(key)]
            # Parameter found in local cache and has not expired
            if co["ttl"] >= int(time.time()):
                return co["value"]

        # Parameter needs to be retrieved from the Backend
        output = self.backend.get_parameters(keys=[self.name(key)])

        # If the parameter was not found raise InvalidParameters
        if output.get("InvalidParameters"):
            raise InvalidParametersError(output["InvalidParameters"])

        # Convert the value to dict
        co = json.loads(output.get(self.name(key)))

        # If the Parameter is not expired return the value
        if co["ttl"] >= int(time.time()):
            # Parameter was not in cache, save it
            self._state[self.name(key)] = output
            return co["value"]

        # If the parameter expired raise an exception
        raise InvalidParametersError(self.name(key))

    def clear(self) -> None:
        self._state = {}
        self.backend.backend.delete_parameters_by_path(path=f"{self.namespace}/state")
