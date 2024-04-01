pipeline{
  agent any
  stages {
    stage('Read YAML File') {
      steps{
        script{
          def yamlData = readYaml(file: 'test.yml')
          if (yamlData.input == true){
            mvn clean
          }
        }
      }
    }
  }
}
