# MIT License

# Copyright (c) 2023 MohitLabs

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from setuptools import setup, find_packages

setup(
    #Project
    name="EmotionallyIntelligentUnit",
    version="0.1.0-alpha",

    #Sources
    packages=find_packages(),
    
    #Dependencies
    install_requires=["flatlib"],

    #Metadata
    description="Vedic Astrology based Artificial Emotional Intelligence",
    long_description="Emotionally Intelligent Unit is a vedic astrology based artificial sentiment synthesis library",
    url="https://github.com/mohitlabs/EmotionallyIntelligentUnit",
    keywords=["EmotionallyIntelligentUnit", "EIU", "Sentiment Synthesis", "Artificial Emotional Intelligence"],
    license="MIT",

    #Authoring
    author="MohitLabs",
    author_email="mohitsingh5.ms@gmail.com",

    classifiers=[
        "Development Status :: 1 - Alpha",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "Programming Languages :: Python :: 3",
        "Operating System :: OS Independent",
    ]
)
