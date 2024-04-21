pipeline{
  agent any
  triggers{
    pollSCM('* * * * *')
  }
  stages {
    stage('check for new') {
      when{
        changeset '**'
      }
      steps{
        script{
          checkout scm
          def devCommit = bat(script: 'git rev-parse origin/dev', returnStdout: true).trim()
          def releaseCommit = bat(script: 'git rev-parse origin/release', returnStdout: true).trim()
          if (devCommit != releaseCommit) {
            echo "new commits found"
          }
          else{
            echo "No new commits"
      }
    }
      }
    }
  }
}
