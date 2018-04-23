node {
	stage('Checkout') 
	{
		//Get code from repo
		checkout scm
	}
	stage('Build') 
	{
		bat 'virtualenv env'
	}
	post 
	{
		success 
		{
			bat "echo 'Pipeline reached the finish line!'"
		}
		failure 
		{
			bat "echo 'Pipeline failed'"
		}
	}
}
