def results(fields, original_query):
    import os
    message = fields['~message']
    if not message or message.isspace():
        message = " "
    message = message.replace(" ", ".*")

    import re
    regex = re.compile(r'(' + message + ')', re.IGNORECASE)

    result = os.popen('cat /Users/rkitay/.scripts/snippets | grep -v \'^#\' | sort -f | egrep -i "'+message+'"').read();
    if not result or result.isspace():
        result = "Found no matches for '" + message + "'"
        html = "<h1>{0}</h1>".format(result)
    else:
        lines = result.split('\n')
        html = "<h1>Found {0} Result(s):</h1>".format(len(lines)-1)
	html += "<table style=\"border: fixed; border-width: 1px;\"><tr><th>Name</th><th>Data</th></tr>"
        for line in lines:
            if line and not line.isspace():
                key_value = line.split('|')
                key = key_value[0]
                key = regex.sub(r'<font color="red">\1</font>', key)
                value = key_value[1].replace("~NL~", "<br/>").replace("~PIPE~", "|")
                value = regex.sub(r'<font color="red">\1</font>', value)
                html += "<tr><td>{0}</td><td>{1}</td></tr>".format(key, value)
        html += "</table>"

    return {
        "title": "Snippets '{0}'".format(message),
        "run_args": [message], # ignore for now
        "html": html
    }


def run(message):
    import os
    os.system('say "{0}"'.format(message)) # TODO: proper escaping via pipes.quote
