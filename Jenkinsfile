pipeline {
	agent any 
	
		stages {
		    stage ("Building") {
				steps {
					bat "echo 'Buidling File....'"
				}
			}
			stage ("Testing") {
				steps {
					bat "echo 'Tests Running....'"
				}
			}
			}
		post {
			success {
				bat "echo 'Pipeline reached the finish line!'"
			}
			failure {
				bat "echo 'Pipeline failed'"
			}
		}
	}
