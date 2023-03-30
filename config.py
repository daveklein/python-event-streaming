kafka_config = { 
    "bootstrap.servers": "localhost:29092",
}

credentials = {
    "consumer.key": "{your_consumer_key}",
    "consumer.secret": "{your_consumer_secret}",
    "access.token": "{your_access_token}",
    "access.token_secret": "{your_access_token_secret}"
}

tp_config = {
    "bootstrap.servers": "localhost:29092",
    "auto.offset.reset": "earliest",
    "group.id": "conf-tweets"
}

td_config = {
    "bootstrap.servers": "localhost:29092",
    "auto.offset.reset": "earliest",
    "group.id": "top-tweeters"
}

topics = {
    "input": "conf-tweets",
    "output": "top-tweeters"
}
