import logging
logging.info("Loading Variables")
WORK = 5

PEER_NODES = ['192.168.1.222']
MINER_NODE_URL = "127.0.0.1"
PORT = 5000
PENDING_TRANSACTIONS = []
logging.debug("work: {} peers:{} node_url:{} port: {} pending: {}".format(WORK,PEER_NODES,MINER_NODE_URL,PORT,PENDING_TRANSACTIONS))
logging.info("Done loading Variables")