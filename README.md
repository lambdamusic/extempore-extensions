# Extempore Extensions

My custom extensions to the [Extempore](https://extemporelang.github.io/) programming environment.

## Overview

A bunch of scheme abstractions that I developed in order to create Extempore musical algorithms more efficiently and more naturally. 

No documentation yet, but various examples of what the extensions look like are available on [The Musical Code](https://github.com/lambdamusic/The-Musical-Code) and its counterpart [YouTube channel](https://www.youtube.com/channel/UCanqSICbxzRNEZGMlu8qfyw).  

Files 

* `init_midi` helpers for playing midi instruments
* `init_beats` metro+beat utils
* `init_music` utils to generate chord structures
* `init_steps` midi step sequencer 
* `init_symbols` notes symbols 
* `init_utils` lisp and scheme utils 

## How to Use

Extempore allows to pass a startup script at runtime, e.g.: 

```
./extempore --run {YOUR-FILE}.xtm
```

Hence you can set things up like this in your `bash_profile`: 

```bash
export EXTEMPORE_RUNTIME="/your/extempore/runtime/installation/"
export EXTEMPORE_EXTENSIONS="/your/path/to/these/extensions/"

alias xtm-plus="cd $EXTEMPORE_RUNTIME;./extempore --frames 256 --run '$EXTEMPORE_EXTENSIONS'LOAD_ALL.xtm"
```


## See also

- [The Musical Code](https://github.com/lambdamusic/The-Musical-Code) and its counterpart [YouTube channel](https://www.youtube.com/channel/UCanqSICbxzRNEZGMlu8qfyw)
- Unofficial Extempore [Functions Explorer](https://extempore.michelepasin.org/) 
- [My livecoding blog](https://www.michelepasin.org/words/index.html%3Ftag=algorithmiccomposition.html) 
- Livecoding community: [TOPLAP](https://toplap.org/about/)
