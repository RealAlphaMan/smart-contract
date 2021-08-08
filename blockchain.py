from time import time
import json
import hashlib

class Blockchain(object):
    def _init_(self):
        self.chain = []
        self.current_transactions = []

        #Create first new block
        self.new_block(previous_hash=1, proof=100)

    def new_block(self, proof, previous_hash = None):
        #Create new block and add to chain
        block = {
            'index': len(self.chain)+1,
            'timestamp': time(),
            'transactions': self.current_transactions,
            'proof': proof,
            'previous_hash': previous_hash or self.hash(self.chain[-1])
        }
        #Reset the current list of transaction
        self.current_transactions = []
        self.chain.append(block)

        return block

    def new_transaction(self, sender, receiver, amount):
        #Create new transaction to go into the next mined block
        self.current_transactions.append({'sender': sender, "receiver": receiver, "amount": amount})
        return self.last_block['index'] + 1

    @staticmethod
    def hash(block):
        #Hash a block
        block_string = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()

    @property
    def last_block(self):
        #Return the last block
        pass