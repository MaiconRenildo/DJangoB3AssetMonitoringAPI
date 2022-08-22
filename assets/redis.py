def Redis():
    import redis

    return redis.Redis(
       host = "localhost",
       port = 6379
    )


def Queue(name:str):
    from rq import Queue
    return Queue(connection=Redis(),name=name)


def monitoring_queue():
    return Queue("monitoring")


def email_queue():
    return Queue("email")