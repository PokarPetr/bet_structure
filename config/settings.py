PREMATCH_UPDATE_INTERVAL = 3600  # Интервал для обновления предматчевых данных
LIVE_UPDATE_INTERVAL = 60       # Интервал для обновления live данных
MAX_CONCURRENT_REQUESTS = 10    # Максимальное количество одновременных запросов
HEADERS = {
    "User-Agent": "Mozilla/5.0"
}

# Constants for retries
MAX_RETRIES = 3
RETRY_DELAY = 2  # Delay between retries in seconds

MAX_CONCURRENT_REQUESTS = 300