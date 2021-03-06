import os
import time
import pandas as pd

from pathlib import Path

from web3 import Web3, IPCProvider
from pathlib import Path

ipc_file = os.path.join(Path.home(), '.ethereum/social/geth.ipc')

web3 = Web3(IPCProvider(ipc_file))

addresses_df = pd.read_csv(
    'snapshot/snapshot_0001.txt',
    header=None, names=['id', 'address', 'balance']
)

total_balance = 0
transactions_count = 0


with open('geth_genesis.json', 'a') as genesis_file:
    for row in addresses_df.itertuples():
        transactions_count += 1
        web3.eth.sendTransaction({
            'from': '0xc572dc5a3aa8ce2970259f3ae3b5e985b3bbe588',
            'to': row.address,
            'value': row.balance,
            'gas': 21000,
            'gasPrice': 1800000000000,
        })
        total_balance += int(row.balance)

        if transactions_count == 10000:
            print('Last Transaction Address: {}'.format(row.address))
            time.sleep(50)
            transaction_count = 0

print(total_balance)
