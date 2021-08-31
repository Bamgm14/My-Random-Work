import asyncio
import json 
import base64

class ServerProtocol(asyncio.Protocol):
    def connection_made(self, transport):
        peername = transport.get_extra_info('peername')
        print('[#]Connection from {}'.format(peername))
        self.transport = transport
        self.transport.write(b"Welcome to the game!\n")
        self.transport.write(b"Same as before but with a twist....\nI am based.\n")
    def data_received(self, data):
        try:
            message = data.decode()
            #print(message,type(message))
            try:
                message = base64.b64decode(message)
            except:
                self.transport.write(b"Hmm, seems like I have made it harder? 64 times harder maybe XD")
                self.transport.close()
                return None
            message = json.loads(message)
            if list(message.keys()) == ['name','phone_number','random']:
                with open("Winnerisme.txt",'a') as f:
                    f.write(str(message) + '\n')
                self.transport.write(b"You are in!")
            else:
                self.transport.write(b"Are you sure you did it right?\n")
            self.transport.close()
            return None
        except Exception as e:
            self.transport.write(b"Some error in formatting happened, please try again\n")
            self.transport.write(bytes(str(e),'utf-8') + b'\n')
            self.transport.close()
            return None



async def main():
    # Get a reference to the event loop as we plan to use
    # low-level APIs.
    loop = asyncio.get_running_loop()
    print('[#]Server Started!')
    server = await loop.create_server(
        lambda: ServerProtocol(),
        '127.0.0.1', 30000)

    async with server:
        await server.serve_forever()


asyncio.run(main())