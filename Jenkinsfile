pipeline {
	agent any
	stages  {
		stage('Building') {
		steps {
			checkout scm
			bat 'make'
			}
		
		}
		stage('Testing') {
			steps {
				echo 'Working'
			}
		}
	post {
		success 
		{
            		echo 'This will run only if successful'
        	}
        	failure 
		{
            		echo 'This will run only if failed'
       		}
	}
	}
}

