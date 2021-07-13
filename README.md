# Personal Profile Repo

If you would want to replicate this github page you can clone this repository and 
change as you wish.
```bash
$ git clone https://github.com/jezur/jezur.github.io
```
I could enable mathematical notation using **MathJax** by modifying the 
[`_includes/head.html` file](_includes/head.html) from the 
[minima theme](https://github.com/jekyll/minima). 
If you are using a jekyll theme, you can get the location of 
all the files of the theme by using 
```bash
$ bundle info --path THEMENAME
```

I added the `mathjax_support`
file in my `_includes` directory. The file was taken from 
[*Haixing-Hu*'s repository](https://github.com/Haixing-Hu/Haixing-Hu.github.io). 
After adding the `mathjax_support` file to yout `_includes` you only have 
to add this to the head section of the `default.html` file. I did this in 
the `head.html` file since it is imported by `default.html` in the case
of the **minima** theme.  
