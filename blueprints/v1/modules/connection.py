import redis
import os

class Singleton(type):
    """
    An metaclass for singleton purpose. Every singleton class should inherit from this class by 'metaclass=Singleton'.
    """
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class RedisClient(object):

    def __init__(self):
        self.pool = redis.ConnectionPool(host=os.environ.get('redishost'), port=6379, db=1) #host = HOST, port = PORT, password = PASSWORD

    @property
    def conn(self):
        try:
            if not hasattr(self, '_conn'):
                self.getConnection()
            return self._conn
        except:
            return None


    def getConnection(self):
        self._conn = redis.Redis(connection_pool = self.pool)