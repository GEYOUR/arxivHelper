# arxivHelper

arxivHelper is a Python program that helps organize files for latex research projects. It searches for all pdf files within a given directory path and its subdirectories, and moves them to the given directory path while prefixing their filenames with the directory names leading to the given path.

Additionally, arxivHelper can edit LaTeX files. It searches for strings matching `\includegraphics[*]{path}`, which is the LaTeX command for including graphics from the file indicated by the "path" argument. It then splits the path and concatenates the last two names of the path to be the new path, and replaces the old path with the new path.

## How to use

Run:

```
python main.py
```

The program is currently in the development stage.


