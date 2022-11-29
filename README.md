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
Exception: Could not parse '(1+1)'); Reading: )
```
Note that the numbers are converted to floats.

You can also enable debugging by adding the `--debug` command-line argument.
This shows every recursive descent step according to the following grammar:
- `E => TE'`
- `E' => +TE' | -TE' | ε`
- `T => PT'`
- `T' => *PT' | /PT' | ε`
- `P => RQ`
- `Q => ^P | ε`
- `R => -F | F`
- `F => (E) | <number>`


## License

MIT License

Copyright (c) 2022 Tobias Kalmbach

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions: The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software. 

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

---

> [kalmbach.dev](https://www.kalmbach.dev) &nbsp;&middot;&nbsp;
> GitHub [@Tobi2K](https://github.com/Tobi2K) &nbsp;&middot;&nbsp;
> Email [tobias@kalmbach.dev](mailto:tobias@kalmbach.dev)