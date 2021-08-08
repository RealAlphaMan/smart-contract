class BlockChain(object):
    def _init_(self):
        self.chain = []
        self.current_transaction = []

    def new_block(self):
        #Create new block and add to chain
        pass

    def new_transaction(self, sender, receiver, amount):
        #Create new transaction to go into the next mined block
        self.current_transaction.append({'sender': sender, "receiver": receiver})

    @staticmethod
    def hash(block):
        #Hash a block
        pass

    @property
    def last_block(self):
        #Return the last block
        pass