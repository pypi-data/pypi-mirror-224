

import threading
import asyncio
import websockets
from time import sleep

# create handler for each connection

class twebsocket(threading.Thread):

    def __init__(self):
        threading.Thread.__init__(self)

        self.start_server = websockets.serve(self.handler, "localhost", 8000)
        self.loop = asyncio.get_event_loop()

        self.count_msg = 0

        self.start()


    async def handler(self, websocket, path):
        data = await websocket.recv()

        reply = f"Data recieved as:  {data}!"
        print(reply)

        self.count_msg += 1

        await websocket.send(reply)

    def run(self):
        self.loop.run_until_complete(self.start_server)
        self.loop.run_forever()

    def stop(self):

        self.loop.stop()


if __name__ == '__main__':
    tws = twebsocket()

    while True:
        sleep(1)
        print(f'count msg: {tws.count_msg}')
        if tws.count_msg == 5:
            tws.





