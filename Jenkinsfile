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
                // Install dependencies
                bat 'npm install'

                // Run electron-packager command
                bat 'electron-packager . SiliconLabs --platform=win32 --arch=x64 --out=dist --electronVersion=28.2.0'

                // Start Electron app
                bat 'start dist/SiliconLabs-win32-x64/SiliconLabs.exe'
            }
        }
    }

    triggers {
        pollSCM('* * * * *')
    }
}
