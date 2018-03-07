#CredSimple DevOps Challenge:

Set up a 3 tier application in AWS with FE, API, and Database. Use load balancers where would make sense in a Production environment. Set up a VPC how you see reasonable, capable of being peered with another VPC whose ip range is 10.0.0.0/16. 

Pretend that there is a docker orchestrator that will be placing containers in a cluster of nodes. You only need to create one such node, and manually create the containers there that this imaginary orchestrator would for the FE and API projects.

Look at devops/contacts-app-api/server/datasources.production.js to see the environment variables needed by the api.

##Details

* The FE is available in contacts-app, the API in contacts-app-api.
* Create a MySQL 5.7 database in RDS to use with the api. The sql dump is in the api project.
* Use the Ohio Region.
* Set the api to api.challenge.aws.credsimple.com.
* Set the fe to fe.challenge.aws.credsimple.com.
* Use appropriately small instances for a test.
* Create a new keypair and send back to us.
* Don’t worry about https.
