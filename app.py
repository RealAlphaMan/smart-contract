from uuid import uuid4
from flask import Flask, jsonify
from blockchain import Blockchain

app = Flask(__name__)

# Generate a globally unique address for this node
node_identifier = str(uuid4()).replace('-', '')

blockchain = Blockchain()

@app.route('/mine', methods = ['GET'])
def mine():
    return "We will mine the block"

@app.route('/transaction/new', methods = ['GET'])
def new_transaction():
    return "We will add new transaction"

@app.route('/chain', methods = ['GET'])
def full_chain():
    reponse = {
        'chain': blockchain.chain,
        'length': len(blockchain.chain)
    }
    return jsonify(reponse), 200

if __name__ == '__main__':
    app.run(port=5000)