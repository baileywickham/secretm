# secrets
A tiny secret manager in python. Adds the secrets file to the `.gitignore`.

## TODO
- Add encryption with public RSA key
- Store key in header of encrypted file

## Example
```python
import secretm

# The class takes an optional path for the secrets file
s = secretm.Secrets()

# Write the api key to the secrets file
s['api_key'] = 'abc'

# Print the secret
print(s['api_key'])
```
