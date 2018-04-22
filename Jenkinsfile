pipeline {
	agent any
	
	stages {
		stage ('Build') {
		
			steps {
				withMaven(maven : 'maven_3_5_3') {
					sh 'mvn clean compile'
				}
			}
		}
		
		stage ('Deploy') {
		
			steps {
				withMaven(maven : 'maven_3_5_3') {
					sh 'mvn deploy'
				}
			}
		}
	}	
}
