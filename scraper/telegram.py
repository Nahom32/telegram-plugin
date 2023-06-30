import configparser
import json
import asyncio
import pandas as pd

from telethon import TelegramClient
from telethon.errors import SessionPasswordNeededError
from telethon.tl.functions.channels import GetParticipantsRequest
from telethon.tl.types import ChannelParticipantsSearch
from telethon.tl.types import (
    PeerChannel
)

def get_client(username: str, api_id, api_hash:str):
    try:
        return TelegramClient(username,api_id,api_hash)
    except:
        raise Exception("The client doesn't exist")

    
    