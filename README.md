# Indicator Registry


## Deployments
We currently have a simplified deployment process with limitted scalability using a fabric script (http://www.fabfile.org/). In the future we plan to to use Amazon Elastic Beanstalk (https://aws.amazon.com/es/elasticbeanstalk/) to handle deployment and scalability.

### Fabric script
The deployment script is stored on `fabfile` folder and was based on this project: https://github.com/ashokfernandez/Django-Fabric-AWS

#### Requirements:
 * Install the libraries of fabfile `pip install -r fabfile/requirements.txt`.
 * Private AWS key file to access the instances installed on your SSH folder `~/.ssh/indicatorregistry.pem` (check permissions of the file, 400 is expected)
 * Private deploy key on your ssh file `indicatorregistry_dply` and `indicatorregistry_dply.pub`
 * Passphrase of the deployment key

### Deployment commands:
A complete description can be found on `fabfile/django_fabric_aws.py`.
 * fab spawn instance
 * fab configure_instance
 * fab update_packages
 * fab deploy
 * fab reload_gunicorn
 * fab reload_nginx
 * fab reload_supervisor
 * fab manage:command="management command"


### Customizations
In some deployments we need to simplify how we serve the static files or/and the database.

#### Nginx
A posibility is to use nginx to serve the static folder of the project.
We can also use nginx to handle redirects from non www to www domains.

### Deployment steps
You can trigger a deploy to the instances listed on `fabfile/project_conf.py` variable `EC2_INSTANCES` by executing

```
fab deploy
```

this command will update the repository on the instances to the latest version of the branch selected on each one.
