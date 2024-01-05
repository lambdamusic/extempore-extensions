# Extempore Extensions

My custom extensions to the [Extempore](https://extemporelang.github.io/) programming environment.

## Overview

A bunch of scheme abstractions that I developed in order to create Extempore musical algorithms more efficiently and more naturally. 

No documentation yet, but various examples of what the extensions look like are available on [The Musical Code](https://github.com/lambdamusic/The-Musical-Code) and its counterpart [YouTube channel](https://www.youtube.com/channel/UCanqSICbxzRNEZGMlu8qfyw).  

NOTE: The extensions have been developed to support **MIDI** composition / livecoding primarily.

Files 

* `init_midi` helpers for playing midi instruments
* `init_beats` metro+beat utils
* `init_music` utils to generate chord structures
* `init_steps` midi step sequencer 
* `init_symbols` notes symbols 
* `init_utils` lisp and scheme utils 

## How to Use

### 1. Grab the repo and update its configuration

After cloning the repo, there are a couple of settings at the top of [LOAD_ALL.xtm](https://github.com/lambdamusic/extempore-extensions/blob/main/LOAD_ALL.xtm) that should be updated.

```scheme
(define *extensions-path* 
  "/Users/michele.pasin/Dropbox/code/extempore/src/xtm-extensions/init/")

(define *DEFAULT_MIDI_DEVICE_NAME* 
  "IAC Driver Extempore Bus")
```

Explanation: 

* `*extensions-path*`: your local filepath where the extensions files have been saved
* `*DEFAULT_MIDI_DEVICE_NAME*`: the main MIDI device you are using ( as displayed with `(pm_print_devices)` ) 


### 2. Set up the Extempore startup command

Extempore allows to pass a startup script at runtime, e.g.: 

```
./extempore --run {YOUR-FILE}.xtm
```

The extensions root folder includes a helper file [LOAD_ALL.xtm](https://github.com/lambdamusic/extempore-extensions/blob/main/LOAD_ALL.xtm) that can be used as a startup script, so to to load up all the extensions in the `init` folder. 

Hence you can set things up like this in your `bash_profile`: 

```bash
export EXTEMPORE_RUNTIME="/your/extempore/runtime/installation/"
export EXTEMPORE_EXTENSIONS="/your/path/to/these/extensions/"

alias xtm-plus="cd $EXTEMPORE_RUNTIME;./extempore --frames 256 --run '$EXTEMPORE_EXTENSIONS'LOAD_ALL.xtm"
```


## VSCode resources

The [backups](backups/) folder contains snippets and keybindings files for VSCode, as well as other potentially reusable bits and pieces. 


## See also

- [Extempore language project](https://github.com/digego/extempore)
- Unofficial Extempore [Functions Explorer](https://extempore.michelepasin.org/) 
- [The Musical Code](https://github.com/lambdamusic/The-Musical-Code) and its counterpart [YouTube channel](https://www.youtube.com/channel/UCanqSICbxzRNEZGMlu8qfyw)
- [My livecoding blog](https://www.michelepasin.org/words/index.html%3Ftag=algorithmiccomposition&type=all.html)
- Livecoding community: [TOPLAP](https://toplap.org/about/)

## Changelog

* 2023-11-24: VScode snippets moved to [backups](backups/vscode-snippets/) folder.