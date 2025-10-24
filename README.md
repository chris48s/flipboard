# flipboard

CLI tool for applying useful transformations to text on the clipboard

## Usage

### copy text to the clipboard: 

```
cat in.txt > flipboard stdin
flipboard stdin < in.txt
```

### apply transformations:

```
flipboard [encode|decode] [base64|url]
flipboard [minify|pprint] [json|xml]
flipboard trim
```

### write out clipboard contents:

```
flipboard stdout
flipboard stdout > out.txt
```
