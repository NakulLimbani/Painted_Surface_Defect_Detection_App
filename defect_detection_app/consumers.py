import json
from channels.generic.websocket import AsyncWebsocketConsumer
from .utils import get_results

class LiveDetectionConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        print("WebSocket connected")
        await self.accept()

    async def disconnect(self, close_code):
        print("WebSocket disconnected")
        pass

    async def receive(self, text_data):
        pass

    async def send_results(self, event):
        try:
            print("Sending results...")
            results = get_results()  # Assuming get_results() returns the latest results as a dictionary
            await self.send(text_data=json.dumps(results))
            print("Results sent successfully.")
        except Exception as e:
            # Handle any exceptions or errors that may occur
            print(f"Error sending results: {e}")
