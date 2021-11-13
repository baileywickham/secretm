import secretm


s = secretm.Secrets()
s['api_key'] = 'abc'

print(s['api_key'])

