import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()


setuptools.setup(
     name='bot_it',  
     version='0.1.1',
     scripts=['bot.py'] ,
     author="Bruno Peselli",
     author_email="brunopeselli@gmail.com",
     description="BOT IT is an easy-to-use automation framework build with Python",
     long_description=long_description,
   long_description_content_type="text/markdown",
     url="https://github.com/pzzzl/bot-it",
     packages=setuptools.find_packages(),
     classifiers=[
         "Programming Language :: Python :: 3",
         "License :: MIT License",
     ],
 )