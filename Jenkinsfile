pipeline{
  agent any

  triggers{
    pollSCM('H/1 * * * *')
  }
  stages {
    stage('Merge') {
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
