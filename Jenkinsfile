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
                bat 'set PATH=C:\\Python312\\Scripts;%PATH%'
                // bat 'C:\\Python312\\python.exe --version'
                // bat 'C:\\Python312\\python.exe -m pip list'


                //bat 'C:\\Users\\"All Users"\\AppData\\Local\\Microsoft\\WindowsApps\\python.exe -m venv venv'
                bat 'c:\\Python312\\python.exe -m venv venv'
                bat 'venv\\Scripts\\activate'

                bat 'C:\\Users\\"Lenovo T490"\\AppData\\Roaming\\npm\\electron-packager.cmd . SiliconLabs --platform=win32 --arch=x64 --out=dist --electronVersion=28.2.0 --overwrite'
            }
        }

        stage('Start Electron App') {
            steps {
                bat 'start dist/SiliconLabs-win32-x64/SiliconLabs.exe'
            }
        }

        stage('Start Robot Test') {
            steps {
                bat 'C:\\Python312\\Scripts\\pip.exe install robotframework'
                bat 'C:\\Python312\\Scripts\\pip.exe install pywinauto'
                bat 'C:\\Python312\\Scripts\\pip.exe install pyautogui'
                bat 'c:\\Python312\\python.exe -m robot Test.robot'
            }
        }
    }

    triggers {
        pollSCM('* * * * *')
    }
}


// pipeline {
//     agent any

//     stages {
//         stage('Checkout') {
//             steps {
//                 checkout scm
//             }
//         }

//         stage('Build Electron App') {
//             steps {
//                 bat 'npm install'

//                 bat 'C:\\Users\\"All Users"\\AppData\\Roaming\\npm\\electron-packager . SiliconLabs --platform=win32 --arch=x64 --out=dist --electronVersion=28.2.0'
//             }
//         }
//         stage('Start Electron App') {
//             steps {
//                 bat 'start dist/SiliconLabs-win32-x64/SiliconLabs.exe'
//             }
//         }
//         stage('Start Robot Test') {
//             steps {
//                 bat 'python -m pip install robotframework'
//                 bat 'python -m pip install pywinauto'
//                 bat 'python -m pip install pyautogui'

//                 bat 'python -m robot Test.robot'
//             }
//         }
//     }

//     triggers {
//         pollSCM('* * * * *')
//     }
// }
