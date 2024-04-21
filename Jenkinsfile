pipeline{
  agent any

  stages {
    stage('Checkout'){
      steps{
        git branch: 'dev', url: 'https://github.com/chethanat/maven-project.git'
      }
    }
    stage('Merge') {
      steps{
        script{
          sh 'git fetch origin'
          def mergeInfo = sh(script: 'git log --merges --oneline origin/dev..origin/feature', returnStatus: true)
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
