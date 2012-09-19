# Funnel - SSH routing framework based on twisted


## How to use

```python
import funnel

class MyFunnel(Funnel):
    def auth_by_public_key():
        # ...

    def auth_by_password():
        # ...

    def getPty():
        # ...

    def execCommand():
        # ...

    def openShell():
        # ...


if __name__ == '__main__':
    MyFunnel.run()
```
