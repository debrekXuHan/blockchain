#!/usr/bin/python
# -*- coding: utf-8 -*-
import datetime  # generate timestamp for each block
import hashlib  # hashing algorithm

# define the 'block' data structure
class Block:
    # each block has 7 attribute
    blockNo = 0
    data = None  # data stored in this block
    next = None  # pointer to the next block
    hash = None  # unique id for this block and converting block info into a number in a certain range
    nonce = 0  # a number only used once (use it to compute a unique hash)
    previousHash = 0x0  # hash of the previous block (previousHash for the first block is 0x0)
    timestamp = datetime.datetime.now()

    # initialize a block by storing some data in it
    def __init__(self, data):
        self.data = data

    # function of computing the hash of this block
    def hash(self):
        # using SHA-256 algorithm
        h = hashlib.sha256()
        h.update(
            str(self.nonce).encode('utf-8') +
            str(self.data).encode('utf-8') +
            str(self.previousHash).encode('utf-8') +
            str(self.timestamp).encode('utf-8') +
            str(self.blockNo).encode('utf-8')
        )
        # return a hexademical string
        return h.hexdigest()

    def __str__(self):
        # print out the value of a block
        return "Block Hash: " + str(self.hash()) + \
               "\nBlock No: " + str(self.blockNo) + \
               "\nBlock Data: " + str(self.data) + \
               "\nHashes: " + str(self.nonce) + \
               "\n-------------------"

# define the blockchain datastructure
class Blockchain:
    maxNonce = 2 ** 32
    diff = 20  # mining difficulty
    target = 2 ** (256 - diff)  # target hash for mining

    # generate the first block in a blockchain, called 'genesis' block
    block = Block('Genesis')
    head = block

    # add a given block to this blockchain
    def add(self, block):
        block.previousHash = self.block.hash()
        block.blockNo = self.block.blockNo + 1
        # the next block equals to the input block
        self.block.next = block
        # the current block move to the input block
        self.block = self.block.next

    # determine whether or not we can add a given block to the blockchain
    def mine(self, block):
        for n in range(self.maxNonce):
            if int(block.hash(), 16) <= self.target:  # solve this function to determine whether or not to add
                self.add(block)
                # print(block)
                break
            else:
                block.nonce += 1

if __name__ == "__main__":
    blockchain = Blockchain()

    for n in range(10):
        blockchain.mine(Block("Block " + str(n+1)))

    while blockchain.head != None:
        print(blockchain.head)
        blockchain.head = blockchain.head.next
