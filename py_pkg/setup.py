from setuptools import find_packages, setup

package_name = 'py_pkg'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='utk',
    maintainer_email='kutkarsh706@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            "num_publisher = py_pkg.num_publisher:main",
            "num_subscriber = py_pkg.num_subscriber:main",
            "move_turtle = py_pkg.move_turtle:main",
            "reset_turtle = py_pkg.reset_turtle:main",
            "task = py_pkg.task:main"
        ],
    },
)
