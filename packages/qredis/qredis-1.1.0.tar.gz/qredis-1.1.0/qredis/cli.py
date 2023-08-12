from redis import Redis

from .util import setup

redis_opts, extra_opts = setup()
redis = Redis(**redis_opts)

STR = {
    "str:hello": "world",
    "str:big": 1000 * ("".join(map(chr, range(ord('1'), ord('Z')))) + "\n"),
    "str:number": 567,
}

HASH = {
    "hash:simple": {"hello": "world", "foo": "bar"},
    "hash:many": {f"key_{i:04d}": f"value for {i:04d}" for i in range(1000)},
}

SET = {
    "set:simple": ("hello", "world", "foo", "bar"),
    "set:many": tuple(f"item {i:04d}" for i in range(1000)),
}

ZSET = {
    "zset:simple": {"hello": 100, "foo": 200},
    "zset:many": {f"item {i:04d}": i for i in range(100, 10_000, 10)},
}

LIST = {
    "list:simple": ("hello", "world", "foo", "bar"),
    "list:many": tuple(f"item {i:04d}" for i in range(1000)),
}

def fill(redis: Redis, prefix="demo:"):
    redis.mset({f"{prefix}{key}": value for key, value in STR.items()})
    for key, value in HASH.items():
        redis.hset(f"{prefix}{key}", mapping=value)
    for key, value in SET.items():
        redis.sadd(f"{prefix}{key}", *value)
    for key, value in ZSET.items():
        redis.zadd(f"{prefix}{key}", mapping=value)
    for key, value in LIST.items():
        redis.delete(f"{prefix}{key}")
        redis.rpush(f"{prefix}{key}", *value)

fill(redis)