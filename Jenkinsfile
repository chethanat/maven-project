pipeline{
  agent any
  stages {
    stage('Read YAML File') {
      steps{
        script{
          def yamlData = readYaml(file: '${workspaceDir}/${test.yml}')
          echo yamlData.input
          def currentDir = pwd()
          echo "Directory: ${currentDir}"
          if (yamlData.input == true){
            mvn clean
          }
        }
      }
    }
  }
}
