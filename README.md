# Personal Profile Repo

If you would want to replicate this github page you can clone this repository and 
change as you wish.
```bash
$ git clone https://github.com/jezur/jezur.github.io
```
I could enable *Latex mathematical syntax* using **MathJax** by adding a copy of the 
[`_includes/head.html` file](_includes/head.html) from the 
[minima theme](https://github.com/jekyll/minima) to my `_includes` folder,
and then modifying it. 
If you are using a jekyll theme, you can get the location of 
all the files of the theme by using 
```bash
$ bundle info --path THEMENAME
```

I added an *if statement* at the end of the `head.html` file that includes a 
[mathjax support](https://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-MML-AM_CHTML)
file whith some configurations. I used the configurations found in the 
file `_includes/mathjax_support` from [*Haixing-Hu*'s repository](https://github.com/Haixing-Hu/Haixing-Hu.github.io), 
and also read [this comment by *sudhirln92*](https://github.com/mmistakes/minimal-mistakes/issues/735),
and [this post](http://csega.github.io/mypost/2017/03/28/how-to-set-up-mathjax-on-jekyll-and-github-properly.html).
I guess what worked for me was `sourcing` the correct mathjax scripts and using all 
the correct *tex2jax* characters.
They all did this in a similar manner. Now, normaly  you would  only have
to add the following lines of code to the head section of the `default.html` file. I did this in 
the `head.html` file since it is imported by `default.html` in the case
of the **minima** theme. 
```html
<!-- mathjax support -->
{% if page.usemathjax %}
<script type="text/x-mathjax-config">
  MathJax.Hub.Config({
    TeX: { equationNumbers: {autoNumber: "AMS"} },
    extensions: ["tex2jax.js"],
    jax: ["input/TeX", "output/HTML-CSS"],
    tex2jax: {inlineMath: [ ['$','$'], ['\\(', '\\)'] ], 
    		displayMath: [ ['$$','$$'], ["\\[","\\]"] ], 
    		processEscapes: true,}
  });
</script>
<script type="text/javascript"
  src="https://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-MML-AM_CHTML">
</script>
{% endif %}
```

Then, wherever you use the *Latex syntax* add this to the YAML front matter of the 
markdown file:
```markdown
---
...
usemathjax = true
---
``` 
