# Personal Profile Repo

If you would want to replicate this github page you can clone this repository and 
change as you wish.
```bash
$ git clone https://github.com/jezur/jezur.github.io
```
I could enable mathematical notation using **MathJax** by adding a copy of the 
[`_includes/head.html` file](_includes/head.html) from the 
[minima theme](https://github.com/jekyll/minima) to my `_includes` folder. 
If you are using a jekyll theme, you can get the location of 
all the files of the theme by using 
```bash
$ bundle info --path THEMENAME
```

I added the `mathjax_support`
file in my `_includes` directory since it enables the funcitionality. The file was taken from 
[*Haixing-Hu*'s repository](https://github.com/Haixing-Hu/Haixing-Hu.github.io). 
After adding the `mathjax_support` file to your `_includes` you only have 
to add the following lines of code to the head section of the `default.html` file. I did this in 
the `head.html` file since it is imported by `default.html` in the case
of the **minima** theme.  
```html
<!-- support the MathJax if necessary -->
{% if page.use_math %}
  {% include mathjax_support %}
{% endif %}
```
