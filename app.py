import asyncio
from parsers.main_parser import get_events
from parsers.pre_match_parser import parse_pre_match
from parsers.live_match_parser import parse_live_match
from utils.logging_config import log_message
from config.settings import MAX_CONCURRENT_REQUESTS, HEADERS
from utils.sender import send_data
from utils.imports import ClientSession

parsed_matches = {
    "PreMatch": {},
    "Live": {}
}
previous_state = {
    "PreMatch": {},
    "Live": {}
}

async def parse_data(mode):
    global parsed_matches
    semaphore = asyncio.Semaphore(MAX_CONCURRENT_REQUESTS)
    async with ClientSession(headers=HEADERS) as session:
        events = await get_events(session, mode)
        tasks = [get_event_details(event, session, mode, semaphore) for event in events]
        results = await asyncio.gather(*tasks)
        results = [result for result in results if result is not None]


async def get_event_details(matches, session, mode, semaphore):

    semaphore = asyncio.Semaphore(MAX_CONCURRENT_REQUESTS)
    async with ClientSession(headers=HEADERS) as session:
        tasks = []
        for match in matches:
            url = match.get('url')  # Assuming each match has its own URL to fetch odds
            payload = {
                "match_id": match['match_id'],
                # Any other payload fields required for the request
            }
            tasks.append(parse_data(url, payload, semaphore, session))
        results = await asyncio.gather(*tasks)
        return results