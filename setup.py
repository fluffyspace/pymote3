import os
import sys
from setuptools import setup, find_packages

# transfer profile_pymote3 for ipython into IPYTHONDIR
if 'install' in sys.argv or 'develop' in sys.argv:
    import shutil
    try:
        import IPython
        ipythondir = IPython.utils.path.get_ipython_dir()  # @UndefinedVariable
    except ImportError as AttributeError:  # @ReservedAssignment
        print("Pymote3 IPython configuration not installed. Install latest "
              "IPython and then copy the conf/ipython/profile_pymote3/"
              "ipython_config.py manually to IPython config dir.")
    else:
        profiledir = os.path.join(ipythondir, 'profile_pymote3')
        if not os.path.exists(ipythondir):
            os.makedirs(ipythondir)
        if not os.path.exists(profiledir):
            os.makedirs(profiledir)
        print(("copying ipython_config.py and ipython_notebook_config.py "
               "to "+profiledir))
        shutil.copy(os.path.join('pymote3', 'conf', 'ipython',
                                 'ipython_config.py'), profiledir)
        shutil.copy(os.path.join('pymote3', 'conf', 'ipython',
                                 'ipython_notebook_config.py'), profiledir)

sys.path.insert(0, 'pymote3')
import release  # @UnresolvedImport
sys.path.pop(0)

setup(
    name=release.name,
    version=release.version,
    url=release.url,
    author=release.authors['Arbula'][0],
    author_email=release.authors['Arbula'][1],
    description=release.description,
    keywords=release.keywords,
    download_url=release.download_url,
    license=release.license,
    platforms=release.platforms,
    classifiers=release.classifiers,
    packages=find_packages(),
    #package_data = {
    #    '': ['*.bat'],
    #},
    exclude_package_data={'': ['README.rst']},
    install_requires=[
        'networkx',
        'numpy',
        'scipy',
        'pypng',
        'ipython',
        'matplotlib',
        'PySide6',
    ],
    long_description=open(os.path.join(os.path.dirname(__file__),
                                       'README.rst')).read(),
    long_description_content_type='text/x-rst',
    entry_points={
        'pymote3.algorithms': [],
        'console_scripts': [
            'ipymote3 = pymote3.scripts.ipymote3:start_ipymote3',
        ],
        'gui_scripts': [
            'pymote3-simgui = pymote3.gui.simulationgui:main',
        ]
    },
    test_suite='nose.collector',
    tests_require=['nose'],

#    include_package_data=True,
#    zip_safe = False,
)
