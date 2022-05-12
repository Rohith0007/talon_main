from __future__ import absolute_import
from distutils.core import setup


setup(name='talon_main',
	packages = ['talon'],
      version='0.2',
      description=("Mailgun library "
                   "to extract message quotations and signatures."),
      license='APACHE2',
      
      include_package_data=True,
      zip_safe=True,
      install_requires=[
          "lxml",
          "regex",
          "numpy",
          "scipy",
          "scikit-learn>=1.0.0",
          "chardet",
          "cchardet",
          "cssselect",
          "six",
          "html5lib",
          "joblib",
          ],
      tests_require=[
          "mock",
          "nose",
          "coverage"
          ]
      )
