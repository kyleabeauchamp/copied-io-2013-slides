#!/usr/bin/env python

import codecs
import re
import jinja2
import markdown
import argparse

BASE_HTML = "base.html"

def process_slides(md_filename, html_filename, extensions = []):
    """Process markdown and write HTML slides.

    Parameters
    ----------
    md_filename : str
        Filename of input markdown file.
    html_filename : str
        Filename of ouput HTML file.
    extensions : list, optional
        List of markdown extensions to use.  e.g. ['mathjax']
    """
    with codecs.open(html_filename, 'w', encoding='utf8') as outfile:
        md = codecs.open(md_filename, encoding='utf8').read()
        md_slides = md.split('\n---\n')
        print 'Compiled %s slides.' % len(md_slides)

        slides = []
        # Process each slide separately.
        for md_slide in md_slides:
            slide = {}
            sections = md_slide.split('\n\n')
            # Extract metadata at the beginning of the slide (look for key: value) pairs.
            metadata_section = sections[0]
            metadata = parse_metadata(metadata_section)
            slide.update(metadata)
            remainder_index = metadata and 1 or 0
            # Get the content from the rest of the slide.
            content_section = '\n\n'.join(sections[remainder_index:])
            html = markdown.markdown(content_section, extensions=extensions)
            slide['content'] = postprocess_html(html, metadata)

            slides.append(slide)

        template = jinja2.Template(open(BASE_HTML).read())

        outfile.write(template.render(locals()))

def parse_metadata(section):
    """Given the first part of a slide, returns metadata associated with it."""
    metadata = {}
    metadata_lines = section.split('\n')
    for line in metadata_lines:
        colon_index = line.find(':')
        if colon_index != -1:
            key = line[:colon_index].strip()
            val = line[colon_index + 1:].strip()
            metadata[key] = val

    return metadata

def postprocess_html(html, metadata):
    """Returns processed HTML to fit into the slide template format."""
    if metadata.get('build_lists') and metadata['build_lists'] == 'true':
        html = html.replace('<ul>', '<ul class="build">')
        html = html.replace('<ol>', '<ol class="build">')
    return html

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Render Markdown into HTML5 slides.')

    parser.add_argument('md_filename', metavar='m', type=str, help='Filename for markdown input.')
    parser.add_argument('html_filename', metavar='o', type=str, help='Filename for HTML output.')
    parser.add_argument('--extensions', metavar='e', type=str, help='List of extensions needed for compilation.  e. g. "mathjax"', default=[], nargs="*")

    args = parser.parse_args()
    process_slides(args.md_filename, args.html_filename, args.extensions)
