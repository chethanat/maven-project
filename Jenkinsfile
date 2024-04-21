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
        PATH_TO_BASH = tool 'C:\Program Files\Git\bin'
      steps{
        script{
          sh 'git fetch origin'
          def mergeInfo = sh(script: "${PATH_TO_BASH} -c 'git log --merges --oneline origin/dev..origin/feature'", returnStatus: true)
          if (mergeInfo == 0) {
            echo "Deploy to dev"
        }else{
            echo "No merge detected"
      }
    }
      }
    }
  }
}
