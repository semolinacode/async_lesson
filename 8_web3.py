import asyncio
import random

from web3 import Web3
from web3.eth import AsyncEth


class Client:
    def __init__(self, rpc: str, private_key: str | None = None):
        self.rpc = rpc

        self.w3 = Web3(
            provider=Web3.AsyncHTTPProvider(
                endpoint_uri=self.rpc,
            ),
            modules={'eth': (AsyncEth,)},
            middlewares=[]
        )

        if private_key:
            self.account = self.w3.eth.account.from_key(private_key=private_key)
        else:
            self.account = self.w3.eth.account.create(extra_entropy=str(random.randint(1, 999_999_999)))

    async def get_balance(self, address: str | None = None):
        if not address:
            address = self.account.address
        return await self.w3.eth.get_balance(account=address)


async def main():
    while True:
        client = Client(rpc='https://rpc.ankr.com/arbitrum')
        # client = Client(rpc='https://arbitrum.llamarpc.com')
        balance = await client.get_balance()
        print(client.account.key.hex(), client.account.address, balance, '\n')
        if balance:
            break


if __name__ == '__main__':
    asyncio.run(main())
