import os
import csv
import sys
import json
import codecs

import click

from . import Article, version_info


epilog = click.style('''\n
\b
example:
    {prog} url1 url2 url3
    {prog} urls.txt
    {prog} urls.txt -o out.jl                     
    {prog} urls.txt -o out.json -f json                
    {prog} urls.txt -o out.json -f json -i 2
    {prog} urls.txt -o out.csv -f csv                    
    {prog} urls.txt -o out.csv -f csv -e utf-8-sig   [BOM mode for Office Excel]           
    {prog} urls.txt -o out.xls -f csv -e utf-8-sig -s '\\t'                 

contact: {author} <{author_email}>             
''', fg='cyan').format(**version_info)


CONTEXT_SETTINGS = dict(help_option_names=['-?', '-h', '--help'])

@click.command(
    name=version_info['prog'],
    help=click.style(version_info['desc'], italic=True, fg='green', bold=True),
    context_settings=CONTEXT_SETTINGS,
    no_args_is_help=True,
    epilog=epilog,
)
@click.argument('urls', nargs=-1)
@click.option('-o', '--outfile', help='the output filename [stdout]')
@click.option('-f', '--outfmt', help='the format of output', type=click.Choice(['jl', 'json', 'csv']), default='jl', show_choices=True)
@click.option('-d', '--delimiter', help='the delimiter for csv output', default=',', show_default=True)
@click.option('-e', '--encoding', help='the encoding for output', default='utf-8')
@click.option('-i', '--indent', help='the indent for json output', type=int)
@click.option('-p', '--print-text', help='only print the text', is_flag=True)
@click.version_option(version=version_info['version'], prog_name=version_info['prog'])
def cli(urls, outfile, outfmt, indent, delimiter, encoding, print_text):
    delimiter = codecs.decode(delimiter, 'unicode_escape')

    out = open(outfile, 'w', encoding=encoding) if outfile else sys.stdout
    data = []
    with out:

        if outfmt == 'csv':
            csv_writer = csv.writer(out, delimiter=delimiter)
            csv_writer.writerow(['#Title', 'Text', 'Url'])

        if len(urls) == 1 and os.path.isfile(urls[0]):
            urls = [line.strip() for line in open(urls[0]) if line.strip()]

        for url in urls:
            article = Article(url)

            if print_text:
                print(article.full_text)
                continue

            if outfmt == 'tsv':
                line = '\t'.join([article.title, repr(article.full_text)])
            elif outfmt == 'csv':
                csv_writer.writerow([article.title, article.full_text])
                continue
            elif outfmt == 'jl':
                context = dict(title=article.title, text=article.full_text, url=article.url)
                line = json.dumps(context, ensure_ascii=False)
            elif outfmt == 'json':
                data.append(dict(title=article.title, text=article.full_text, url=article.url))
                continue
            out.write(line + '\n')
        if outfmt == 'json':
            out.write(json.dumps(data, ensure_ascii=False, indent=indent) + '\n')


def main():
    cli()


if __name__ == '__main__':
    main()
