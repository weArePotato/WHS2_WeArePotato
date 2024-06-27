# Color print

# Installation

Install using `pip`...

    pip install Discord-Embedds

# Usage

```python
from color_print import print
print("testerino", color='green')
```
![Alt text](/img/first.png?raw=true)
```python
print("testerino", color='blue', tag='success', tag_color='green')
```
![Alt text](/img/second.png?raw=true)
```python
print("testerino", color='blue', tag='success', tag_color='green', background='yellow')
```
![Alt text](/img/third.png?raw=true)
```python
print("testerino", color='blue', tag='success', tag_color='green', format='underline')
```
![Alt text](/img/four.png?raw=true)


* colors: [yellow, red, green, blue, cyan, magenta, purple]
* backgrounds: [yellow, red, green, blue, cyan, magenta, purple]
* formats: [bold, underline, blink]
