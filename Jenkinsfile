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
    stage('archieve') {
      input{
        message "want to archieve"
        ok "Yes"
      }
      steps{
        archiveArtifacts artifacts: "**/*.war"
      }
    }
    
  }
}
