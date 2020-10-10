![](https://ww.namu.la/s/0f836325137567259d1deedc2f134012282f926334957c5d30823a2a2ffa181984c7389e09591cdcc4c293ce2c86ea8bcf911c64604237a1f7c5468448b66b2b5bb880c7048422330809a911ec85a410f4c0d6924aec175061516cf59fd8377b)



### 1. 게임의 소개

​	1)copy할 게임 : 스트라이커즈 1945

​		-사이쿄에서 만든 종스크롤 슈팅게임이다.

​		-플레이어는 6가지 특색 있는 기체 중 하나를 선택해 플레이할 수 있다.

​		-보스를 한번 처치하면 다른 형태로 변신하는 특징이 있다.

​	2)게임의 목적, 방법 간단한 설명

​		-플레이어는 적들의 총알을 피하며 적들을 처치한다.

​		-플레이어의 공격 수단은 주무기, 보조무기, 폭탄이다.

​		-적을 처치하면 점수아이템과 파워업 아이템이 생성된다.

​		-스테이지 별로 보스가 존재하며 보스를 처치하면 다음 스테이지로 넘어갈 수 있다.



### 2.게임 컨셉

​		-게임 진행 방식

​				(1) 적의 총알이 플레이어 캐릭터의 충돌 범위에 닿으면 파괴되고 라이프가 1 감소한다.

​					파괴 후 부활 시 3초의 무적 시간이 있다.

​					남은 라이프가 0일 때 파괴되면 컨티뉴 화면으로 넘어간다.

​				(2)플레이어의 공격은 5단계로 구분된다. 게임 진행 시 등장하는 파워업 아이템을 먹으면 단계가 올라간					다.

​					공격 단계가 올라가면 발사하는 총알과 보조무기의 갯수가 늘어난다.

​					5단계에서 파워 업 아이템을 먹으면 공격 단계는 변하지 않고 점수로 환산 된다.

​				(3)적은 공중의 적과 지상의 적으로 구분 된다.

​					지상의 적과는 충돌 처리를 하지 않는다.

​					공중의 적과 충돌 시 플레이어의 공격 단계가 한 단계 줄어든다.

​				(4)플레이어의 총알이 적의 피격 범위에 닿으면 적의 체력이 줄어든다.

​					적의 체력이 0이 되면 파괴된다.

​				(5)폭탄 사용 시 화면의 적의 총알 객체가 모두 사라진다.



​			-게임 조작키 

​				(1)상하좌우 방향키로 캐릭터의 위치를 조작한다.

​				(2) a키를 눌러 총알을 발사한다. 오래 누르고 있으면 차지샷이 나간다.

​				(3) x 키를 누르고 있으면 연속으로 총알을 발사한다. 게임 스테이트가 아닐 시 선택키이다.

​				(4) z키를 눌러 폭탄을 사용한다.

​				(5)esc키를 눌러 일시정지 스테이트로 진입한다.



### 3. GameState(Scene)의 수 및 각각의 이름

​	8가지의 스테이트로 이루어졌다.	

​		-로고

​		-타이틀

​		-메뉴

​		-캐릭터 선택

​		-게임

​		-일시정지

​		-컨티뉴

​		-점수판

### 4. 각 GameState 별 항목

#### 		1)로고

​			-로고를 띄운다. 일정 시간 후에 자동으로 타이틀로 넘어간다.



#### 		2)타이틀

​			-게임의 타이틀을 띄운다. x키를 눌러 메뉴로 진입할 수 있다.



#### 		3)메뉴

​			-캐릭터 선택 스테이트와 점수판 스테이트, 게임 종료를 선택할 수 있는 스테이트이다.

​			-좌우 방향키로 항목을 고르고 x키를 눌러 해당 스테이트로 이동할 수 있다.





#### 		4)캐릭터 선택

​					 			

​			-캐릭터를 선택하는 스테이트이다.

​			-좌우 방향키로 캐릭터를 고르고 x키를 눌러 게임 스테이트로 진입한다.

​			-z키를 누르면 메뉴로 돌아간다.

​			-화면에 표시할 객체들의 목록 

​				(1)6종 캐릭터의 이미지 객체



#### 		5)게임스테이트

<img src="https://upload.wikimedia.org/wikipedia/en/5/55/ARC_Strikers_1945_%28Striker_1945%29.png?1602260571254" style="zoom:150%;" />

​			-게임을 진행하는 스테이트이다.

​			-화면에 표시할 객체들의 목록

​				(1)플레이어 캐릭터

​				(2)적 캐릭터

​				(4)플레이어 보조무기

​				(5)플레이어 총알(주무기, 보조무기 총알)

​				(6)적 총알

​				(7)점수 아이템

​				(8)파워 업, 폭탄 아이템

​				(9)상태창(폭탄 소지 갯수, 남은 라이프, 획득점수)

​				(10)배경 이미지

#### 		6)일시 정지

​			-게임 도중 esc를 눌러 진입하는 스테이트이다.

​			-메뉴로 돌아가기, 게임 재개 항목을 선택할 수 있다.

​			-상하 방향키로 항목을 고르고 x키를 눌러 실행한다.

​			-메뉴로 돌아가기를 선택하면 메뉴 스테이트로 진입한다.

​			-게임 재개를 선택하면 일시 정지 되어었던 게임 스테이트로 되돌아간다.

​		

#### 		7)컨티뉴

​			-게임 스테이트에서 라이프가 잔여 라이프가 0이 되면 집입하는 스테이트이다.

​			-게임 오버 후 x를 눌러 점수판 스테이트로 진입한다.



#### 		8)점수판

​			-자신이 기록한 점수가 높은 순서대로 10개 까지 저장되어 있다.

​			-최고점수를 기록하면 x키를 눌러 알파벳을 기입할 수 있다.

​			-이후 x키를 눌러 메뉴 스테이트로 진입한다.



### 5.개발 범위

​			1)플레이어블 캐릭터 1종

​				(1)공격단계 

​				(2)플레이어를 따라다니는 보조무기 객체

​			2)npc

​				(1)적 5종(지상 2종, 공중 3종)

​				(2)보스(페이즈 구현)

​			3)스테이지  1종

​			4)스테이트

​				로고, 타이틀, 메뉴, 캐릭터 선택, 게임, 일시정지, 컨티뉴, 점수판 구현

### 6.예상 게임 흐름

​			1)메뉴

![](https://postfiles.pstatic.net/MjAyMDEwMTBfNzIg/MDAxNjAyMzMxNTUwMDAw.eSh2eBN5cbVGzQqjCKhz3J3hMxYruxtKlW_rWkPE7w0g.SibvTFpebkMa891HsKJUPUJH-394xBwBXuulWnKvyxQg.PNG.kb9655/%EB%A9%94%EB%89%B4.PNG?type=w580)

​			2)캐릭터 선택

![](https://cdn.cloudflare.steamstatic.com/steam/apps/1261960/ss_e9b5480af44d0c0a40694060ac84d39c70912713.600x338.jpg?t=1598871662)

​			3)스테이지

![](https://postfiles.pstatic.net/MjAyMDEwMTBfMTg3/MDAxNjAyMzMxNTUzNjQz.nBmryWDeNtRgNFZQvk03eYoDHkoezAyFgVa9KIKgmIcg.D-efLbtiLy_3_QdVXkDcgC_Xpp9w-nMHN4xy6E42Ee4g.PNG.kb9655/1.PNG?type=w580)

​			4)보스

![](https://postfiles.pstatic.net/MjAyMDEwMTBfMjE0/MDAxNjAyMzMxNTU2OTY2.0dvVt3_zOCsbbl4XeYYaAznCbEWrfpkNe4QwKdyVNogg.2mSyJCuaA9Ygzsry-ssAZb612TZ5aTiVV-IIOo5Ukmsg.PNG.kb9655/%EB%B3%B4%EC%8A%A4_%EB%93%B1%EC%9E%A5.PNG?type=w580)

​			5)보스 페이즈 변경

![](https://postfiles.pstatic.net/MjAyMDEwMTBfMjM5/MDAxNjAyMzMxNTYzOTY1.f6tH9TSS16yZFYDPc1l0CSVUYIlUFIdACVbR-zadxB0g.HFwXOr2XHGu550kKo0-kK_UQxgjNHSWb7xeYe0gPny4g.PNG.kb9655/%EB%B3%B4%EC%8A%A4%EB%B3%80%EC%8B%A0.PNG?type=w580)

​			6)보스 처치

![](https://postfiles.pstatic.net/MjAyMDEwMTBfMTI4/MDAxNjAyMzMxNTYxMDcw.c_4uNwhzfw0kFHwgpRBDb1DDBWMzw6uYbaaRoDvyAMQg.j5zAHqkjJF9MffW3psLxHliyDXlVESR-NnSmY0_LJRgg.PNG.kb9655/%EB%B3%B4%EC%8A%A4%EA%B2%A9%ED%8C%8C.PNG?type=w580)

​			7)게임 오버

![](https://postfiles.pstatic.net/MjAyMDEwMTBfMjQy/MDAxNjAyMzMxNTY5NTY0.3pXNwhHcczH_kcsJyH4zmuhCHlQ2pFu-wOpdEg7HTykg.1En1YIswcCI7iMyVevfpJtJaF-uq5yweRYdpiq3nipog.PNG.kb9655/%EC%BB%A8%ED%8B%B0%EB%89%B4.PNG?type=w580)

​			8)메뉴판

![](https://postfiles.pstatic.net/MjAyMDEwMTBfMjkz/MDAxNjAyMzMxNTY2NDky.jJ1ozyic12ZNHkHJpgwSpa4kl3KTGtGSLmwtU4hxj6og.lfXUt4tRcnIh1AsZKPlXNKj7LLD0ToZ53-p_Qq4cxMMg.PNG.kb9655/%EC%A0%90%EC%88%98%ED%8C%90.PNG?type=w580)



### 7.개발일정

​	1주차 : 게임 리소스 탐색

​	2주차 : 스테이트 구조 구현, 내용은 기본적인 것만 우선해서 구현

​	3주차 : 수업시간에 배운 프레임워크를 토대로 게임 월드 구현

​	4주차 : 총알 발사, 파괴 등 플레이어블 캐릭터과 npc의 공통적인 기능 구현

​	5주차 : 플레이어블 캐릭터의 보조무기, 피격범위, 공격 단계,  npc의 피격범위 설정

​	6주차 : 보스의  의사결정 구현, npc배치

​	7주차 : 점수판, 캐릭터 선택, 메뉴 구현

​	8주차 : 부족한 부분 수정

### 8.필요한 기술

​	1)다른 과목에서 배운 기술

​		-피격 판정

​	2)이 과목에서 배울것으로 기대되는 기술

​		-배경 화면 스크롤하는 기술

​	3)다루지 않는 것 같아서 수업에 다루어 달라고 요청할 기술

​		-세이브 기능

