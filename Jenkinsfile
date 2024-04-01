pipeline{
  agent any
  stages {
    stage('Read YAML File') {
      steps{
        script{
          def yamlData = readYaml(file: 'test.yml')
          echo yamlData.input
          if (yamlData.input == true){
            mvn clean
          }
        }
      }
    }
  }
}
