import hashlib
# import json
from time import time
from uuid import uuid4

class Blockchain(object):
    def __init__(self):
        self.current_transactions = []
        self.chain = []

        # 초기 블록 생성
        self.new_block(previous_hash=1, proof=100)

    def new_block(self, proof, previous_hash=None):
        block = {
            'index': len(self.chain) + 1, # 순번
            'timestamp': time(), # 시간
            'transactions': self.current_transactions, # 무슨 작업인지
            'proof': proof,  # 암호화를 위한 값
            'previous_hash': previous_hash or self.hash(self.chain[-1]), # 이전 암호화된 데이터
        }

        # 트렌젝션 초기화
        self.current_transactions = [] 

        # 체인에 블록을 추가
        self.chain.append(block) 
        return block

    def new_transaction(self, sender, recipient, amount):
        """
        Creates a new transaction to go into the next mined Block
        :param sender: <str> Address of the Sender
        :param recipient: <str> Address of the Recipient
        :param amount: <int> Amount
        :return: <int> The index of the Block that will hold this transaction
        """
        self.current_transactions.append({
            'sender': sender,
            'recipient': recipient,
            'amount': amount,
        })

        return self.last_block['index'] + 1

    @staticmethod
    def hash(block):
        # block_string = json.dumps(block, sort_keys=True).encode()
        # return hashlib.sha256(block_string).hexdigest()
        return hashlib.sha256(block).hexdigest()

    @property
    def last_block(self):
        return self.chain[-1] # 인덱싱 ==> -1 = 마지막
    # 작업증명 == 이 작업이 맞는지 증명하는 과정
    def proof_of_work(self, last_proof):
        """
        A와 B사이의 C라는 작업이 있는데
        A가 B에게 전송한 암호화된 C를 C가 맞는지 확인하는 작업
        """

        proof = 0
        while self.valid_proof(last_proof, proof) is False:
            proof += 1

        return proof

    @staticmethod
    def valid_proof(last_proof, proof):
        # 앞에 숫자를 붙여서 인코딩
        guess = f'{last_proof}{proof}'.encode()
        # 그 데이터를 해싱을 하면
        guess_hash = hashlib.sha256(guess).hexdigest()
        # 앞에 0이 몇개있는지 확인할 수 있음
        # 지금은 난스가 58인지 확인
        return guess_hash[:4] == "0000"
        
