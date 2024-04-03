pipeline{
  agent any
  stages {
    stage('Build') {
      steps{
        script{
          bat "mvn clean"
        }
      }
    }
     stage('Test') {
      steps{
        script{
          bat "mvn package"
        }
      }
    }
    
  }
}
