from setuptools import find_packages, setup

package_name = 'todo_reminder'

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
    maintainer='Kazuki Fujita',
    maintainer_email='kazu.maro.126624@icloud.com',
    description='ROS 2 package to send reminders via topics',
    license='BSD-3-Clause',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
            'todo_reminder = todo_reminder.todo_reminder:main',
        ],
    },
)
