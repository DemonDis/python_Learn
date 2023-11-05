import websockets
from websockets.sync.client import connect
import _thread

def receive_messages(websocket):
    while True:        
        try:
            message = websocket.recv()
            print(">", message)
        except websockets.exceptions.ConnectionClosed:
            break

with connect("ws://localhost:8001") as ws:
    _thread.start_new_thread(receive_messages,(ws,))  # прослушивание с сервера
    while True:
        toSend = input() 
        ws.send(toSend)