pipeline{
  agent any

  triggers{
    pollSCM('* * * * *')
  }
  stages {
    stage('Merge') {
      when{
        changeset '1'
      }
      steps{
        script{
          checkout scm
          def isMerged = bat(script: 'git log --merges --oneline origin/dev..origin/feature', returnStatus: true)
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
