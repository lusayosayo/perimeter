Perimeter - Infrastructure Management Tool
==========================================

Perimeter is a tool for managing multiple computers. You can use it to:

    + Manage multiple SSH clients.
    + Manage multiple Remote Desktop and VNC credentials.
    + Track IP address configurations, and service availability across an organization.

## INSTALLATION:
  + Windows: https://www.fpoint.tech/products/downloads/perimeter.exe
  + Ubuntu: https://www.fpoint.tech/products/downloads/perimeter.deb
  + Source code: https://github.com/neet-lord/perimeter.git

## USER DOCUMENTATION:

You can find the documentation at:
  + https://github.com/neet-lord/perimeter/blob/master/docs/index.html

## FOR DEVELOPERS:
To get an instance of perimeter up and running on your machine
for development.

  + Download the repository:
        
        git clone https://github.com/neet-lord/perimeter.git

  + Enter the directory:

        cd perimeter

  + Create a virtual environment:
  
        python3 -m pip venv venv

  + Activate the virtual environment:
  
        source venv/bin/activate

  + Install requirements:

        python3 -m pip install -r requirements.txt

  + Create a database:
    + The default database engine is mysql.
    + The default configuration is:
      + Database name: perimeter
      + User: perimeter
      + Password: perimeter
      + Host: localhost
    
    + You can change the database config app/config/settings.py

  + For the following steps, make sure you are in the 'app' directory:
    + Run migrations:

          python3 manage.py migrate

    + Load sample data (Optional but recommended)

          python3 load_data.py
    
    + Run application:
    
          python3 manage.py runserver

  + Navigate to your browser and run: http://localhost:8000.

