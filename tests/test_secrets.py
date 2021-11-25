import secretm


def test_default():
    s = secretm.Secrets()
    #s['api_key'] = 'abc'
    assert (s['api_key']) == 'abc'

