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

I added an *if statement* at the end of the `head.html` file that includes the 
latest [mathjax support](http://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML)
file whith some configurations. I used the configurations found in the 
file `_includes/mathjax_support` from [*Haixing-Hu*'s repository](https://github.com/Haixing-Hu/Haixing-Hu.github.io). 
They did it in a similar manner. Now, normaly  you would  only have
to add the following lines of code to the head section of the `default.html` file. I did this in 
the `head.html` file since it is imported by `default.html` in the case
of the **minima** theme. 
```html
{% if page.usemathjax %}
<script type="text/x-mathjax-config">
  MathJax.Hub.Config({
    TeX: { 
      equationNumbers: {autoNumber: "AMS"} },
    tex2jax: {
      inlineMath: [ ['$','$'], ['\(', '\)'] ],
      displayMath: [ ['$$','$$'] ],
      processEscapes: true,
    }
  });
</script>
<script type="text/javascript"
      src="http://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML">
</script>
{% endif %}
```

Then, wherever you use the *Latex syntax* you add this to the header of the 
markdown file:
```markdown
---
...
use_math = true
---
``` 
