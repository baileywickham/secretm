# secrets
A tiny secret manager in python. Adds the secrets file to the `.gitignore`, uploads a copy encrypted
with your ssh key.

## Install
`pip install --user secretm`


## Use
Instantiate the module:
```python
s = secretm.Secrets()
```

## TODO
- [x] Add encryption with public RSA key
- [x] Store key in header of encrypted file
- [ ] Add async mode

## Example
```python
import secretm

# The class takes an optional path for the secrets file
s = secretm.Secrets()

# Write the api key to the secrets file
# This will normally be done by editing the yaml file directly, as
# coping a key to a file is easier than putting it in code.
s['api_key'] = 'abc'

# Print the secret
print(s['api_key'])
```
