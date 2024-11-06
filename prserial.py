import serial

import time

ser = serial.Serial('USB',112)
# GitHub 리포지토리 연동 방법 설명

"""
GitHub 리포지토리를 연동하는 과정은 다음과 같습니다:

1. Git 설치:
   - 컴퓨터에 Git이 설치되어 있어야 합니다.
   - https://git-scm.com/downloads 에서 다운로드 가능합니다.

2. GitHub 계정 생성:
   - GitHub.com에서 계정을 만듭니다.

3. 로컬 프로젝트 초기화:
   - 터미널에서 프로젝트 폴더로 이동합니다.
   - 'git init' 명령어로 Git 저장소를 초기화합니다.

4. GitHub에 새 리포지토리 생성:
   - GitHub 웹사이트에서 새 리포지토리를 만듭니다.

5. 로컬 저장소와 GitHub 연결:
   - 'git remote add origin [GitHub 리포지토리 URL]' 명령어를 사용합니다.

6. 파일 추가 및 커밋:
   - 'git add .' 로 모든 파일을 스테이징합니다.
   - 'git commit -m "초기 커밋"' 으로 변경사항을 커밋합니다.

7. GitHub에 푸시:
   - 'git push -u origin master' 로 GitHub에 코드를 업로드합니다.

이 과정을 따라하면 로컬 프로젝트를 GitHub 리포지토리와 연동할 수 있습니다.
"""

# 주의: 이 설명은 코드로 직접 실행되지 않습니다. 
# 실제 연동을 위해서는 위 단계를 수동으로 따라해야 합니다.

