import jovian

jovian.commit(project='jovian-v2-script-test2', 
              message='Testing message from script', 
              privacy='secret', 
              environment='pip',
              git_message='a commit from jovian')

