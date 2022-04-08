TTC - My version of the deliverable for QA's DevOps Practical Project

Project Brief:

The brief of this project was to produce an application consisting of four individual microservices which generate random objects and combine them between each other to 'make a new object' for the user.

Below is the list of technology I have used throughout this project:

Kanban Board for project tracking (linked here: https://abi-hunt.atlassian.net/jira/software/projects/TTCREAT/boards/3/roadmap?selectedIssue=TTCREAT-24&timeline=WEEKS) Git, following the correct methods for the feature-branch model. Jenkins was used as a CI server Ansible for configuration management GCP to manage multiple VM's/containers Docker as a containerisation tool Docker Swarm for container orchestration NGINX as a reverse Proxy

Generally I started with my kanban board. I am usually very bad at making sure this is kept up to date and this was no exception. I have since found that it is possible to connect git commits with tasks using Jira, and I feel that this will massively help me in the future so that I keep an accurate log of the work I have accomplished.

Following this I created a risk assessment matrix to cover possible events or situations which might hinder my project. This can be seen along with any other referenced images in the following google docs file: https://docs.google.com/document/d/1cGjINqd6rQxPMlw62Acp91umNKZbf5iO7FuKYbdjfSg/edit?usp=sharing

Usually the risks on these assessments are fairly far-fetched and unlikely, however this project I came down quite ill a few days before the hand in date. This severely hindered my progress and it will be outlined as a far more likely risk in future projects.

App Design:

In response to the brief I decided to create a super-hero themed Top Trumps card generator with my four services laid out like so: Front-end (service 1): this service essentially allows any users to interact with the api's.

Super Hero stats (service 2): This service receives get requests from service 1 and responds randomly generated stats such as their strength or courage.

Name creator (service 3) This was supposedly going to generate random super hero names.

Service 4 would have combined the style of the super hero name and the stats given to create a suitable nickname (Such as Fast feet Flash for having a high speed stat)

unfortunately I could not bring these services fully to life and only managed to get a very basic functionality out of two services where they combined their information (such as a catchphrase; Hulk Smash.)

In Diagram 2 I have shown that i confirmed 2 of my api's were communicating during early doors of development, and roughly around the same time I used post-mate to confirm that my initial get and post requests were working, which they were! (Evidence in Diagram 5).

CI Pipeline: Again, unfortunately I was unable to maintain a fully functioning ci Pipeline. My tracking was not up to parr on kanban, and unfortunately I faced an error with Github as it kept deleting my public ssh keys from the GCP vm's I was using. This meant working with Jenkins to set up a pipeline or even keeping my development in a suitable development environment.

The workaround I found for this was simply to have two version of my program, one which was used to demonstrate my feature branch model and the other I used to test what little CI I could get done.

Looking at diagram 3 you can see the code I used as a workaround to try and get as much CI done as possible, however it only worked for so long. This massively hindered my ability to complete the project work.

Also, although I did not fully get to use them I had the VM's on GCP ready and configured to be used correctly for their assigned services, as is shown in diagram 6. I also had a few docker files and docker-compose.yaml files ready for containerisation once ansible is completed

However, due to the fact I basically had to manage two seperate directories within vs code to check if things worked, it did mean that I was successful in creating a perfect feature branch model of my work. (diagram 4)

The drawbacks of my project is that due to unforseen circumstanced I was unable to complete the follow:

Complete testing 
Complete setting up and testing CI Pipeline 
Complete setting up Ansible Roles

Although it is hard for me to say, I do feel like I was not very far off completing these tasks despite the unforseen circumstances that slowed me down. However having said that, I am still disappointed that I was unable to complete all aspects of the minimum viable product, and I can only hope that I will be given another chance by QA to continue.
