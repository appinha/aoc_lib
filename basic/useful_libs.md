# useful libs

## collections

```python
from collections import defaultdict

qty_by_location = defaultdict(int)
instructions_by_wire = defaultdict(list)
location_by_location_by_distance = defaultdict(dict)
```

# hashlib

```python
import hashlib

md5_hexa_hash = hashlib.md5(test.encode()).hexdigest()
```

# string

```python
from string import ascii_lowercase

self.alphabet_trios = self._get_sequenced_trios(ascii_lowercase)
```
