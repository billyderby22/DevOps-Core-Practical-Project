# DevOps-Core-Practical-Project
##  Project brief - 
In this project we were tasked with creating an application consisting of four microservices that interact with each other to generate objects using some defined logic. The application needed to be produced and maintained using an automated CI/CD pipeline. The full tech stack can be seen below:

- Kanban board for project tracking
- Git for version control
- Jenkins as a CI server
- Ansible for configuration management
- GCP cloud platform
- Docker as a containerisation tool
- Docker swarm for container orchestration
- NGINX as a reverse proxy

## Project Planning - 
When planning this project I started with a risk assessment to identify the hazards associated with this project. See below:

![Risk Assessment](Project%202%20Screen%20shots/Screenshot%202022-03-16%20at%2014.51.14.png)

The user will not be submitting information to this app so the main focus of the risk assessment was operational risks. For each hazard a likelihood and impact level were given to help gauge the risks. Aslo control measures and responses where needed were implemented. 

## App Design - 
For this project I am going to make a random football player generator. The 4 services will communicate together to generate a random player for the user. According to the brief I am working on the concept of MVP (Minimum Viable Product) so that I will complete all requirements before adding additional functionality.  

Front-end (service 1): this is the service the user interacts with. This service sends requests to the other 3 services to generate a random football player and display it to the user. 

Player-api (service 2): this service receives a HTTP GET request from service 1 and responds with a player name from a list at random.

Team-api (service 3): this service receives a HTTP GET request from service 1 and responds with a random team from a tuple.

Position-api (service 4): this service receives a HTTP POST request from service 1 that provides it with a random team and player that was generated from service 2 & 3. It then uses this data and provides a position to the player scoring to their name. If the player and team are correct a statement is printed that shows the name, team and position. If the statement is incorrect it is read as invalid. 

As well as the main services a reverse proxy using NGINX was used. The NGINX service listens to port 80 on the host machine and performs a proxy pass that directs traffic from port 80 on the host to port 5000 on the front-end container. See the front-end in action bellow:

![Front-end](Project%202%20Screen%20shots/app%20design.png)

The front end displays generated players with every new request made to the page adding a new one. The generated players are stored in a SQL database, see entity diagram below-

![ED](Project%202%20Screen%20shots/ed.png)

The microservice architecture looks like this:

![Architecture](Project%202%20Screen%20shots/architecuture.png)

## CI/CD Pipeline
This project uses a full CI/CD pipeline to test, build, deploy and maintain the application. The main components of this pipeline are:

- Project tracking
- Version control
- Development environment
- CI server
- Deployment environment

Project Tracking was done using Jira. I created tasks and assigned them with story points and used MoSCoW prioritisation to sort them. Tasks started in the backlog then moved to complete as I worked through the sprint. See my Jira board bellow - 

![Jira](Project%202%20Screen%20shots/jira.png)

[Jira Board](https://qawilliamderby.atlassian.net/jira/software/projects/DEV/boards/5)

Ansible was used to configure the vms with what was needed to make the project work. Using a playbook with roles written for the individual vms allowed for set-up to be automated and much quicker. 

![Ansible](Project%202%20Screen%20shots/Ansible.png)

Git was used for version control, the repository was hosted on Github. A feature branch model was used to keep a stable version of the application available throughout development. See the feature branch model bellow - 

![Feature branch model](Project%202%20Screen%20shots/feature%20branch%20model.png)

The development environment was a Ubuntu virtual machine hosted on GCP that was accessed with vscode. 

Jenkins was used as a CI server. Using a github webhook Jenkins cloned down the repo and executed the pipeline script defined in the Jenkinsfile. The pipeline has 4 main stages: test, build/push, deploy and post build actions. The test stage executes a bash script that cycles through the directories of the 4 services and runs unit tests using pytest. The front-end and the other 3 APIs had unit tests written to test all areas of functionality. The test stage was successful showing the following results. 


Front-end cov -

![Front-end cov](Project%202%20Screen%20shots/Front-end%20cov.png)

Player-api cov -

![Player-api cov](Project%202%20Screen%20shots/Player-api%20cov.png)

Team-api cov -

![Team-api cov](Project%202%20Screen%20shots/team-api%20cov.png)

Position-api cov -

![position-api cov](Project%202%20Screen%20shots/Position-api%20cov.png)

If the tests are successful, the build/push stage uses docker-compose to build the images for the different services. It then logs into docker using the credentials configured on the Jenkins VM and then pushes the images to Dockerhub. 

Following the build and push stage comes the deploy stage that deploys the application. the docker-compose.yaml and the nginx.conf files are copied to the swarm manager node by secure copy (scp).  

The results of the pipeline are shown below - 

![Pipeline](Project%202%20Screen%20shots/Jenkins%20Build.png)

Successful stages appear green, unstable builds are shown by yellow stages and failures are indicated with red stages. If a stage fails later stages will be skipped and that will prevent failed versions from being deployed. 

The structure of the CI/CD pipeline is - 

![CI pipeline diagram](Project%202%20Screen%20shots/CI%20Pipeline.png)

## Known Issues

- Invalid players can show, ideally only valid players would
- Idealy 100% tests accross the board

## Future Improvements
In the future I would like to add a way so that only a few players are displayed on the home page, ideally the five newest. Then I would like to add a history tab that allows the user to scroll through all of the past players that were generated. 

