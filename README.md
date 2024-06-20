# Syyclops
# Ifc-based BIM application

## Overview:
This project uses the IfcOpenShell library to process Building Information Model (BIM) files in the IFC format. The application reads an IFC file, extracts relevant data about building elements, their properties, relationships and performs simple analysis (total wall area and number of elements), and saves the processed data to two separate JSON files. This project is containerized using Docker to ensure a consistent runtime environment.

## Prerequisites
- (Docker)(https://www.docker.com/get-started) installed on your machine.
- (Docker Compose)(https://docs.docker.com/compose/install/) installed on your machine.
  
## Instructions to clone the repo and run the app

1.	Clone the Repository:
    Clone this repository to your local machine.
    ```sh
    git clone https://github.com/NishchithAnanthaRamu/Syyclops-Application-Enhanced_GitHub_Actions.git
    ```
    
2. Change the directory to Syyclops-Application-Enhanced:
    ``` sh
    cd Syyclops-Application-Enhanced
    ```
    
3.	Updating the IFC file path in the script:

    Update the script to use the correct path to your IFC file if required

4.	Update the docker-compose.yml file:

   Update the paths of the 'elements_properties' and 'relationships' directories in the 'built' directives of the yml file.

5.	Build the Application with Docker-compose:
    ```sh
    docker-compose build
    ```

6. Run the Application with Docker-compose:
   ``` sh
   docker-compose up
   ```



