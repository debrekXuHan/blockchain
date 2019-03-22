#!/usr/bin/python
# -*- coding: utf-8 -*-
import hashlib
import json
from time import time

# Define a blockchain class
class Blockchain(object):
    def __init__(self):
        self.chain = []
        self.current_transactions = []

    # Create a new block and add it to the chain
    def new_block(self, proof, previous_hash=None):
        """
        Create a new block into the chain.
        proof: <int> The proof generated by PoW Algorithm
        previous_hash: (optional) <str> Hash value of the previous block
        return: <dict> A new block
        """
        block = {
            'index': len(self.chain) + 1,
            'timestamp': time(),
            'transaction': self.current_transactions,
            'proof': proof,
            'previous_hash': previous_hash or self.hash(self.chain[-1])
        }

        # Initialize current transaction
        self.current_transactions = []

        self.chain.append(block)
        return block

    # Add a new transaction to the list of transactions
    def new_transaction(self, sender, recipient, amount):
        """
        Creates a new transaction to go into the next mined block.
        sender: <str> Address of the sender
        recipient: <str> Address of the recipient
        amount: <int> Transaction amount
        return: <int> The index of the block that will hold this transaction
        """
        self.current_transactions.append({
            'sender': sender,
            'recipient': recipient,
            'amount': amount
        })

        return self.last_block['index'] + 1

    # Return the last block in the chain
    @property
    def last_block(self):
        return self.chain[-1]

    # Hashes the block
    @staticmethod
    def hash(block):
        """
        Generate hexadecimal SHA-256 value for a block.
        block: <dict> Certain block as input
        return: <str> SHA-256 value
        """
        # Make sure this dict(block) is listed. Otherwise, we will get a scattered list
        block_string = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()