pipeline{
  agent any
  triggers{
    pollSCM('* * * * *')
  }
  stages {
    stage('Merge') {
      when{
        changeset '**'
      }
      steps{
        script{
          checkout scm
          def isMerged = bat(script: 'git log --merges --oneline -- first-parent origin/dev..origin/feature', returnStdout: true).trim().split('\n')
          if (mergeCommits.size() > 0) {
            echo "Deploy to dev"
          }
          else{
            echo "No merge detected"
      }
    }
      }
    }
  }
}
