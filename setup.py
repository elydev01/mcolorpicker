from distutils.core import setup

setup(
  name = 'mcolorpicker',
  packages = ['mcolorpicker'],
  version = '0.1.1',
  license='MIT',
  description = 'A simple, minimalist and beautiful color picker for kivy based applications. This color picker is easy to use and integrate into your application to allow your application users to choose the color in a simple way.',
  author = 'KOUA ELYSEE',
  author_email = 'elydev01@gmail.com',
  url = 'https://github.com/elydev01/mcolorpicker',
  download_url = 'https://github.com/elydev01/mcolorpicker/archive/refs/tags/1.0.tar.gz',
  keywords = ['kivy', 'color', 'picker', 'colorpicker', 'kivymd', 'choose', 'mobile'],
  install_requires=[
          'kivy',
          'kivymd',
      ],
  classifiers=[
    # Quel est le degré de maturité de ce projet ? Les valeurs courantes sont
    # 3 - Alpha
    # 4 - Bêta
    # 5 - Production/Stable
    'Development Status :: 3 - Alpha',

    # Indiquez à qui votre projet est destiné
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Widget Sets',

    # Choisissez votre licence comme vous le souhaitez
    'License :: OSI Approved :: MIT License',

    # Spécifiez ici les versions de Python que vous prenez en charge.
    # En particulier, assurez-vous que vous indiquez si vous supportez
    # Python 2, Python 3 ou les deux.
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.8'
  ],
)
