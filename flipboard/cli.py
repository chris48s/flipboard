import json
from base64 import b64encode, b64decode
from urllib.parse import quote, unquote
import click
import pyperclip
import xmlformatter
import xml.parsers.expat


@click.group()
def cli():
    pass


@cli.command()
@click.argument('encoding', type=click.Choice(['base64', 'url']), required=True)
def encode(encoding):
    input_ = pyperclip.paste()

    if encoding == 'url':
        return pyperclip.copy(quote(input_))

    if encoding == 'base64':
        tmp = input_.encode('ascii')
        tmp = b64encode(tmp)
        tmp = tmp.decode('ascii')
        return pyperclip.copy(tmp)

    raise NotImplementedError()


@cli.command()
@click.argument('encoding', type=click.Choice(['base64', 'url']), required=True)
def decode(encoding):
    input_ = pyperclip.paste()

    if encoding == 'url':
        return pyperclip.copy(unquote(input_))

    if encoding == 'base64':
        tmp = input_.encode('ascii')
        tmp = b64decode(tmp)
        tmp = tmp.decode('ascii')
        return pyperclip.copy(tmp)

    raise NotImplementedError()


@cli.command()
@click.argument('language', type=click.Choice(['json', 'xml']), required=True)
def pprint(language):
    input_ = pyperclip.paste()

    if language == 'json':
        try:
            return pyperclip.copy(json.dumps(json.loads(input_), indent=2))
        except json.decoder.JSONDecodeError:
            return

    if language == 'xml':
        if '<' not in input_ or '>' not in input_:
            return
        formatter = xmlformatter.Formatter(indent="2", indent_char=" ")
        try:
            return pyperclip.copy(
                formatter.format_string(input_).decode(formatter.encoding_effective)
            )
        except xml.parsers.expat.ExpatError:
            return

    raise NotImplementedError()


@cli.command()
@click.argument('language', type=click.Choice(['json', 'xml']), required=True)
def minify(language):
    input_ = pyperclip.paste()

    if language == 'json':
        try:
            return pyperclip.copy(json.dumps(json.loads(input_)))
        except json.decoder.JSONDecodeError:
            return

    if language == 'xml':
        if '<' not in input_ or '>' not in input_:
            return
        formatter = xmlformatter.Formatter(compress=True, indent_char=" ")
        try:
            return pyperclip.copy(
                formatter.format_string(input_).decode(formatter.encoding_effective)
            )
        except xml.parsers.expat.ExpatError:
            return

    raise NotImplementedError()


@cli.command()
def trim():
    input_ = pyperclip.paste()
    return pyperclip.copy(input_.strip())
