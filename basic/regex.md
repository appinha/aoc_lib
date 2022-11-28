# regex

## findall

2015/day/5:
```python
has_repeated = re.findall(r'((\w)\2{1,})', string) != []
has_pairs = re.findall(r'(\w{2}).*?(\1)', string) != []
```

2015/day/12:
```python
def _find_all_numbers(self, string):
    return list(map(int, re.findall(r'[0-9\-]+', string)))
```

## search

2015/day/6:
```python
split = re.search(r'([a-z ]+)([0-9,]+)([a-z ]+)([0-9,]+)', instruction)
```

2015/day/14:
```python
result = re.search(r'(\w+).+(\b\d+).+(\b\d+).+(\b\d+)', line)
```

## split

2015/day/9:
```python
location_1, location_2, distance = re.split(' to | = ', line)
```

## sub

2015/day/8:
```python
string = re.sub(r'\\x([0-9a-f][0-9a-f])', 'H', string)
```
