from setuptools import setup, find_packages

VERSION = '0.0.3' 
DESCRIPTION = 'Forecaster that combines the strengths of Prophet, SARIMA, and Holt-Winters.'
LONG_DESCRIPTION = "The package employs a combination of time series models: Exponential Smoothing - Holt-Winters, SARIMA, and Prophet. Required installations to run the package: Stats models, Prophet."

setup(
        name="blaze-forecaster", 
        version=VERSION,
        author="Ysabel Chen",
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        packages=find_packages(),
        
        keywords=['python', 'forecaster'],
        classifiers= [
            "Programming Language :: Python :: 3",
            "Operating System :: MacOS :: MacOS X",
            "Operating System :: Microsoft :: Windows",
        ]
)