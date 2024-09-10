from utils.networks import fetch_with_retry
from .pre_match_parser import parse_pre_match
from .live_match_parser import parse_live_match


async def get_pre_matches(session):
    url = ''
    payload = {}
    return await fetch_with_retry(session, url, payload)

async def get_live_matches(session):
    url = ''
    payload = {}
    return await fetch_with_retry(session, url, payload)


async def get_events(mode, session):
    if mode == "PreMatch":
        return await get_pre_matches(session)
    elif mode == "Live":
        return await get_live_matches(session)
    return []

async def parse_one_match(event, session, mode, semaphore):
    async with semaphore:
        urls = {}
        if mode == "Live":
            event = await parse_live_match(session, event, urls)
            return event
        url = urls['parse_one_match']
        event = await parse_pre_match(session, event, url)
        return event