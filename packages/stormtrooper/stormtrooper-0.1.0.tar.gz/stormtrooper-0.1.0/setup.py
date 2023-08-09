# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['stormtrooper']

package_data = \
{'': ['*']}

install_requires = \
['numpy>=1.23.0,<2.0.0',
 'scikit-learn>=1.2.0,<2.0.0',
 'tqdm>=4.60.0,<5.0.0',
 'transformers>=4.25.0,<5.0.0']

setup_kwargs = {
    'name': 'stormtrooper',
    'version': '0.1.0',
    'description': 'Transformer-based zero and few-shot classification in scikit-learn pipelines',
    'long_description': '# stormtrooper\nTransformer-based zero/few shot learning components for scikit-learn pipelines.\n\n## Example\n\n```bash\npip install stormtrooper\n```\n\n```python\nfrom stormtrooper import ZeroShotClassifier\n\nclass_labels = ["atheism/christianity", "astronomy/space"]\nclassifier = ZeroShotClassifier().fit(None, class_labels)\n\nexample_texts = [\n    "God came down to earth to save us.",\n    "A new nebula was recently discovered in the proximity of the Oort cloud."\n]\npredictions = classifier.predict(example_texts)\n\nassert list(predictions) == ["atheism/christianity", "astronomy/space"]\n```\n',
    'author': 'Márton Kardos',
    'author_email': 'power.up1163@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
