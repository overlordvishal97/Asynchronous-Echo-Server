import asyncio
import websockets

async def connect_to_server():
    uri = "ws://localhost:8888"  # WebSocket server URI
    try:
        async with websockets.connect(uri) as websocket:
            while True:
                message = input("Enter message to send: ")
                await websocket.send(message)
                response = await websocket.recv()
                print("Received:", response)
    except ConnectionRefusedError:
        print("Unable to connect to the WebSocket server. Please ensure it is running and accepting connections.")

asyncio.run(connect_to_server())