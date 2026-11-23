
pipeline {
    agent any

    options {
        timestamps()
        disableConcurrentBuilds()
    }

    environment {
        IMAGE_REPO = "shopsphere-api"
    }

    stages {
        stage("Test") {
            steps {
                sh "python3 -m venv .venv"
                sh ".venv/bin/pip install -r requirements.txt"
                sh ".venv/bin/python -m pytest -v"
            }
        }

        stage("Build Image") {
            steps {
                script {
                    env.IMAGE_TAG = sh(
                        script: "git rev-parse --short=12 HEAD",
                        returnStdout: true
                    ).trim()
                }

                sh "docker build -t ${IMAGE_REPO}:${IMAGE_TAG} ."
            }
        }

        stage("Deploy") {
            steps {
                sh "APP_IMAGE=${IMAGE_REPO}:${IMAGE_TAG} docker compose -p shopsphere up -d --remove-orphans"
            }
        }

        stage("Verify") {
            steps {
                sh "docker compose -p shopsphere ps"
                sh "for i in 1 2 3 4 5 6 7 8 9 10; do curl -fsS http://127.0.0.1:8085/health && exit 0; sleep 3; done; exit 1"
            }
        }
    }

    post {
        success {
            echo "ShopSphere deployed and health check passed"
        }

        failure {
            sh "docker compose -p shopsphere logs --tail=80 || true"
        }
    }
}
