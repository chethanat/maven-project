pipeline{
  agent any
  stages {
    stage('Merge') {
      steps{
        script{
          def mergeCount = sh (script: 'git log --merges --oneline origin/dev..origin/feature')
          if (mergeCount == 0) {
            echo "No merge detected"
        }else{
            echo "Deploy to dev"
      }
    }
      }
    }
  }
}
