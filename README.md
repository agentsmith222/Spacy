# Spacy on Python 3.5.2

## Ensure that you are on Python > 3.5

```python --version```

My system returns, for example:

Python 3.5.2 :: Anaconda 4.1.1 (x86_64)

## Install Spacy

```pip install -U --user spacy```

The U flag stands for upgrade to the latest.

User flag is needed for permissions.

"Building wheel for Spacy" will require a lot of time to run

## Install Spacy (Full Directions)

https://spacy.io/usage

## Install Spacy Module for the Hello World Script

```python -m spacy download en_core_web_sm```

## hello spacy world

Tutorial to Setup Spacy on Python 3.5.2 for Parsing Parts of Speech of Text

## Run The Program

```python helloworld.py```

## Parse sentences and identify patterns that you like

### "That's a really nice Github"

That DET nsubj

is VERB ROOT

a DET det

really ADV advmod

nice ADJ amod

Github PROPN attr

### Pattern

DET nsubj, VERB ROOT, DET det, ADV advmod, ADJ amod, PROPN attr

### References

https://spacy.io/usage


