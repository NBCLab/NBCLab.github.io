# The Lipka Lab website

# TODOS

See Issues on [the site](https://github.com/NBCLab/nbclab.github.io).

# How to add content

Because the website code is hosted on GitHub, any lab member can contribute to the site. The general pattern will be: (1) Fork the repository to your own account; (2) Clone your fork to your laptop; (3) Make changes (e.g., add a new post to News or update your bio) to your local copy; (4) Test those changes by running a local version of the website; (5) If your changes don't break the website, commit your changes to your fork's remote; (6) Open a pull request from your fork to the main repository. Once the PR is open, the website administrator will review the changes and merge them into the main website.

In order to contribute, you must have a GitHub account and you must set up Jekyll on your laptop (in order to demo your changes).

Essentially, follow the instructions [here](https://help.github.com/articles/setting-up-your-github-pages-site-locally-with-jekyll/#step-2-install-jekyll-using-bundler). Namely, do the **Requirements**, **Step 2.5**, and **Step 4**. The rest of the steps are extraneous, I think (as long as you have your fork cloned locally).

## 1. Download Ruby and install bundler
```bash
# Install Ruby, if you don't have it
\curl -sSL https://get.rvm.io | bash -s stable
rvm install ruby-2.4.1
rvm use ruby-2.4.1 --default

# Install bundler
gem install bundler
```

For OSX users, Ruby comes pre-installed on your computer, but you may not be able to install Ruby packages due to permission issues.
See https://stackoverflow.com/a/54873916/2589328 for some helpful information if you come up against this issue.

## 2. Install Jekyll and other dependencies from the GitHub Pages gem
```bash
cd /location/of/repository/
bundle install
```

## 3. Make your changes
Just edit the files to make the changes you want.

## 4. Build your local Jekyll site
```bash
cd /location/of/repository/
bundle exec jekyll serve
```

## 5. Open the local site and check your changes
Open a browser and go to `localhost:4000/`. Any changes you make to any of the repository's files, except `_config.yml`, will be reflected on the site after refreshing the page. If you edit `_config.yml`, you will need to quit the local server (`Ctrl+C`) and rebuild the site locally in order to see your changes.

# How the site is set up
The structure can be a little confusing, but I'll try to outline the basics.
Still, here it goes:

## Framework and tools

This website (and most GitHub Pages-based sites) uses [Jekyll](https://jekyllrb.com).
Jekyll uses HTML, CSS, [Liquid](https://shopify.github.io/liquid/), and Markdown to produce [static](https://en.wikipedia.org/wiki/Static_web_page) websites.
This website also uses the Bootstrap framework via [JekyllBootstrap](http://jekyllbootstrap.com) and SASS (a CSS preprocessing tool).

Okay, so what does this all mean to the layperson?

HTML is the basic language for making websites.
Everything is more or less built off of HTML, but HTML is ugly and writing raw HTML generally means a lot of duplication that is hard to maintain.

Markdown is the simple markup language used throughout GitHub; Jekyll lets you specify content in Markdown files (easy to write) that is rendered into HTML files automatically, instead of having to work directly with HTML (harder to write).

CSS and SASS provide style-sheets, which are sets of custom formatting commands that the HTML code can use.
We currently only have a SASS style-sheet.

Liquid is a "template language" that lets you write more standard code (e.g., working with variables) in your HTML and Markdown files.
Liquid is essential, but frustratingly limited.

Bootstrap is a CSS framework with CSS and Javascript design templates.

JekyllBootstrap shares a number of shortcuts, including interfaces for social networking sites like Twitter.
It is also what lets us switch between themes (more on that later), which we probably don't even want.

## Organization

The different pages (e.g., News, Papers, Team) are organized in separate folders.
Each folder contains a file for the page itself (`index.html`) and a folder containing markdown files with the different entries for the page (`_posts/`).

The markdown files for the homepage, the "About the site" page, and the "Contact us" page are all located in `misc/_posts/`.

Whether adding a new lab member, paper, poster, presentation, project, or piece of news, you will generally be creating one of these markdown files in `[type]/_posts/` where `[type]` is the type of post.

Each post (i.e., markdown file) is also rendered as its own page, with a link on the main page for the type.
For example, an individual poster corresponds to one of the markdown files in `posters/_posts/`.
That poster has its own page, and there is a link to that page on the main "Posters" page (which is generated from `posters/index.html`).

The markdown files have two sections, a header with metadata and the content below.
How the post is formatted on the general page (e.g., how Taylor Salo's picture fits into the [Team webpage](https://nbclab.github.io/team/)) is determined by the `index.html` file mentioned above.
How the post is formatted on its own page (e.g., [Taylor Salo's member page](https://nbclab.github.io/team/taylor-salo)) is determined by the theme file for that post's category.

## Themes

This website is set up so that you can switch between "themes" (i.e., sets of HTML and CSS patterns).
Files controlling the formatting of the different themes are located in `_includes/themes/[theme]/*.html` and `assets/themes[theme]/`.
The default theme for the website is "lab", but we may add other ones in the future.

Which theme is in use is controlled by the files in `_layouts`.
The theme can be changed with commands in the Rakefile.
The command to change the theme is `rake theme:switch name="[theme]"`, where `[theme]` is replaced with whatever the target theme is.
**There is very little reason to play with the themes.
Focus your formatting efforts on the `lab` theme.**

To be honest, we should probably just remove the theme functionality completely, except that it's packaged as part of JekyllBootstrap.

## Changing the formatting

The basic HTML file template is `_includes/themes/lab/default.html`.
The actual formatting for the different post types is going to be controlled by the files in `_includes/themes/lab`.
The formatting for the different group pages (e.g., "Team") is primarily controlled by the `[type]/index.html` files.

The files in `_layouts` should be left alone.
They are just there to make it easier to switch themes.

### Meta-formatting

Edit the SASS file at `_includes/themes/lab/css/style.scss`.
Don't bother messing with files in `_includes/themes/twitter`, because we don't use that theme.
Don't bother messing with files in `_includes/themes/lab/bootstrap/`, because that is a prepackaged framework.

## Assets

Pictures, pdfs, etc. can be placed in `assets/`.
Because GitHub repositories are limited in terms of space, we tend to use low-resolution images.
Any important, high-resolution files that do not need to be directly rendered on the website should be stored elsewhere (e.g., Google Drive) and linked to on the website.

In order to reduce the amount of data we use with images, we have rules for image sizes:

| Category | Width (pixels) | Height (pixels) |
|------------------|----------------|-----------------|
| Lab member photo | 200 | 200 |
| Journal cover    | 150 | variable |
| Poster           | <=375* | <=375* |
| Talk             | 1000 | variable |
| Project          | 1000 | variable |
| News             | 1000 | variable |

\* Either height or width must be 375 pixels, and the other must be less than or equal to 375 pixels.

## License

The [code for this site][0] was forked from Dr. Allan Drummond's lab website, which in turn took a great deal of inspiration from Dr. Travis Bedford's [lab website][1]. We have modified a lot of the code and added some fun features, but the core codebase is still largely taken from the Drummond lab's original repository. The code was openly shared on [GitHub][2] under the MIT license, so please feel free to adapt it for your own purposes. However, if you do use any of the code, please remember to cite the code to Dr. Drummond and to link back to his [site][3].

[0]: https://github.com/NBCLab/NBCLab.github.io
[1]: http://bedford.io
[2]: https://github.com/drummondlab/drummondlab.github.io
[3]: http://drummondlab.org/about.html


