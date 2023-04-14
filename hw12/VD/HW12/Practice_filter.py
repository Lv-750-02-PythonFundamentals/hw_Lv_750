"""Display a list of list items that have the values "red", ["red",
"green", "black", "red", "brown", "red", "blue", "red", "red",
“yellow”] using the filter function.
"""

values = ["red", "green", "black", "red", "brown",
        "red", "blue", "red", "red", "yellow"
        ]

red = list(filter(lambda color: color == "red", values))
print(red)