import requests

class Mockfly:
    def __init__(self, environment=None, auth_header=None):
        self.evaluation_key = ''
        self.environment = environment
        self.auth_header = auth_header

    def identify(self, value):
        self.evaluation_key = value

    def get_flag(self, key):
        if not self.auth_header:
            raise ValueError('You must add the authHeader in constructor when create the Mockfly object.')
        
        if not key:
            raise ValueError('Key cannot be null. Please, set a key when call to Mockfly.get_flag(key).')
        
        if not self.evaluation_key:
            raise ValueError('You must identify a user before get a flag. You can use Mockfly.identify(value) function.')
        
        response = requests.post(
            'https://api.mockfly.dev/flags/evaluate',
            json={
                'keyFlag': key,
                'environment': self.environment,
                'evaluationKey': self.evaluation_key,
            },
            headers={'Authorization': self.auth_header}
        )

        response.raise_for_status() 
        return response.json()
