pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build Electron App') {
            steps {
                sh 'npm install'

                sh 'electron-packager . SiliconLabs --platform=win32 --arch=x64 --out=dist --electronVersion=28.2.0'
            }
        }
    }

    triggers {
        pollSCM('* * * * *')
    }
}
