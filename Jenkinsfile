def latestImageTag
def buildImageTag
def gitHashImageTag
def branchLatestTag

pipeline {
    agent { label 'linux' }

    environment {
        DOCKER_REGISTRY = 'https://docker.psiphon.io'
        DOCKER_IMAGE_NAME = 'docker.psiphon.io/telegram_bot/telegram_bot'
    }

    stages {
        stage('Build main docker image') {
            when {
                branch 'master'
            }

            steps {
                script {
                    latestImageTag = env.DOCKER_IMAGE_NAME + ':latest'
                    // Will be of the format <image>:jenkins-<name of job>-<build-number>
                    // Example <image>:jenkins-telegram-bot-master-10
                    buildImageTag = env.DOCKER_IMAGE_NAME + ':' + env.BUILD_TAG.replaceAll(" ", "-")
                    gitHashImageTag = env.DOCKER_IMAGE_NAME + ':' + env.GIT_COMMIT
                }

                withDockerRegistry([credentialsId: 'psiphon-docker-io-creds', url:  env.DOCKER_REGISTRY]) {
                    sh label: 'Pull latest image to populate build cache',
                       script: 'docker pull ' + latestImageTag,
                       returnStatus: true // okay if this fails

                    sh label: 'Build docker image',
                       script: """
                       docker build \
                       --tag ${latestImageTag} \
                       --tag ${buildImageTag} \
                       --tag ${gitHashImageTag} \
                       .
                       """

                    sh label: 'Push latest tag',
                       script: 'docker push ' + latestImageTag

                    sh label: 'Push git hash tag',
                       script: 'docker push ' + gitHashImageTag

                    sh label: 'Push build image tag',
                       script: 'docker push ' + buildImageTag
                }
            }
        }
        stage('Build PR docker image') {
            when {
                changeRequest()
            }

            steps {
                script {
                    latestImageTag = env.DOCKER_IMAGE_NAME + ':latest'
                    // Will be of the format <image>:jenkins-<name of job>-<build-number>
                    // Example <image>:jenkins-telegram-bot-PR-5-10
                    buildImageTag = env.DOCKER_IMAGE_NAME + ':' + env.BUILD_TAG.replaceAll(" ", "-")
                    gitHashImageTag = env.DOCKER_IMAGE_NAME + ':' + env.GIT_COMMIT
                    branchLatestTag = env.DOCKER_IMAGE_NAME + ":" + env.BRANCH_NAME + '-latest'
                }

                withDockerRegistry([credentialsId: 'psiphon-docker-io-creds', url:  env.DOCKER_REGISTRY]) {
                    script {
                        try {
                            sh label: 'Pull existing branch image to populate build cache',
                               script: 'docker pull ' + branchLatestTag
                        } catch (exc) {
                            echo 'Could not pull existing branch image, trying latest main build'
                            try {
                                sh label: 'Pull latest image to populate build cache',
                                   script: 'docker pull ' + latestImageTag
                            } catch (inner_exc) {
                                echo 'No latest image found'
                            }
                        }
                    }

                    sh label: 'Build docker image',
                       script: """
                       docker build \
                       --tag ${branchLatestTag} \
                       --tag ${buildImageTag} \
                       --tag ${gitHashImageTag} \
                       .
                       """

                    sh label: 'Push PR latest tag',
                       script: 'docker push ' + branchLatestTag

                    sh label: 'Push git hash tag',
                       script: 'docker push ' + gitHashImageTag

                    sh label: 'Push build image tag',
                       script: 'docker push ' + buildImageTag
                }
            }
        }
    }

    post {
        failure {
            script {
                changes = getChangeList()
            }
            slackSend message:"${env.JOB_NAME} - Build #${env.BUILD_NUMBER} failed (<${env.BUILD_URL}|Open>)\nChanges:\n${changes}",
                      color: "danger"
        }
    }
}

String getChangeList() {
    if (currentBuild.changeSets.size() == 0) {
        return "No changes"
    }

    def changeList = ""
    for (changeSet in currentBuild.changeSets) {
        for (entry in changeSet.items) {
            changeList += "- ${entry.msg} [${entry.authorName}]\n"
        }
    }

    return changeList
}
