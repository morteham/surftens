from distutils.core import setup

setup(name='surftens',
            version='1.0.0',
            description='Surface tension ',
            author='Morten Hammer',
            author_email='morten.hammer@sintef.no',
            url='',
            packages=['surftens'],
            package_data={'surftens':['data/nist.json']}
           )

