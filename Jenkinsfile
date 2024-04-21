pipeline{
  agent any

  stages {
    stage('Checkout'){
      steps{
        git branch: 'dev', url: 'https://github.com/chethanat/maven-project.git'
      }
    }
    stage('Merge') {
      environment {
        PATH_TO_BASH = 'C:\Program Files\Git\bin'
      steps{
        script{
          checkout scm
          def isMerged = bat(script: "\"${PATH_TO_BASH}\\git.exe\" log --merged --oneline origin/dev..origin/feature", returnStatus: true)
          if (isMerged == 0) {
            echo "Deploy to dev"
        }else{
            echo "No merge detected"
      }
    }
      }
    }
  }
}
