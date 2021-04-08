# index-for-datasets-and-models

Here are a few datasets prepared to be imported into Torchtext. You may find the datasets useful, but probably not. There are also various pretrained models, with different training strategy. The models may even have different architecture. We will not put more information here, since we haven't figured out which model works best.

Certainly, you are confused. Just contact me if you'd like to know more about what's happening here!

## Usage
Supposed you'd like to download a model and a pair of datasets into your current working path
```python
from puller import pull
pull('replace-3-test.json', 'replace-3-train.json', 'nlg-3-5.pt')
```

You are going to get errors for sure if trying to pull a file that is not listed in this index.
