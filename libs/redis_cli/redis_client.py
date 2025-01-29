import redis

from database.core.settings import config


redis_client = redis.Redis().from_url(config.redis_url)  
