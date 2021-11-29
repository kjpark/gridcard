# Qwest Gridcard
a tool to speed up login to Qwest SSO

# Use
after cloning / copying the code...
1. edit `config.py` to match your gridcard
2. `python3 gridcard.py`

valid syntax is case-insensitive:
```
a1 b2 c3
A1B2C3
[a1][b2][c3]
[A1] [B2] [C3]
E2] [H1] [H4 # partial entries containing all essential info OK
```

you can set up an alias if you'd like

`alias grid="python3 ~/path/to/gridcard.py"`


to include copy to clipboard option

1. first run `pip install requirements.txt` from within this directory

1. In config.py change autoCopy value to `True`


# Warnings / Disclaimer
this is not an official tool, use at your own risk.
if you'd like to contribute, please DO NOT commit your
personal gridcard contents anywhere.
