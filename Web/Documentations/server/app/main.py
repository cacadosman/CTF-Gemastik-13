from flask import Flask, render_template
from flask import render_template_string
import re

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/docs')
@app.route('/docs/<name>')
def docs(name=None):
    blacklisted = [
        'config',
        'request',
        'url_for',
        'builtins'
        'import',
        'attr',
        'join',
        'map',
        'get',
        'namespace',
        'lipsum',
        'range',
        'session',
        'dict',
        'cycler',
        'joiner',
        'func_globals',
        'subclasses',
        'class',
        'base',
        'mro',
        'init',
        'globals',
        'decode',
        'hex',
        'chr',
        'doc',
        'eval',
        'popen',
        'system',
        'read',
        'self',
        'args',
        ' ',
        '\\',
        '+',
        '.',
        'IFS',
        '{',
        '}',
        '|',
        '%',
        ',',
        '-',
        '&',
        '>',
        '`',
        '$'
    ]

    if name:
        for b in blacklisted:
            if b in name:
                return 'The following character are not allowed', 403

        title = re.sub('[}{]*', '', ''.join(name.split()))
        name = '{{ %s.__doc__ }}' % (name)

        return render_template('docs.html', title=title, name=render_template_string(name))
    else:
        return render_template('index.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=4444, debug=False)