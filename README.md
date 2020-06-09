# python-blockchain

Development of a blockchain and cryptocurrency using Python, JavaScript and React

**Activate the virtual environment (Windows 10)**
```
blockchain-env/Scripts/Activate.ps1
```

**Install all packages**
```
pip install -r requirements.txt
```

**Run the tests**
Make sure to activate the virtual environment.
```
python -m pytest backend/tests
```

**Run the application and API**
Make sure to activate the virtual environment.
```
python -m backend.app
```

**Run a peer instance**
Make sure to activate the virtual environment.
```
$env:PEER='True'; python -m backend.app
```
