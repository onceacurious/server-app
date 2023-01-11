from channels.consumer import SyncConsumer


class EchoConsumer(SyncConsumer):

    def connect(self, event):
        self.send({
            "type": "websocket.accept",
            "message": "WS connected"
        })

    def receive(self, event):
        self.send({
            "type": "websocket.send",
            "text": event["text"],
        })
