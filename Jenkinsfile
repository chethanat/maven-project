pipeline{
  agent any
  stages {
    stage('Merge') {
      steps{
        script{
          def branches = git branch: '', poll: false
          def isMerged = branches.contains('origin/feature')
          if (isMerged) {
            echo "Deploy to dev"
        }else{
            echo "No merge detected"
      }
    }
      }
    }
  }
}
