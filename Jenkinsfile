pipeline {
    agent any
    post {
        failure {
            updateGitlabCommitStatus name: 'build', state: 'failed'
        }
        success {
            updateGitlabCommitStatus name: 'build', state: 'success'
        }
    }
    options {
        gitLabConnection('gitlab-capstone')
    }
    triggers {
        GenericTrigger(
            genericVariables: [
                [key: 'ref', value: '$.ref']
            ],
            
            causeString: 'Triggered on $ref',
            
            token: 'abc123',

            printContributedVariables: true,
            printPostContent: true,

            silentResponse: false,

            regexpFilterText: '$ref',
            regexpFilterExpression: 'refs/heads/' + BRANCH_NAME
        )
    }
    stages {
        stage("build") {
            steps {
                checkout scm
                script {
                    docker.withTool('docker') {
                        docker.withRegistry('https://registry.capstone.com', 'gitlab-root-credential') {
                            def customImage = docker.build("registry.capstone.com/capstone/testproject:${env.BUILD_ID}", ".")
                            customImage.push()
                        }
                    }
                }
            }
        }
        stage('deploy') {
            steps {
                script {
                    sh """helm upgrade --install testapp charts/ --namespace app --set image.tag=${env.BUILD_ID}"""
                }
            }
        }
    }
}
