from Cython.Build import cythonize
from setuptools import Extension


def build(setup_kwargs):
    extensions = [
        Extension(
            "second_python_package.harmonic_mean",
            ["second_python_package/harmonic_mean.pyx"],
        )
    ]

    setup_kwargs.update(
        {
            "ext_modules": cythonize(extensions),
        }
    )
