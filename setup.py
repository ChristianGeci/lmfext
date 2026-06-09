from setuptools import setup

setup(
    name='lmfext',
    version='0.1.0',    
    description='extensions for the lmfit python package',
    #url='https://github.com/ChristianGeci/fluorCalc',
    author='Christian Geci',
    author_email='christian.geci@maine.edu',
    license='MIT license',
    packages=['lmfext'],
    install_requires=[
                      'numpy',
                      'lmfit',
                      'pandas',
                      ],

    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Science/Research',
        #'License :: OSI Approved :: BSD License',  
        #'Operating System :: POSIX :: Linux',        
        #'Programming Language :: Python :: 2',
        #'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        #'Programming Language :: Python :: 3.4',
        #'Programming Language :: Python :: 3.5',
    ],
)
