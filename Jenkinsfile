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
                bat 'npm install'

                bat 'electron-packager . SiliconLabs --platform=win32 --arch=x64 --out=dist --electronVersion=28.2.0'
            }
        }
        stage('Start Electron App') {
            steps {
                bat 'start dist/SiliconLabs-win32-x64/SiliconLabs.exe'
            }
        }
        stage('Start Robot Test') {
            steps {
                bat 'robot Test.robot'
            }
        }
    }

    triggers {
        pollSCM('* * * * *')
    }
}
