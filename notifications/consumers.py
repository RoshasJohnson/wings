from channels.generic.websocket import WebsocketConsumer,AsyncWebsocketConsumer # AsyncWebsocketConsumer
from channels.db import database_sync_to_async  # database_sync_to_async
from asgiref.sync import async_to_sync,sync_to_async    
from channels.layers import get_channel_layer  # for getting the channel layer
