from channels.generic.websocket import AsyncWebsocketConsumer
import json


class BaseConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.action_name = "base"

        await self.channel_layer.group_add(
            self.action_name,
            self.channel_name
        )
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.action_name,
            self.channel_name
        )

    async def receive(self, text_data=None):
        text_data_json = json.loads(text_data)
        data = text_data_json["data"]
        await self.channel_layer.group_send(
            self.action_name, {"type": "base_data", "data": data}
        )

    async def base_data(self, event):
        data = event["data"]
        await self.send(text_data=json.dumps({"type": "base", "data": data}))
