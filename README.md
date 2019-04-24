# Spacy on Python 3
## hello spacy world

Tutorial to Setup Python 3's Spacy for Machine Learning Natural Language

```python helloworld.py```

## Parse sentences and identify patterns that you like and dislike

### Dislike

### "you are someone trying to get free labor"

you PRON nsubj

are VERB ROOT

someone NOUN attr

trying VERB acl

to PART aux

get VERB xcomp

free ADJ amod

labor NOUN dobj

### Like

### "That's a really nice Github"

That DET nsubj

is VERB ROOT

a DET det

really ADV advmod

nice ADJ amod

Github PROPN attr

## Ensure that you are on Python 3

```python --version```

My system returns, for example:

Python 3.5.2 :: Anaconda 4.1.1 (x86_64)

## Install Spacy

```pip install -U --user spacy```

The U flag stands for upgrade to the latest.

User flag is needed for permissions.

"Building wheel for Spacy" will require a lot of time to run

## Install Spacy Module for the Hello World Script

```python -m spacy download en_core_web_sm```

### References

https://spacy.io/usage
