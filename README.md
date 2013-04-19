## What have you done to the Google slides?!

I've taken the liberty of heavily modifying the IO 2013 slides:

https://code.google.com/p/io-2013-slides/

My changes were done with the intention of making these slides into something useful for giving scientific talks.  

 - Removed all mobile device features
 - Focus *only* on editing markdown files
 - Move *all* slide information (including title + authors) into the markdown file.
 - Enable the use of "raw" type slides, where the user inserts raw HTML for totally custom look.  Note: this is currently whitespace-sensitive.
 - Enable the use of mathJax for equation typesetting.  This requires you to install the mathjax markdown plugin:
 
 https://github.com/mayoff/python-markdown-mathjax
 
 I found that I had to rename their python extension as `mathjax.py` to get
 things to work properly.  

## Compiling slides

Go to `scripts/md/`

    $./render.py slides.md ../../out.html --extensions mathjax
    
There are currently pathing issues, so some of the paths are kinda hardcoded.

## Running the slides

The slides can be run locally from `file://` making development easy :)

### Running from a web server

If at some point you should need a web server, use [`serve.sh`](serve.sh). It will
launch a simple one and point your default browser to [`http://localhost:8000/template.html`](http://localhost:8000/template.html):

    $ cd io-2012-slides
    $ ./serve.sh

You can also specify a custom port:

    $ ./serve.sh 8080

### Presenter mode

The slides contain a presenter mode feature (beta) to view + control the slides
from a popup window.

To enable presenter mode, add `presentme=true` to the URL: [http://localhost:8000/template.html?presentme=true](http://localhost:8000/template.html?presentme=true)

To disable presenter mode, hit [http://localhost:8000/template.html?presentme=false](http://localhost:8000/template.html?presentme=false)

Presenter mode is sticky, so refreshing the page will persist your settings.

---

### Editing the CSS / SCSS templates

First, install compass:

    sudo gem update --system
    sudo gem install compass

Next, you'll want to watch for changes to the exiting .scss files in [`/theme/scss`](theme/scss)
and any new one you add:

    $ cd io-2012-slides
    $ compass watch

This command automatically recompiles the .scss file when you make a change.
Its corresponding .css file is output to [`/theme/css`](theme/css). Slick.

By default, [`config.rb`](config.rb) in the main project folder outputs minified
.css. It's a best practice after all! However, if you want unminified files,
run watch with the style output flag:

    compass watch -s expanded

*Note:* You should not need to edit [`_base.scss`](theme/scss/_base.scss).


## Editing CSS

[Compass](http://compass-style.org/install/) is a CSS preprocessor used to compile
SCSS/SASS into CSS. We chose SCSS for the new slide deck for maintainability,
easier browser compatibility, and because...it's the future!

That said, if not comfortable working with SCSS or don't want to learn something
new, not a problem. The generated .css files can already be found in
(see [`/theme/css`](theme/css)). You can just edit those and bypass SCSS altogether.
However, our recommendation is to use Compass. It's super easy to install and use.

