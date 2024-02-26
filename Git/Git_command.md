# 1. 터미널(terminal)에서의 조작
## 터미널이란?
    개인이 사용하는 로컬 시스템(PC)에서 디렉토리및 파일을 탐색, 추가, 수정, 이동, 실행등의 명령을 내릴 수 있는 CLI(Command Line Interface)을 말한다.
    일반적인 GUI(Graphic User Interface)와는 다르게 다루기 어렵지만 할 수 있는 것들이 더 많다.
    macOS나 Linux기반의 OS에서는 기본적으로 갖고있는 체계이지만 Windows는 독자규격이 따로 존재하므로 git bash라는 번역 프로그램을 따로 실행하여야 한다.
<br>

## 디렉토리(directory)란?
    일상생활에서 흔히 사용하는 용어 '폴더(Folder)'의 원래 이름이다.
    개발자로서 앞으로는 폴더보다는 디렉토리라는 용어를 사용하기로 한다.
<br>

## terminal의 명령어
### 주요 지칭어
---
현재 있는 디렉토리
```
.
```
<br>

현재보다 상위의 디렉토리
```
..
```
<br>

가장 기본이 되는 홈 디렉토리
```
~
```
<br>

로컬내 최상위 디렉토리
```
/
```
<br>

현재 디랙토리내 모든 내용을 지칭(asterisk)
```
*
``` 
<br>

### 주요 명령어
---
현재 디랙토리 내 모든 내용 출력(list)
```
$ ls
``` 
<br>


현재 디렉토리 내 숨겨진 내용까지 모두 출력(list all)
```
$ ls -a
``` 
<br>

해당 디렉토리로 이동(change directory)
```
$ cd {디렉토리명}
```
<br>

디렉토리 생성(make directory)
```
$ mkdir {디렉토리명}
```
<br>
 
파일 생성
```
$ touch {파일명}
```
<br>

파일 실행
```
$ open {파일명}
```
<br>


파일 삭제(remove) 
* -r : 디렉토리또한 삭제 가능(recursive)
* -f : 확실하게 삭제(force)
```
$ rm {파일명}
$ rm -rf {파일명}
```
<br>

파일수정을 터미널 내에서 실행
```
$ vim {파일명}
```
<br>


## vim 내 조작법

내용 입력으로 이동
```
i
```
<br>

명령어 입력으로 이동
```
Esc
```
<br>

명령어 창에서의 조작
|저장(write)|종료(quite)|저장후 종료|저장하지 않더라도 강제종료|
|:-:|:-:|:-:|:-:|
|`:w`|`:q`|`:wq`|`:q!`|
<br><br>

# 2. git의 조작

## git의 구성요소
    git의 구성요소로는 3개의 부분이 있다.
    WorkingTree(WT) / Staging(Stg) / Commit(Cmt)
    WT에는 디렉토리 내에서 일어나는 모든 변경사항에 관련된 정보를 추적한다.
    Stg는 WT에서 일어난 이러한 변경을 잠시 올려두는 단계이다.
    Cmt는 Stg에 올라온 사항을 하나의 기록으로 영구적으로 저장한다. 이를 스냅샷(Snap Shot)이라고 표현한다.
<br>

## git의 로컬 조작
해당 디렉토리를 git depository로 설정(initialize)
```
$ git init
```
<br>

파일 스테이징(Staging)
```
$ git add {파일명}
```
<br>

현재 스테이징 된 파일들 또는 트래킹 되지 않은 파일들의 목록을 출력
```
$ git status
```
<br>

현재 스테이징 된 파일들을 모두 해제
```
$ git reset
```
<br>
  
현재 스테이징 된 파일들을 커밋(Commit)
```
$ git commit
```
* 위의 경우에는 커밋시 설명문을 지정하지 않아서 텍스트 입력창으로 넘어가게 된다.  
* 이를 원치 않으면 커밋과 동시에 설명문을 지정하면 된다.
```
$ git commit -m "{설명문}"
```
<br>
 
지금까지 커밋해온 내역을 확인
* 뒤에 `--online`을 추가하여 짧게 한 줄씩 내역을 출력한다
```
$ git log
$ git log --oneline
```
<br>

커밋할 자신의 개인정보를 설정
```
$ git config --global user.email="{이메일}"
$ git config --global user.name="{이름 입력}"
```
<br>

직전 커밋의 내용을 수정
```
$ git commit --amend
```
<br>

해당 커밋 주소나 브랜치로 이동
```
$ git checkout {커밋 주소 또는 브랜치명}
```
<br>

브랜치 생성(branch)
* `-c {브랜치명}` 없을 시 브랜치 목록 출력
```
$ git branch {브랜치명}
$ git branch -c {브랜치명}
```
<br>
  
브랜치 삭제 
* -d : 일반 삭제
```
$ git branch -d {브랜치명}
```
<br>

브랜치 생성 후 바로 이동
```
$ git checkout -b {브랜치명}
```
<br>

해당 브랜치를 현재 브랜치에 합병함
```
$ git merge {브랜치명}
```
### 주의!
    merge을 실행할 경우 합병하는 두 브랜치가 서로 다른 커밋 로그를 각각 가지고 있는 경우 충돌이 발생할 수 밖에 없다. 이 경우에는 합병을 취소하는 것이 바람직하다.
```
$ git merge --abort
```
<br>

## github와 연동하여 조작
현재 원격으로 연결된 링크 확인
```
$ git remote -v
```
<br>

github의 repository와 연결
```
# 현재 나의 브랜치명을 main으로 바꿈
$ git branch -M main

# 링크를 원격 조작리스트에 추가
$ git remote add origin {연결할 링크}

# 나의 브랜치를 온라인에 업로드
$ git push -u origin main
```
<br>

github에 파일 저장
```
$ git push {브랜치명}
```
<br>

github의 파일을 받아옴
```
$ git pull origin {브랜치명}
```
<br>

github에서 처음 repository를 받아옴
* 오픈된 것은 복사가 가능하지만 원격 수정은 되지 않는다
* 그러므로 일반적으로는 먼저 clone으로 저장소를 가져온 후에 pull로 업데이트 하게 된다
```
$ git clone {저장소 링크}
```
<br>

### .gitignore 파일
* git에 업로드하지 않을 파일, 디렉토리를 지정할 수 있다
* 파이썬의 정규표현식과 비슷하게 표현한다
```
# .gitignore 파일 내부에 작성
file.txt # 정확한 파일/경로명 입력
file* # 시작
*le* # 중간
*.txt # 끝
dir/ # 폴더명
```