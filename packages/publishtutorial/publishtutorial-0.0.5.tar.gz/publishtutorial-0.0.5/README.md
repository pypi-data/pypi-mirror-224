# Publish package tutorial

## Installation
Create a virtualenv and then install the library
```bash
pip3 install publishtutorial
```

## Usage
```python
from src.myfunc import say_hello, average
from src.second_script import second_function

# Generate "Hello, World!"
say_hello()

# Generate "Hello, Everybody!"
say_hello("Everybody")

# Compute average between two numbers (default values are 1 and 2 -> 1.5)
average()

# Compute average between two numbers (2.5)
average(2,3)

# Sum to input value the average between the input and 2 (default value is 1 -> 1 + average(1,2) = 2.5)
second_function()

# Sum to input value the average between the input and 2 (5.5)
second_function(3)
```

## Developing
To install publishtutorial,
 along with the tools you need to develop and run tests,
 run the following in your virtualenv:
```bash
# Clone the repo
$ git clone git@github.com:matteobollettino/publish_tutorial.git

# Install package, along with the tools you need to develop and run tests
$ pip3 install -e .[dev]

# Run the tests already present
$ pytest
```


Credits to: [Coding Tech](https://www.youtube.com/watch?v=GIF3LaRqgXo&t=3s) and [NeuralNine](https://www.youtube.com/watch?v=tEFkHEKypLI&t=2s)