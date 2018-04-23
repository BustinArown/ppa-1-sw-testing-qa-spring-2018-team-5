pipeline {
	agent any
	
	stages {
		stage('Build') {
			steps {
				echo 'Building'
				scm checkout
				bat 'make'
			}
		}
		stage('Test') {
			steps {
				echo 'Testing'
			}
		}
	}
	
	post {
		success {
            		echo 'This will run only if successful'
        		}
       		failure {
            		echo 'This will run only if failed'
        		}
        	unstable {
            		echo 'This will run only if the run was marked as unstable'
		}
	}
}
				
