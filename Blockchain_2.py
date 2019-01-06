import datetime
import hashlib

class Block:
    block_no = 0
    data = None
    next = None  # Pointer to next block
    hash = None  #
    nonce = 0  # Number we increment every single time we make a guess, by changing the nonce we get a different hash
    previous_hash = 0x0  # Hash of previous block (this is what make a block chain immutable)
    timestamp = datetime.datetime.now()

    def __init__(self, data):
        self.data = data

    def hash(self):
        """Calculate the hash of the block"""
        h = hashlib.sha256()
        h.update(
        str(self.nonce).encode('utf-8') +
        str(self.data).encode('utf-8') +
        str(self.previous_hash).encode('utf-8') +
        str(self.timestamp).encode('utf-8') +
        str(self.block_no).encode('utf-8')
        )
        return h.hexdigest()

    def __str__(self):
        return "Block Hash: " + str(self.hash()) + "\nblock_no: " + str(self.block_no) + "\nBlock Data: " + str(self.data) + "\nHashes: " + str(self.nonce) + "\n--------------"


class Blockchain:
    diff = 5
    maxNonce = 2**32  # Value is adjusted so that the hash of the block will be less than or equal to the target
    target = 2 ** (256-diff)  # Lower target higher difficulty

    block = Block("Genesis")
    dummy = head = block

    def add(self, block):

        block.previous_hash = self.block.hash()  # Set the previous hash of the new block equal to that of the old block
        block.block_no = self.block.block_no + 1  # The block no of the new block is equal to the old block no + 1

        self.block.next = block  # Set the next pointer to the new block we want to add (like a linked list)
        self.block = self.block.next  # Moves the next pointer up, so we can keep adding new blocks to the chain

    def mine(self, block):
        for n in range(self.maxNonce):
            if int(block.hash(), 16) <= self.target:  # If hash is less than target, accept and add block to the chain
                self.add(block)
                print(block)
                break
            else:
                block.nonce += 1  # Else keep trying


blockchain = Blockchain()   # Instantiate the blockchain

for n in range(10):
    blockchain.mine(Block("Block " + str(n+1)))

while blockchain.head != None:
    print(blockchain.head)
    blockchain.head = blockchain.head.next