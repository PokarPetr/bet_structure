import asyncio, time

from app import parse_data
from config.settings import *
from utils.logging_config import log_message

async def run_parsing_tasks(interval, mode):
    while True:
        start_time = time.time()
        try:
            await parse_data(mode)
        except Exception as e:
            log_message('error', f"Error by parsing: {e}")

        elapsed_time = time.time() - start_time
        await asyncio.sleep(max(0, interval - elapsed_time))

async def main():
    tasks = [
        run_parsing_tasks(PREMATCH_UPDATE_INTERVAL, "PreMatch"),
        run_parsing_tasks(LIVE_UPDATE_INTERVAL, "Live")
    ]
    await asyncio.gather(*tasks)

if __name__ == "__main__":
    asyncio.run(main())