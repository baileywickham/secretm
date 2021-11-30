import secretm

def test_readFromSecrets():
    s = secretm.Secrets()
    #s['api_key'] = 'abc'
    assert s['api_key'] == 'abc'

def test_writeToSecrets():
    s = secretm.Secrets()
    s['new'] = 'new'
    del s
    new = secretm.Secrets()
    assert new['new'] == 'new'


