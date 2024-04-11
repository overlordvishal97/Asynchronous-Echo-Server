import asyncio
import websockets

async def handle_client(websocket, path):
    try:
        while True:
            message = await websocket.recv()
            print(f"Received: {message}")
            await websocket.send(message)
    except websockets.ConnectionClosedError:
        print("WebSocket connection closed")

start_server = websockets.serve(handle_client, "localhost", 8888)

print("WebSocket server started on localhost:8888")
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()