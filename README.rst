===============================================================
GoogleFreeTrans: Free Google translate API for Python
===============================================================
|GitHub license| |travis status| |Documentation Status| |PyPI version|
|Coverage Status| |Code Climate|
python 3.4+

----------
Quickstart
----------
You can install it from PyPI:

.. sourcecode:: bash

   $ pip install GoogleFreeTrans

..
or manual install:

.. sourcecode:: bash

   $ python setup.py test
   $ python setup.py install

..

~~~~~~~~~~~~~~~~~~~~~~~~~~~
single sentence translation
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: python

    >>> from GoogleFreeTrans import Translator
    >>> translator = Translator.translator(scr='en', dest='fr')
    >>> translator.translate('china')
    'Chine'

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
multiple sentence translation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: python

   >>> from GoogleFreeTrans import Translator
   >>> translator = Translator.translator(scr='en', dest='fr')
   >>> translator.translate('china. french')
   [[['Chine. ', 'china.', None, None, 1],  ['français.', 'french.', None, None, 1]], None, 'en']

----------------
support language
----------------

.. code::

  'afrikaans': 'af',
  'arabic': 'ar',
  'belarusian': 'be',
  'bulgarian': 'bg',
  'catalan': 'ca',
  'czech': 'cs',
  'welsh': 'cy',
  'danish': 'da',
  'german': 'de',
  'greek': 'el',
  'english': 'en',
  'esperanto': 'eo',
  'spanish': 'es',
  'estonian': 'et',
  'persian': 'fa',
  'finnish': 'fi',
  'french': 'fr',
  'irish': 'ga',
  'galician': 'gl',
  'hindi': 'hi',
  'croatian': 'hr',
  'hungarian': 'hu',
  'indonesian': 'id',
  'icelandic': 'is',
  'italian': 'it',
  'hebrew': 'iw',
  'japanese': 'ja',
  'korean': 'ko',
  'latin': 'la',
  'lithuanian': 'lt',
  'latvian': 'lv',
  'macedonian': 'mk',
  'malay': 'ms',
  'maltese': 'mt',
  'dutch': 'nl',
  'norwegian': 'no',
  'polish': 'pl',
  'portuguese': 'pt',
  'romanian': 'ro',
  'russian': 'ru',
  'slovak': 'sk',
  'slovenian': 'sl',
  'albanian': 'sq',
  'serbian': 'sr',
  'swedish': 'sv',
  'swahili': 'sw',
  'thai': 'th',
  'filipino': 'tl',
  'turkish': 'tr',
  'ukrainian': 'uk',
  'vietnamese': 'vi',
  'yiddish': 'yi',
  'chinese_simplified': 'zh-CN',
  'chinese_traditional': 'zh-TW'
