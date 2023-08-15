# pilk-clicker
Library for working api pilk-clicker.ru

## Installation
```bash
pip install pilk-clicker
```

## Usage

### Get token (login)
```python
from pilk_clicker.api import Auth
from pilk_clicker.interfaces.auth import ILoginRequest

credentials = ILoginRequest(
    username="", password=""
)

response = Auth.login(credentials)

response.auth_token
```

### Logout
```python
from pilk_clicker.api import Auth
from pilk_clicker.interfaces.auth import ITokenRequest

credentials = ITokenRequest(authorization="token")

Auth.logout(credentials)
```

### Logup
```python
from pilk_clicker.api import Auth
from pilk_clicker.interfaces.auth import ILogupRequest

credentials = ILogupRequest(
    username="", password="", email=""
)

response = Auth.logup(credentials)
```

### clicker detail
```python
from pilk_clicker.api import Clicker
from pilk_clicker.interfaces.auth import ITokenRequest

credentials = ITokenRequest(authorization="token")

response = Clicker.clicker_detail(credentials)
```

### top list
```python
from pilk_clicker.api import Clicker
from pilk_clicker.interfaces.auth import ITokenRequest

credentials = ITokenRequest(authorization="token")

response = Clicker.top_list(credentials)
```

### save clicker
```python
from pilk_clicker.api import Clicker
from pilk_clicker.interfaces.auth import ITokenRequest
from pilk_clicker.interfaces.clicker import IClickerSaveRequest

credentials = ITokenRequest(authorization="token")

data = IClickerSaveRequest(
    arcoin_amount=1,
    arcoins_per_click=1,
    arcoins_per_seconds=1
)

response = Clicker.save_clicker(data, credentials)
```

### shop user
```python
from pilk_clicker.api import Shop
from pilk_clicker.interfaces.auth import ITokenRequest

credentials = ITokenRequest(authorization="token")

response = Shop.shop_user(credentials)
```

### save item
```python
from pilk_clicker.api import Shop
from pilk_clicker.interfaces.auth import ITokenRequest
from pilk_clicker.interfaces.shop import ISaveItemRequest

credentials = ITokenRequest(authorization="token")

items = Shop.shop_user(credentials)

for item in items:
    Shop.save_item(
        ISaveItemRequest(id=item.id, amount=item.amount + 1),
        credentials
    )
```
