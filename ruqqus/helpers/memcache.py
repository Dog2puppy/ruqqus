from os import environ
import pylibmc
import flask_caching
import flask_caching.backends as backend


class Custom_Cache(pylibmc.Client, backend.base.BaseCache):
    pass

def custom_memcache(app, config, *args, **kwargs):
  return Custom_Cache(
                    [environ.get("MEMCACHIER_SERVERS")],
                    binary=True,
                    username=environ.get("MEMCACHIER_USERNAME"),
                    password=environ.get("MEMCACHIER_PASSWORD"),
                    behaviors={
                      # Faster IO
                      'tcp_nodelay': True,

                      # Keep connection alive
                      'tcp_keepalive': True,

                      # Timeout for set/get requests
                      'connect_timeout': 30000, # ms
                      'send_timeout': 750 * 1000, # us
                      'receive_timeout': 750 * 1000, # us
                      '_poll_timeout': 2000, # ms

                      # Better failover
                      'ketama': True,
                      'remove_failed': 1,
                      'retry_timeout': 2,
                      'dead_timeout': 30,
                    })


#import string
CACHE_TYPE = 'ruqqus.helpers.get.memcache.custom_memcache'