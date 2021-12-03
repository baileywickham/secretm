# secrets
A tiny secret manager in python. Adds the secrets file to the `.gitignore`, uploads a copy encrypted
with your ssh key.

## Install
`pip install --user secretm`


## Use
Write YAML file, usually named `secrets`:
```yaml
key: very_secret
```

Instantiate the module:
```python
import secretm
s = secretm.Secrets()
print(s['key']) # Prints "very_secret"
```

By default the package encrypts your `secrets` file with your public key found in `~/.ssh/id_rsa.pub`. This encrypted file is `secrets.enc` which can be safely uploaded to github. To decrypt, the package uses your private key found in `~/.ssh/id_rsa`. The secrets file is added to a `.gitignore` file.  


## TODO
- [x] Add encryption with public RSA key
- [x] Store key in header of encrypted file
- [ ] Add async mode

## Example
```python
import secretm

# Shown are the optional paramaters, where gh_user is your github user if you want your 
# public key fetched from there, and public_key and private_key are RSA.RsaKey objects.
s = secretm.Secrets(datafile='secrets', gh_user=None, public_key_file=`~/.ssh/id_rsa.pub`,
                    private_key_file=`~/.ssh/id_rsa`, public_key=None, private_key=None)

# Write the api key to the secrets file
# This will normally be done by editing the yaml file directly, as
# coping a key to a file is easier than putting it in code.
s['api_key'] = 'abc'

# Print the secret
print(s['api_key'])
```
