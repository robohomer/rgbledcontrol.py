from distutils.core import setup

setup(
    name='rgbledcontrol.py',
    version='0.1',
    packages=['src', 'src.ledlib'],
    url='https://github.com/triphoppingman/rgbledcontrol.py',
    license='Apache',
    author='Bruce McDonald',
    author_email='el.triphop@gmail.com',
    description='Library to manipulate two kinds of WIFI RGB lights',
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 3 - Alpha',

        # Indicate who your project is intended for
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',

        # Pick your license as you wish (should match "license" above)
        'License :: OSI Approved :: Apache License',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7'
    ],
    keywords='RGB WIFI LED',
    install_requires=['twisted', 'PyParsing', 'yeelight', 'phue']
)
