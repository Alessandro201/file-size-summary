# file-size-summary

Provide a summary of the total size of the files divided by file types

## Installation
If you have Rye, installing the script and making it available everywhere it's as simple as:

```bash
git clone https://github.com/Alessandro201/file-size-summary.git
rye install . -force
```

## Usage
Just pass to `fss` all the paths you want to check:
```bash
$ cd file-size-summary
$ fss .
269.0K 	Total
164.8K 	<NoExtension>
49.1K 	.12
23.0K 	.sample
7.9K 	.py
5.1K 	.bat
4.1K 	.fish
4.1K 	.pyc
3.8K 	.nu
2.7K 	.ps1
2.6K 	.csh
510.0B 	.lock
503.0B 	.toml
229.0B 	.pth
211.0B 	.json
203.0B 	.cfg
92.0B 	.md
61.0B 	.txt
43.0B 	.TAG
```
