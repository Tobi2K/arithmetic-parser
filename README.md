# Arithmetic Parser
A simple parser to parse and evaluate arithmetic strings (e.g., `(2+3)*4ˆ(2)`).
The parser supports the operations:
* Addition: `+`
* Subtraction: `-`
* Multiplication: `*`
* Division: `/`
* Parentheses: `()`
* Power: `^`

The operator precedence is `^ > *,/ > +,-`, with `*` and `/` as well as `+` and `-` having the same precedence.

The parser reads the given string and outputs the correct result.

## Usage
Start the parser with:
```shell
python parser.py
```
The parser runs until an invalid equation is entered.

A sample use would look like this:
```shell
Enter your equation: 
3+9
Result: 12.0


Enter your equation: 
2^5
Result: 32.0


Enter your equation: 
2+5/3*2
Result: 5.333333333333334


Enter your equation: 
(1+1))
Exception: Could not parse (1+1)); Reading: )
```
Note that the numbers are converted to floats.

You can also enable debugging by setting the `print_debug` variable to True.
This shows every recursive descent step according to the following grammar:
- `E => TE'`
- `E' => +TE' | -TE' | ε`
- `T => PT'`
- `T' => *PT' | /PT' | ε`
- `P => RQ`
- `Q => ^P | ε`
- `R => -F | F`
- `F => (E) | <number>`
