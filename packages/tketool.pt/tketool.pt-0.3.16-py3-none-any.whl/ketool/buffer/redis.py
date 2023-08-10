import pickle, os
import redis, json
from ketool.JConfig import get_config_obj

import ketool.buffer.bufferbase as bb
from ketool.buffer.bufferbase import buffer

_redis_instance = None
_redis_buffer_key = "redis_buffer"


def _get_pool():
    global _redis_instance
    if _redis_instance is None:
        config_c = get_config_obj()
        _redis_instance = redis.ConnectionPool(host=config_c.get_config("redis_host"),
                                               port=int(config_c.get_config("redis_port")), decode_responses=True)
    return _redis_instance


def _load_buffer_file(key):
    pool = _get_pool()
    rrdis = redis.Redis(connection_pool=pool)

    if rrdis.hexists(_redis_buffer_key, key):
        return json.loads(rrdis.hget(_redis_buffer_key, key))

    raise Exception("没有此buffer item")


def _save_buffer_file(lists):
    pool = _get_pool()
    rrdis = redis.Redis(connection_pool=pool)
    for key, value in lists:
        # nkey = _get_hash_key_(key)
        rrdis.hset(_redis_buffer_key, key, json.dumps(value))


def _delete_buffer_file(key):
    if _has_buffer_file(key):
        pool = _get_pool()
        rrdis = redis.Redis(connection_pool=pool)

        rrdis.hdel(_redis_buffer_key, key)


def _has_buffer_file(key):
    pool = _get_pool()
    rrdis = redis.Redis(connection_pool=pool)

    if rrdis.hexists(_redis_buffer_key, key):
        return True

    return False


bb.has_buffer_file = _has_buffer_file
bb.load_buffer_file = _load_buffer_file
bb.delete_buffer_file = _delete_buffer_file
bb.save_buffer_file = _save_buffer_file
