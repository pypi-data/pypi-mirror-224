# jsonmgnt

A simple JSON parsing tool.

## Installation

Install it via pip:

```bash
pip install jsonmgnt
```

## Usage

```python
import jsonmgnt

dat2 = jsonmgnt.parse('{"Invoker": "SunStrike"}')
print(dat2['Invoker']) # SunStrike

dat1 = jsonmgnt.parse('{"Hammer Level": 25}')
print(dat1['Hammer Level']) # 25
```
