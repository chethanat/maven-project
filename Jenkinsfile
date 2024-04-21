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
      environment {
        PATH_TO_BASH = 'C:\\Program Files\\Git\\bin'
      }
      steps{
        script{
          checkout scm
          def isMerged = bat(script: "\"${PATH_TO_BASH}\\git.exe\" log --merges --oneline origin/dev..origin/feature", returnStatus: true)
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
