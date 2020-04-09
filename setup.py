from distutils.core import setup

def README():
    return open("README.md").read()

setup(name='function_synthesizer',
    version = '0.0.1',
    description = 'Generates a polynomial interpolation from a set up points',
    author = 'David J. Kowalk',
    author_email = 'david.kowalk@gmail.com',
    url = 'https://github.com/davidkowalk/FunctionSynthesizer',

    license = "MIT",
    keywords = "math interpolation polynomial calculus",

    long_description = README(),
    long_description_content_type='text/markdown',

    classifiers=[
        "Development Status :: 4 - Beta",
        'Intended Audience :: Developers',
        "License :: OSI Approved :: MIT License",
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],

    package_dir = {'':'src'},

    python_requires = ">=3.6",
    install_requires=['numpy'],

    project_urls={
        'Bug Reports': 'https://github.com/davidkowalk/FunctionSynthesizer/issues',
        'Funding': 'https://paypal.me/davidkowalk',
        'Source': 'https://github.com/davidkowalk/FunctionSynthesizer/',
    }

)
