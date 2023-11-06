import asyncio
import websockets
from websocket import create_connection
import json
# сохраняет всех клиентов, подключенных к серверу
client_list = []   

async def handler(websocket):
    client_list.append(websocket)    
    while True:
        try:
            message = await websocket.recv()
            print('Message received from client: ', message)           
            # await broadcast(message)
            if message == 'd':
                print('!!!!!!', message)
                await websocket.send(json.dumps({"op":"addr_sub", "addr":"dogecoin_address"}))
                # websocket.send(json.dumps({"op":"addr_sub", "addr":"dogecoin_address"}))
                # result =  ws.recv()
                # print (result)
        except Exception as e:            
            print(e)
            client_list.remove(websocket)
            break

async def broadcast(message):
    for client in client_list:                
        # транслирует сообщение другому клиенту
        await client.send(message)

async def main():
    async with websockets.serve(handler, "", 8001):
        await asyncio.Future()  # работает бесконечно

if __name__ == "__main__":
    asyncio.run(main())