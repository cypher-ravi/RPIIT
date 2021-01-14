import uuid

def generate_txnid():
    return 'txn' + str(uuid.uuid4())

