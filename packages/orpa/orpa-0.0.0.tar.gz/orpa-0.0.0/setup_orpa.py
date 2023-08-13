from setuptools import setup, find_packages
import os

setup(name='orpa',
      version="0.0.0",
      description='The powerful open source RPA platform for business (pyOpenRPA)',
      long_description='Prototype',
      long_description_content_type='text/markdown',
      classifiers=[
        'Development Status :: 5 - Production/Stable',
		'License :: Free For Educational Use',
		'License :: Free For Home Use',
		'License :: Free for non-commercial use',
        'Intended Audience :: Developers',
        'Environment :: Win32 (MS Windows)',
        'Environment :: X11 Applications',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.7',
		'Programming Language :: Python :: 3.8',
		'Programming Language :: Python :: 3.9',
		'Programming Language :: Python :: 3.10',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Software Development :: Testing',
        'Topic :: Software Development :: User Interfaces',
        'Topic :: Software Development :: Quality Assurance',
        'Topic :: Home Automation'
      ],
      keywords='ORPA pyOpenRPA OpenRPA RPA Robot Automation Robotization OpenSource',
      url='https://orpa.app/',
      author='Ivan Maslov',
      author_email='Ivan.Maslov@pyopenrpa.ru',
      license='Текст лицензии см. в файле по адресу: https://pyopenrpa.ru/license/oferta.pdf',
      packages=find_packages(),
      install_requires=[
          'pillow>=6.0.0',
		  'keyboard>=0.13.3',
          'pyscreeze==0.1.21',
		  'pyautogui<=0.9.52',
		  'psutil>=5.6.2',
		  'crypto>=1.4.1', 
		  'schedule>=1.1.0', 
		  'Jinja2>=2.2.11.2', 
		  'selenium==3.141.0',
		  'fastapi>=0.81.0',
		  'uvicorn>=0.18.3',
          'python-multipart>=0.0.6',
          'autodocsumm>=0.2.10',
          'screeninfo>=0.8.1',
          "pytesseract"
      ],
	  extras_require={
        ':sys_platform == "win32"': [
            'pywin32>=224', 'WMI>=1.4.9', 'pywinauto>=0.6.8', 'desktopmagic'
        ],
        ':"linux" in sys_platform': [
            'simplepam>=0.1.5', 'pyclip>=0.6.0'
        ]
	},
      include_package_data=True,
      #data_files = datafiles,
      #package_data = {"pyOpenRPA": datafiles},
      zip_safe=False)
