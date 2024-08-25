1.In this project I have created a Task Manager Application using Fastapi and python and MySQL as a Database.(In classes and functions format totally)
2.Firstly in this folder there is a requirements.txt file download that first in the python environment and I prefer and suggest PyCharm for creating and using  Python application and for python programming.
3.pip install -r requirements.txt -- Use this command to download all the require packages and models.
4.After installing the requirements.txt I have create one Registration name python package and in that package again create a com name python package.(To follow the SOLID principles and Architecture of the development).
5.In this project i have followed the SOLID principles and design pattern as per the requirements and the structure of the project i just like the that.
6. Then in com python package there are 6 more python packages with there own specific work and functionality.
ie. a.const,
    b.controller,
    c.daos,
    d.dbas,
    e.services.
So in const there are all the const values like hostname username and password for database connection.
Controller layer is the layer which are visible to the end user and daos and service layer are not visible 
Now,dbas layer:

In this layer i have made a connection and this connection we use in all the daos layer for all the CRUD operations.
FOR connection with database(MYSQL) i have used sqlalchemy.
In sqlalchemy we have to create a engine and after that we have to start a session for the engine and we use specific syntax for this 
ie .f"mysql+pymysql://{username}:{password}@{hostname}:{port}/{database}"after making the connection with the database we use this connection in all the files bu giving the reference to this function and class.


* dbas layer --- This is the most important layer and all the logic are written in it. All the queries and there logic are written in this and this only layer have the authority to direct connect with the database.

* service layer --- This layer consist of all the services given to the user (add_user,task,seraching).This layer connect with the dbas layer.
* Controller layer ---This layer consist of the controller means programming related to fastapi only not any logic. This layer is visible to user and we use only this layer to open swaager.

In Controller layer there are different python files to run a file we use "uvicorn Registration.com.controller.TaskController:app --reload" (this command is for taskcontroller) change the name according to the name of the file.
Uvicorn is an ASGI web server implementation for Python. 
In this project i have all the things required if there are some things missing it can be created and updated.
Open this folder in PyCharm and create python environment and download all the packages in requirement.txt file and run controller layer by using the above command.s



