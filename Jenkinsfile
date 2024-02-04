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
                //bat 'C:\\Users\\"All Users"\\AppData\\Local\\Microsoft\\WindowsApps\\python.exe -m venv venv'
                // bat 'c:\\Python312\\python.exe -m venv venv'
                // bat 'venv\\Scripts\\activate'

                bat 'C:\\Users\\"Lenovo T490"\\AppData\\Roaming\\npm\\electron-packager.cmd . SiliconLabs --platform=win32 --arch=x64 --out=dist --electronVersion=28.2.0 --overwrite'
            }
        }

        stage('Start Electron App') {
            steps {
                bat 'start dist/SiliconLabs-win32-x64/SiliconLabs.exe'
            }
        }

        stage('Start Robot Test') {
            // steps {
            //     // bat 'c:\\Users\\"All Users"\\Jenkins\\.jenkins\\workspace\\"SiliconLabs Build+Test"\\venv\\Scripts\\python.exe -m pip install robotframework'
            //     // bat 'c:\\Users\\"All Users"\\Jenkins\\.jenkins\\workspace\\"SiliconLabs Build+Test"\\venv\\Scripts\\python.exe -m pip install pywinauto'
            //     // bat 'c:\\Users\\"All Users"\\Jenkins\\.jenkins\\workspace\\"SiliconLabs Build+Test"\\venv\\Scripts\\python.exe -m pip install pyautogui'

            //     // bat 'c:\\Users\\"All Users"\\Jenkins\\.jenkins\\workspace\\"SiliconLabs Build+Test"\\venv\\Scripts\\python.exe -m robot Test.robot'
            //     // Full path to Python executable and Scripts directory
            //     def pythonExecutable = 'C:\\Python312\\python.exe'
            //     def pythonScripts = 'C:\\Python312\\Scripts'

            //     // Continue with your other commands
            //     bat "${pythonExecutable} -m pip install robotframework"
            //     bat "${pythonExecutable} -m pip install pywinauto"
            //     bat "${pythonExecutable} -m pip install pyautogui"

            // }
            steps {
                script {

                    // Full path to Python executable and Scripts directory
                    def pythonExecutable = 'C:\\Python312\\python.exe'
                    def pythonScripts = 'C:\\Python312\\Scripts'

                    // Continue with your other commands
                    bat "${pythonExecutable} -m pip install robotframework"
                    bat "${pythonExecutable} -m pip install pywinauto"
                    bat "${pythonExecutable} -m pip install pyautogui"

                    // Add the Python Scripts directory to the PATH for subsequent commands
                    bat "set PATH=${pythonScripts};%PATH%"

                    // Continue with your other commands
                    bat "${pythonExecutable} -m robot Test.robot"
                }
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
