import marimo

__generated_with = "0.24.0"
app = marimo.App(width="medium", app_title="Python Fundamental")


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
        Excercise 01: Swap the values of a, b, and c.
    """)


@app.cell
def _():
    a, b, c = (5, 10, 15)
    a, b, c = (c, a, b)
    print(a, b, c)
    return


@app.cell
def _(mo):
    mo.md(r"""
        Excercise 02: Take the user input of age, height, and name and print it. Use the try-except block to handle invalid input.
    """)


@app.cell
def _():
    try:
        age = int(input("Enter your age: "))
        height = float(input("Enter your height: "))
        name = input("Enter your name: ")
        age = 10
        height = 5.8
        name = "abcd"

        print(f"Name: {name} | Age: {age} | Height: {height}")

    except ValueError:
        print("Invalid error!")
    return


@app.cell
def _(mo):
    mo.md(r"""
        Excercise 03: Calculate the total price of a product given its price and quantity. Use the formatting to properly display the outputs.
    """)


@app.cell
def _():
    price = 1234.5678
    product = "Laptop"
    quantity = 5

    print(f"Product: {product:<15} | Price: ${price:>8.2f} | Quantity: {quantity:>3}")
    print(
        "Product: {:<15} | Price: ${:>8.2f} | Quantity: {:>3}".format(
            product, price, quantity
        )
    )
    print("Total: ${:.2f}".format(price * quantity))
    return


@app.cell
def _(mo):
    mo.md(r"""
        Excercise 04: Convert a given number to binary, octal, and hexadecimal using the format function.
    """)
    return


@app.cell
def _():
    num = 255
    print(
        f"Decimal: {num} | Binary: {format(num, 'b')} | Octal: {format(num, 'o')} | Hexadecimal: {format(num, 'X')}"
    )
    return


@app.cell
def _(mo):
    mo.md(r"""
        Excercise 05: Suppose you have given an character "A", and your task is to print from A to G. You can not use manual process rather you have to use the ASCII code and a while loop to print all of them.
    """)
    return


@app.cell
def _():
    ascii_code = ord("A")
    end_code = ascii_code + 6

    while ascii_code < end_code:
        print(f"Character: {chr(ascii_code)} | ASCII code: {ascii_code}")
        ascii_code += 1
    return


@app.cell
def _(mo):
    mo.md(r"""
        Excercise 06: Now, the same task of Excercise 05 has to be done but using a for loop.
    """)
    return


@app.cell
def _():
    ascii_code = ord("A")
    end_code = ascii_code + 6

    for code in range(ascii_code, end_code):
        print(f"Character: {chr(code)} | ASCII code: {code}")
    return


@app.cell
def _(mo):
    mo.md(r"""
        Excercise 07: This task is a bit of fun! What you have to do is to print 6 different city names but has to take the input in the variable from A to G.
    """)
    return


@app.cell
def _():
    site_name = chr(65)
    end_site = chr(ord(site_name) + 6)

    for site in range(ord(site_name), ord(end_site)):
        city = chr(site)
        city = input("Enter a city name: ")
        print(f"City name: {city} | Variable name: {chr(site)}")
    return


@app.cell
def _(mo):
    mo.md(r"""
        Excercise 08: Here, you have to take an input from the user and convert it to an integer.
    """)
    return


@app.cell
def _():
    _val = input("Enter a number: ")
    print(f"Value before conversion: {_val} | Type: {type(_val)}")

    _val = int(_val)
    print(f"Value after conversion: {_val} | Type: {type(_val)}")
    return


@app.cell
def _(mo):
    mo.md(r"""
        Excercise 09: Here, you have to uppercase the string.
    """)
    return


@app.cell
def _():
    str = "hello world"
    print(str.upper())
    return


if __name__ == "__main__":
    app.run()
