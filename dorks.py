def generate_dorks(query):
    # Basic dorks, can extend with templates
    templates = [
        'site:linkedin.com/in "{}"',
        'site:github.com "{}"',
        'intitle:"resume" "{}"',
        'inurl:"cv" "{}"',
        'site:twitter.com "{}"',
        'site:facebook.com "{}"',
        '"{}" filetype:pdf',
        'site:pastebin.com "{}"',
    ]
    return [t.format(query) for t in templates]
