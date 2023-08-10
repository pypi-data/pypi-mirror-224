## `mockfly-python-sdk` SDK Documentation

### General Overview:

The `mockfly-python-sdk` SDK provides a simple interface to interact with the Mockfly service. The SDK allows you to identify users and retrieve flags based on a user's evaluation key.

### Getting Started:

To begin using `mockfly-python-sdk`, you need to install it. (Note: I'm assuming that the package is available on PyPI).

```bash
pip install mockfly-python-sdk
```

Then, you can import it into your project:

```python
from mockfly import Mockfly
```

### Constructor:

The SDK is initialized using the constructor. The constructor accepts the following parameters:

- `environment`: The environment for which you are obtaining the flags: "production" or "test".
- `auth_header`: A string representing the authorization header required to make calls to the Mockfly API. This should be derived from your project's private API key.

Example:

```python
mockfly = Mockfly(
  environment='production',
  auth_header='YOUR_PRIVATE_API_KEY',
)
```

### Methods:

#### `identify(value)`

This method is used to identify a user within the system.

- `value`: The user's evaluation key. It is essential to call this method before `get_flag()`.

Example:

```python
mockfly.identify('user@gmail.com')
```

#### `get_flag(key)`

This method is used to get a flag based on the provided key.

- `key`: The key of the flag you wish to get.

Returns a dictionary that represents the flag value for the given key and the identified user.

Example:

```python
try:
  data = mockfly.get_flag('feature_toggle')
  print(data)
except Exception as error:
  print(error)
```

### Error Handling:

The SDK has built-in validations and will raise errors in the following cases:

- If the `auth_header` is not provided when creating a `Mockfly` instance.
- If attempting to get a flag without providing a key.
- If attempting to get a flag without previously identifying the user.

### Conclusion:

The `mockfly-python-sdk` SDK simplifies interaction with the Mockfly service from Python applications. Ensure to handle potential errors and use the `identify` method before making calls to `get_flag`. Always remember that the `auth_header` value should be derived from the private API key of your project.