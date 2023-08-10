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

## The examples using the find_keys().


```python
data = [
    {"key": 1},
    {"key": 2},
    {"my": 
        {"key": 
            {
                "chain": "A",
                "rope": 5,
                "string": 1.2,
                "cable": False
            }
        }
    },
    {"your":
    	{"key":
            {
                "chain": "B",
                "rope": 7,
                "string": 0.7,
                "cable": True
            }
    	}
    }
]
```

```python
p.find_keys(data, ['rope', 'cable'])
[[5, False], [7, True]]

p.find_keys(data, ['rope', 'cable'], group=False)
[5, False, 7, True]
```