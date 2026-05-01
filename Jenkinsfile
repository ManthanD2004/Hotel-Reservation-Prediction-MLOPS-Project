pipeline{
    agent any

    stages{
        stage('Cloning Github repo to Jenkins'){
            steps{
                script{
                    echo 'Cloning Github repo to Jenkins........'
                    checkout scmGit(branches: [[name: '*/main']], extensions: [], userRemoteConfigs: [[credentialsId: 'Jenkins_Github_Token', url: 'https://github.com/ManthanD2004/Hotel-Reservation-Prediction-MLOPS-Project.git']])
                }
            }
        }
    }
}