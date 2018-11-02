import hashlib
import xmltodict
import ast
import inspect
import logging
import pickle

from anytree import NodeMixin


# The class for Block
class BaseBlock(object):

    def __init__(self, index=-1, time=-1, proof_of_work_input=-1, effort=-1, transactions=-1, previous_hash=-1):
        logging.info("Created a block:{}".format(str(self)))

    def hash_block(self):
        """Creates the unique hash for the block. It uses sha256."""
        m = hashlib.sha256()
        m.update((str(self.index) + str(self.timemade) + str(self.proof_of_work) + str(self.effort) + str(
            self.transactions) + str(self.previous_hash)).encode('utf-8'))
        # logging.debug("Block's hash: {}".format(m.hexdigest()))
        return m.hexdigest()

    def importXml(self, block_xml):
        for field in block_xml:
            if field != "transactions":
                self.setField(field, block_xml[field])
            else:
                for transaction in block_xml[field]['trans']:
                    transaction_to_add = {}
                    for k in transaction:
                        transaction_to_add[k] = transaction[k]
                    self.setField("transaction", transaction_to_add)

    def setField(self,field,value):
        #index=-1, time=-1, proof_of_work_input=-1, effort=-1, data=-1, previous_hash=-1
        if field == 'index':
            try:
                self.index = int(value)
            except:
                pass
        elif field == 'time':
            try:
                self.time = float(value)
            except:
                pass
        elif field == 'proof_of_work':
            try:
                self.proof_of_work = str(value)
            except:
                pass
        elif field == 'effort':
            try:
                self.effort = str(value)
            except:
                pass
        elif field == 'previous_hash':
            try:
                self.previous_hash = str(value)
            except:
                pass
        elif field == 'transaction':
            try:
                if type(value) is type({}):

                    self.transactions.append(value)
            except:
                pass

    def exportXml(self):
        # index=-1, time=-1, proof_of_work_input=-1, effort=-1, transactions=-1, previous_hash=-1
        block = {'block':{'index':self.index,'time':self.time,'proof_of_work':self.proof_of_work,'effort':self.effort,'transactions':{'trans':self.transactions}},'previous_hash':self.previous_hash}
        return xmltodict.unparse(block)

    def getdict(self):
        gen_dict = {'index': self.index, 'timemade': self.timemade, 'proof_of_work': self.proof_of_work,
                    'effort': self.effort, 'transactions': pickle.dumps(self.transactions),
                    'previous_hash': self.previous_hash, 'hash': self.hash}
        return gen_dict


    def __repr__(self):
        # def __init__(self, index, timestamp, pow, effort,data, previous_hash):
        return "Block({},{},'{}','{}',{},'{}')".format(self.index, self.timemade, self.proof_of_work, self.effort,
                                                       self.transactions, self.previous_hash)



    def __str__(self):
        return "hash: {} previous: {}".format(self.hash, self.previous_hash)

    '''
    def __str__(self):
        return "i: {} time: {} \tpow: {} effort: {} data: {} \tprevious: {} hash: {}".format(self.index, self.timestamp,
                                                                                             self.proof_of_work,
                                                                                             self.effort, self.data,
                                                                                             self.previous_hash,
                                                                                             self.hash)
    '''

class Block(BaseBlock, NodeMixin):
    def __init__(self, index=-1, timestamp=-1, proof_of_work_input=-1, effort=-1, transactions=-1, previous_hash=-1,
                 parent=None):
        __tablename__ = "blocks"
        super(BaseBlock, self).__init__()
        self.parent = parent
        self.index = index
        self.timemade = timestamp


        self.proof_of_work = proof_of_work_input
        self.effort = effort
        self.transactions = transactions

        '''
        data contains:
         transactions: list
        '''
        self.previous_hash = previous_hash
        self.hash = self.hash_block()
        # NodeMixin.__init__(self)
        #
        # BaseBlock.__init__(self, index, timestamp, proof_of_work_input, effort, data, previous_hash)
        # self.name = self.hash
        # if parent != None:
        #     self.parent(parent)

    def getBlock(self):
        return super
