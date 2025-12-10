from setuptools import setup

setup(
    name='wigle-heatmap',
    version='0.0.1',
    description='Generate WiFi heatmaps from wiglecsv files',
    author='alex404sl',
    author_email='achen@stealthlabs.io',
    py_modules=['wigle_heatmap'],
    install_requires=[
        'folium>=0.14.0',
        'pandas>=1.5.0',
    ],
    python_requires='>=3.10',
    entry_points={
        'console_scripts': [
            'wigle-heatmap=wigle_heatmap:main',
        ],
    }
)