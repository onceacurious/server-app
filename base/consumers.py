from channels.consumer import SyncConsumer
from asgiref.sync import async_to_sync
import json

class BaseConsumer(SyncConsumer):
    def connect(self):
        self.action_name = "base"

        async_to_sync(self.channel_layer.group_add)(
            self.action_name
        )

    def disconnect(self, close_code):
        async_to_sync(self.channel_layer.group_discard)(
            self.action_name
        )

    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        data = text_data_json["data"]
        async_to_sync(self.channel_layer.group_send)(
            self.action_name, {"type": "base", "data": data}
        )

    def base_data(self, event):
        data = event("data")
        self.send(text_data=json.dumps({"data": data}))