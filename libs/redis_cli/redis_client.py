import redis

from database.core.settings import config


<<<<<<< HEAD
redis_client = redis.Redis().from_url(config.redis_url)  # type: ignore
=======
redis_client = redis.Redis().from_url(config.redis_url)  
>>>>>>> 3f2822f (Complete servis with admin and company)
