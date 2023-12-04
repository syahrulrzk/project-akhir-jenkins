pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                script {
                    git branch: 'python-app', url: 'https://github.com/syahrulrzk/project-akhir-jenkins.git'
                }
            }
        }

        stage('Build') {
            steps {
                script {
                    sh 'python3 build_script.py'
                }
            }
        }

        stage('Test') {
            steps {
                script {
                    sh 'python3 test_script.py'
                }
            }
        }

        stage('Deploy') {
            steps {
                script {
                    // Panggil skrip deploy di sini
                    deployApp()
                    
                    // Menampilkan input untuk persetujuan manual
                    def userInput = input message: 'Apakah aplikasi sudah diuji dan siap untuk dijalankan selama 1 menit? (Klik proceed atau abort)', ok: 'Proceed', parameters: [choice(choices: ['Proceed', 'Abort'], description: 'Pilih Proceed untuk melanjutkan atau Abort untuk menghentikan', name: 'ApprovalDecision')]
                    
                    if (userInput == 'Abort') {
                        error 'Pipeline dihentikan oleh pengguna.'
                    }
                    
                    // Menjeda eksekusi pipeline selama 1 menit
                    sh 'echo "Running the application for 1 minute..."'
                    sh 'sleep 1m'
                    
                    // Mengakhiri aplikasi setelah 1 menit
                    sh 'bash stop_app_script.sh'
                }
            }
        }
        
        stage('Post-Deploy') {
            steps {
                script {
                    // Tambahkan langkah untuk mengakhiri aplikasi
                    sh 'echo "Stopping the application..."'
                    // Tambahkan perintah untuk memberhentikan aplikasi sesuai kebutuhan
                }
            }
        }
    }
}

def deployApp() {
    // Langkah-langkah deploy yang diperlukan
    sh 'echo "Deploying the application..."'
    // Tambahkan langkah-langkah deploy khusus Anda di sini
}

def sendNotification(message) {
    // Langkah-langkah notifikasi (contoh: kirim ke Slack)
    sh 'curl -X POST -H "Content-type: application/json" --data \'{"text":"${message}"}\' https://slack.com/api/chat.postMessage?token=YOUR_SLACK_TOKEN&channel=general'
}
