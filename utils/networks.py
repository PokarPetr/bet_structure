import aiohttp
import asyncio
import logging

from config.settings import MAX_RETRIES, RETRY_DELAY


async def fetch(session, url, payload):
    """
    Function to fetch data from a remote server.

    Args:
        session (aiohttp.ClientSession): The current session for making HTTP requests.
        url (str): The URL to fetch data from.
        payload (dict): The data to send in the request (POST body).

    Returns:
        Response data or None in case of failure.
    """
    try:
        async with session.post(url, json=payload) as response:
            response.raise_for_status()  # Raises an exception for 4xx/5xx errors
            return await response.json()
    except aiohttp.ClientError as e:
        logging.error(f"Error fetching data from {url}: {e}")
        return None


async def fetch_with_retry(session, url, payload, retries=MAX_RETRIES):
    """
    Function to fetch data from a remote server with retries.

    Args:
        session (aiohttp.ClientSession): The current session for making HTTP requests.
        url (str): The URL to fetch data from.
        payload (dict): The data to send in the request (POST body).
        retries (int): Number of retries allowed.

    Returns:
        Response data or None in case of repeated failure.
    """
    for attempt in range(retries):
        result = await fetch(session, url, payload)
        if result is not None:
            return result
        logging.warning(f"Retrying ({attempt + 1}/{retries}) in {RETRY_DELAY} seconds...")
        await asyncio.sleep(RETRY_DELAY)

    logging.error(f"Failed to fetch data from {url} after {retries} attempts.")
    return None