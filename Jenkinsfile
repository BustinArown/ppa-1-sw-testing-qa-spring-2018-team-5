node {
	checkout scm
}
	
pipeline {
	agent any
	stages {
		stage('Buidling...') {
			steps {
			sh 'make'
			archiveArtifacts artifacts: '**/target/*.jar',
			fingerprint: true
			}
		stage('Testing...') {
			steps {
			echo 'Is it working?
			}	
		}
	}
}
