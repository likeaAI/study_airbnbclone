# Airbnb Clone Backend
0.0 개발환경 구축하기
0.1 Git 설정하기
git 설치하기
cd [PROJECT_FOLDER]
git init
touch .gitignore
Python_GitIgnore
git add . && git commit --amend --no-edit
git remote add origin [REPOSITORY_URL}
git push origin main --force
0.2 Python 3.8^ 설치하기
Local
GitPod - Default(3.8.13)
GoormIDE
sudo apt update && sudo apt install -y python3.8 && sudo update-alternatives --install /usr/local/bin/python3 python3 /usr/bin/python3.8 0
0.3 Python Virtual Environment 설정하기: Poetry
CLI로 설치하기
curl -sSL https://install.python-poetry.org | python3 -
poetry init
poetry shell
0.3.1 Poetry 살펴보기
poetry init: 프로젝트를 poetry가 관리하게 하기
poetry add [PACKAGE]: poetry로 python package 설치하기
poetry add --dev [PACKAGE]: 개발자전용 package 설치하기
poetry shell: shell 진입하기
exit: shell 나가기
pyproject.toml: 프로젝트의 명세와 의존성 관리하는 파일
0.4 Django Project 시작하기
poetry add django
django-admin startproject config .
0.4.1 Django Project 구조 살펴보기
manage.py
Terminal에서 Django 명령을 실행하게 함
db.sqlite3
Development 단계에서 Django가 임시로 사용하는 DB 파일
첫 runserver 명령과 함께 자동으로 빈 파일로 생성됨
migration을 통해 코드에 알맞은 DB 모양이 되도록 동기화함.
config/
config.settings
Django Project 관한 모든 설정이 이뤄지는 파일
config.urls
Django Project의 Url들을 관리하는 파일
include로 App별 url을 묶어 관리하기 좋다
0.4.1 Django Project 설정하기
config.settings
# Allow Gitpod To run Django Server
ALLOWED_HOSTS = ["localhost"]
CSRF_TRUSTED_ORIGINS = ["https://*.ws-us72.gitpod.io"]
# To use Server Timezone
TIME_ZONE = "Asia/Seoul
# Modulize INSTALLED_APPS
SYSTEM_APPS=[ ... ]
CUSTOM_APPS=[ ... ]
THIRD_PARTY_APPS=[ ... ]
INSTALLED_APPS=SYSTEM_APPS+CUSTOM_APPS+THIRD_PARTY_APPS
0.4.2 Django Project Command(manage.py) 사용하기
python manage.py [COMMAND]
runserver: Django 서버 시작하기
createsuperuser: Admin 계정 만들기
admin 계정을 저장할 DB와 migration이 필요하다
DB를 초기화(삭제)할 때마다 admin 계정을 새로 만들어야 한다
makemigrations >> migrate: Model의 변경사항을 DB에 반영하는 행위
세부적으로 makemigrations은 파일생성,
migrate는 변경된 내용을 적용한다.
shell: Django Shell 켜기
ORM 등 Django 코드를 콘솔에서 테스트하기 좋다
0.5 Django Server 시작하기
python manage.py runserver
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
/admin 접속하여 admin 계정으로 로그인하기
Admin Panel을 접속했다면 서버 준비완료
1.0 Django Application
App은 마치 Folder와 같다. 특정 주제의 Data와 그러한 Logic을 한 곳에 모아놓은 곳이다.
1.1 App을 Create하고 Configure하기
python manage.py startapp [APPNAME_PLURAL]
App의 이름은 복수형으로 하는게 관행이다
apps.py의 class(~Config)을 config.settings의 CUSTOM_APPS에 추가한다
  CUSTOM_APPS = [
    "users.apps.UsersConfig",
  ]
1.2 App Model를 Create하기
django.db.models를 import하기
models.Model을 inherit한 App Model을 Create하기
from django.db import models

class Room(models.Model):
  ...
1.2.1 Model Field와 종류 살펴보기
Field는 models의 메서드로 특정 속성을 가진 데이터형을 제시한다.
class Model([]):
  [FIELD] = models.[FieldType](~)
짧은 텍스트는 CharField로 하고, max_length를 필수로 가진다
긴 텍스트는 TextField를 사용한다
참거짓값은 BooleanField, 양의 정수값은 PositiveIntegerField를 사용한다
이미지파일은 ImageField를 사용하며 파이썬 패키지 Pillow를 필요로 한다
DateTimeField는 날짜시간을 표현한다
날짜만 DateField, 시간만 TimeField
auto_now_add=True: 처음 생성된 날짜
auto_now=True: 마지막으로 업데이트한 날짜
1.2.2 Default / Blank / Null
Default는 Client가 값을 입력하지 않았을 때 주는 기본값이며,
기존 데이터가 새로운 Field가 추가되었을 때 가지는 값이기도 하다
Blank는 Client 측에서 Form Input을 비웠을 때 허용하는지 여부를 정한다
Null는 DB 측에서 Null값을 허용하는지 여부를 정한다
1.2.3 Model 형태가 달라지면 Migration하기
Model을 새로 만들거나 수정하였을 때,
해당 코드에 맞게 DB형태를 바꾸는 과정을 migration이라 한다.
python manage.py makemigration과 python manage.py migrate을 연이어 적용한다.
1.3 App AdminPanel를 Configure하기
django.contrib.admin를 import하기
admin.ModelAdmin을 inherit한 App Admin을 Create하기
Model을 @(Decorator)로 언급하기
from django.contrib import admin
from . import models

@admin.register(models.Room)
class RoomAdmin(admin.ModelAdmin):
  ...
1.3.1 AdminPanel Option 살펴보기
list_display: Admin Panel에 보여줄 Column 속성들을 튜플로 정의하기
list_display = ("[Field]", ...)
list_filter: Admin Panel 우측에 제공할 필터를 튜플로 정의하기
list_filter = ("[Field]", ...)
fieldsets: Admin Panel에서 Data를 생성 또는 수정하는 화면 구성을 정의하기
fieldsets = (
  ("[Section_Title]", {
    "fields": (~),
    "classes": (~),
  }),
  ...fieldset
)
fieldset: 큰 Section으로 튜플로 정의한다
fields: Admin Panel에서 다룰 Model Field 정의하기
classes: FieldSet을 CSS 옵션을 추가한다
wide: 화면을 더 넓게 사용하기
collapse: fieldset을 접을 수 있게 한다
항목이 하나인 튜플에 ,을 넣어 포맷팅으로 사라지는 오류를 방지하자
{"fields": ("name",),}
search_fields: 좌상측에 키워드로 검색하여 항목을 조회할 수 있다
search_fields = ("[COND1]", "[COND2]")
search_help_text로 검색창 하단에 설명을 넣을 수 있다
lookups을 삽입하여 contains가 아닌 다른 옵션을 설정할 수 있다
^(startswith)
=(exact)
search_fields = (
  "owner__username",
  "=price",
)
search_help_text = "~"
actions: 좌상측에 일괄처리 항목을 선택할 수 있다
actions.py을 만들어 별도로 관리할 수 있다 혹은 admin 안에 포함시킬 수 있다
Custom Action 정의하기
@admin.action(description="~")
def [custom_action](model_admin, request, instances):
  for instance in instances.all():
    ...
    instance.save()
Admin에 actions 포함시키기
from .actions import [custom_action]

@admin.register(Model)
class Admin(admin.ModelAdmin):

  actions = ([custom_action], ...)
1.4 Abstract Model 사용하기
Common App을 Create하기(Optional)
django-admin startapp common
config.settings에 CommonConfig을 CUSTOM_APPS에 추가하기
TimeStampedModel을 Create하기
created와 updated를 DateTimeField로 하기
created: auto_now_add를 True하기
updated: auto_now를 True하기
내부클래스 class Meta에 abstract=True하기
class TimeStampedModel(models.Model):
  class Meta:
    abstract=True
abstract=True하면 해당 Model은 DB에 저장되지 않는다
해당 Abstract Model을 import하여 사용할 Class에 inherit하기
from common.models import TimeStampedModel

class Model(TimeStampedModel):
  ...
2.0 User App
User App을 새로 처음부터 만들기보다 Django에서 제공하는 User App을 확장하는 게 효과적이다
첫 migration 전에 미리 Custom User를 세팅하는 것이 바람직하다.
만약 이미 어느정도 작업했다면 db.sqlite3과 __init__파일을 제외한 모든 각 App 폴더의 migrations/ 파일을 삭제하고 Custom User를 세팅한다.
2.1 Custom User App 세팅하기
users App을 create하기
AUTH_USER_MODEL을 정하기
config.settings에 Django User를 inherit 받을 User App을 AUTH_USER_MODEL하겠다고 설정한다.
AUTH_USER_MODEL = "users.User"
django.contrib.auth.models.AbstractUser을 import하기
User Model 만들기
Model의 경우, models.Model 대신에 AbstractUser을 inherit하기
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
  ...
User AdminPanel 만들기
django.contrib.auth.admin.UserAdmin을 import하기
Admin의 경우, admin.UserAdmin 대신에 UserAdmin을 inherit하기
from django.contrib.auth.admin import UserAdmin
from . import models

@admin.register(models.User)
class CustomUserAdmin(UserAdmin):
  ...
2.2 User Model 만들기
AbstractUser가 가진 field를 참고하기
기존의 first_name과 last_name은 사용 안하도록 editable을 False하기
입력이 아닌 선택지를 주려면 CharField에 choices 항목을 주기
gender = models.CharField(
  max_length=5,
  choices=GenderChoices.choices,
  default=GenderChoices.MALE,
)
Choices는 내부클래스로 정의한다
django.db.models.TextChoices를 inherit한다
변수명은 UPPERCASE로 정하고, 튜플 안에 첫번째 항목은 DB에 저장되는 값으로 lowercase를, 두번째 항목은 Client가 보는 항목으로 TitleCase로 표기한다
class GenderChoices(models.TextChoices):
  MALE = ("male", "Male")
  ...
2.3 User Admin 만들기
UserAdmin 참고하기
fieldsets을 설정하여 기존 UserAdmin의 항목을 확장한다
3.0 Project에 필요한 App 만들기
3.1 Room App & Amenity Model
Room은 여러 Relationship을 가진다.
User owner은 Room을 소유하며(ForeignKey),
Room들은 여러 Amenity를 가진다(ManyToManyField)
__str__을 수정하여 Room이 Admin Panel에 어떻게 표현되는지 수정한다
Admin Panel은 단수형 Model 이름에 단순히 -s를 붙여 복수형을 표현한다. 따라서 Amenities의 경우 복수형을 직접 표현해주어야 한다
inherit한 Abstract Model의 Field를 Admin Panel에 드러나게 만들어보자(read_only)
3.1.1 Room Model을 Create하기
ForeignKey는 연결할 모델과 연결된 모델이 삭제되었을 때 대응을 언급해야 한다
연결할 모델은 다음과 같은 방식으로 표시한다
같은 파일 내 모델의 경우,
models.ForeignKey("model", on_delete=models.CASCADE)
다른 App의 모델의 경우,
models.ForeignKey("app.model", on_delete=models.CASCADE)
on_delete로 연결된 모델이 삭제되었을 때 대응을 정한다
models.CASCADE: 함께 삭제된다
models.SET_NULL: 내역이 남는다(Null=True 함께 사용)
3.1.2 Room Admin을 Configure하기
Reverse Accessor
ForeignKey나 ManyToManyField는 역으로 Model을 접근할 수 있는데 이는 기본적으로 _set라는 이름 가진다
class User(~):
  ...
  rooms = self.room_set.count()
예를 들어, 각 room은 host를 가지는데, host는 여러 rooms를 가질 수 있다. 이때 이 room_set은 User 입장에서 self.room_set으로 접근 가능하다
Reverse Accessor가 보다 직관적인 이름을 가지도록 하려면 related_name으로 항목을 준다
# rooms/models.py
class Room(~):
  ...
  host = models.ForeignKey(
    "users.User",
    on_delete=models.CASCADE,
    related_name="rooms",
  )
# users/models.py
class User(AbstractUser):
  ...
  rooms = self.rooms.count()
Model Method
Model Class이나 Admin Class는 Method를 가질 수 있다
Method는 Class 속 Function으로 DB에서 처리한 값을 return하는데 사용한다.
Model Method는 self를 첫번째 인자로 가진다. self는 직관적으로 Model 이름을 가져도 좋다.
ORM으로 Room Amenities의 합계 구하기
ORM(Object Relational Mapper)로 python 코드로 DB를 CRUD할 수 있다.
ORM을 통해 얻은 DB 결과는 QuerySet 형태를 띄며, 이를 통해 여러 작업을 할 수 있다. 총합은 .count를 사용한다
class Room(~):
  ...
  def total_amenities(room):
    return room.amenities.count()
ORM 예시
.objects.all(): 해당 model의 모든 Instance를 불러온다
[QUERYSET].count(): 해당 QuerySet 안의 Instance 갯수를 return한다.
3.1.3 Amenity App & Admin를 Create하기
ManyToManyField는 1대多 관계를 표현한다.
models.ManyToManyField("app.model")
AdminPanel에서 복수형 표현을 수정해야 한다면,
class Meta로 verbose_name_plural 이용하기
class Amenity(Model):

  class Meta:
    verbose_name_plural = "~"
readonly한 field를 AdminPanel 수정창에 뜨도록 하려면,
readonly_fields에 표시한다
readonly_fields = ("~", ...)
3.2 Experience App & Category App
Room App과 같은 전개로 만들어가되 숙박 개념이 없는 experience는 당일 시작시간과 종료시간을 가지도록 한다
Room의 부속시설인 Amenity처럼 Experience는 Perk을 ManytoManyField로 가진다.
Category는 Room 또는 Experience의 그룹이다
3.3 Review App
__str__ 메서드가 return할 값을 customize할 수 있다. f"" String을 활용해 변수들을 {~}에 넣어 표현 가능하다.
def __str__(self):
  return f"{self.user} / {self.rating}"
Room Reviews들의 평균(Average)을 구하는 Class Method을 만든다
산술평균: 
의총합
갯수
 
해당 Room의 Review 갯수 구하기
self.reviews.count()
Review 갯수가 0일 때 예외처리하기
Review Ratings의 총합 구하기
모든 reviews에서 rating만 가져오기
self.reviews.all().values("rating")
for문 돌려서 rating값 누적합하기
return할 때 소수점 아래 두자리 반올림하기(round)
list_filter는 단순히 해당 Model의 Field만 가능한게 아니라 __로 다른 ForeignKey로 접근한 다른 Model의 Field도 기준으로 삼을 수 있다.
list_filter = (
  "user__is_host",
  "room__category",
)
Custom Filter를 만들어 이를 list_filter에 기재할 수 있다.
django.contrib.admin.SimpleListFilter를 import하기
admin.py에 inline으로 작성해도 좋고 filter.py를 별도로 만들어 관리할 수 있다.
class CustomFilter(SimpleListFilter):
  title = "~"
  parameter_name = "~"

  def lookups(self, request, model_admin):
    return [("PARAM_VALUE", "CLIENT_NAME"), ...]
  
  def queryset(self, request, queryset):
    param = self.value()
    match = {
      "PARAM_VALUE": queryset.filter(~),
      ...
    }
    return match.get(param, queryset)
title / parameter_name 값을 입력한다
title은 Admin Panel 우측 Filter칸에 Filter 이름을 말한다
parameter_name은 URL에서 parameter 이름을 무엇으로 할지 정한다
lookups Function은 Client에게 Filter에 어떻게 보일지 정하는 것이다.
queryset Function은 param에 따라 제시할 queryset을 filter하여 제시한다.
.get은 param이 있을 때 match Dictionary를 참고하지만, 없다면 전체 queryset을 돌려준다
Custom Filter를 admin.py에 import하고 list_display에 추가한다
3.4 Media App
Media를 Local에서 처리할 때와 별도의 DB에서 media를 다룰 때가 다르다.
Local에서 Media를 다룰 경우,
Model: ImageField / FileField 사용하기
poetry add pillow
config.settings: MEDIA_ROOT와 MEDIA_URL 정하기
MEDIA_ROOT: 프로젝트 내 실제 파일을 저장하는 장소
MEDIA_URL: 해당 파일을 접근하는 URL
config.urls: urlpatterns에 static을 설정해준다
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
  ...
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
별도의 DB에서 Media를 다룰 경우,
Media를 다루는 모든 Field를 URLField로 바꾸기
4.0 Django Url & Django View
4.0.1 Django가 웹을 구현하는 과정
Django가 BackEnd에서 FrontEnd로 Data를 구현할 때,
다음 3단계를 거친다
Model + Url - View - Template
Model은 DB에 담긴 data에 대한 정의를 말한다
Url은 Client가 접속하는 Url을 정의하고 처리하는 함수를 연결해준다
View는 Url을 접속할 때 Response를 처리하는 함수이다
Template은 Response한 응답한 HTML이다
이번 프로젝트에서는 Django Template을 사용하지 않고 React로 FrontEnd를 구현할 것이다
따라서, Template 대신 data를 json으로 구현할 API로 Response 하겠다
4.1 Django Url
config/urls.py
django.urls에서 path와 include를 import하기
from django.urls import path, include
urlpatterns라는 list([])를 만들어 path들을 관리한다.
urlpatterns = [
  path(~),
]
각 app폴더마다 url을 따로 관리하는 경우에는,
path에 url과 [apps].urls 경로가 포함된 include를 넣는다.
path("rooms/", include("rooms.urls"))
[apps]/urls.py
django.urls.path와 views.py 내 모든 view들을 import한다
from django.urls import path
from . import views
urlpatterns을 만들고 path에 include 이후 이어지는 url과 view를 적는다
urlpatterns = [
  path("", views.rooms),
  ...
]
FBV(Function-based View)가 아닌 CBV(Class-based View)를 채택한다면 .as_view()를 덧붙인다
path("", views.Room.as_view())
Url에 변수를 주려면 <[DATATYPE]:[PARAM_NAME]>로 표현한다.
path("<int:pk>", views.RoomDetail.as_view())
4.1.1 Reverse Accessor CRUD URL 분리하기
RoomReviews, RooomPhotos와 같이 Reverse Accessor로 처리하는 경우 CRUD를 구분하는 것이 편리하다
GET 경우 Relationship을 URL에 드러내는 것이 좋다
/rooms/1/reviews/
POST의 경우도 일괄 처리하기 편리하게 Relationship 표시한다
DELETE나 PUT의 경우 각 Instance에 대한 처리이므로 별도 처리가 편하다
reivews/35
4.2 Django View
모든 View function은 첫번째 인자로 request를 가진다
URL에 변수를 주면 View Function은 인자를 받을 수 있다
# urls.py
path("<int:pk>", views.~)
# views.py
def room(request, pk):
  ...
Json을 return하는 View를 만드려면 다음 사항이 필요하다
from django.http import HttpResponse
from django.core import serializers

def rooms(request):
  queryset = Room.objects.all()
  data = serializers.serialize("json", queryset)
  return HttpResponse(content=data)
QuerySet을 가져온다
Serializer로 QuerySet을 Json으로 변환한다
Json화된 data를 Response로 return한다
5.0 Django REST Framework로 API 만들기
5.1 DRF 설치하기
Poetry로 DRF 설치하기
poetry add djangorestframework
config.settings에서 THIRD_PARTY_APPS에 DRF를 등록하기
THIRD_PARTY_APPS = ["rest_framework",]
DRF를 사용할 views.py에 import하기
import rest_framework

### 5.2 DRF로 Function-based View(FBV) 만들기
1. `DRF Response`
- `rest_framework.response.Response`로 import하기
```python3
def view(request):
  ...
  return Response([JSON])
DRF Serializer
rest_framework.serializers.Serializer를 import하기
serializers.py를 만들어 관리하기
serialize할 model를 import하고 json에 포함할 field를 맞대응하여 추가한다
serializers.ModelField(~)식으로 추가한다
@api_view
rest_framework.decorators.api_view
view 바로 위에 @api_view()를 설정한다
get이 default고 다른 HTTP_METHOD를 허용하고 싶다면
List([])에 넣는다
@api_view(["GET", "POST"])
class View(~):
HTTP_METHOD는 if문을 request_method로 처리한다.
if request.method == "GET":
  ...
elif request.method == "POST":
  ...
5.2.1 DRF Serializer로 HTTP METHOD 처리하기
GET
LIST형이냐 DETAIL형이냐를 구분한다
LIST형
queryset = Model.objects.all()
serializer = Serializer(queryset, many=True)
return Response(serializer.data)
queryset을 받아 serializer 처리해준뒤, .data하여 Response한다
queryset에 data가 여러개일 경우, many=True한다
DETAIL형
from rest_framework.exceptions import NotFound

try:
  queryset = Model.objects.get(pk=pk)
except Model.DoesNotExist:
  return NotFound
...
serializer = Serializer(queryset)
return Response(serializer.data)
해당 pk인 Instance가 존재하는지 확인한다.
POST
# views.py
if not request.user.is_authenticated:
  return NotAuthenticated
POST하기 전에, 사이트에 인증받은(Authenticated) 세션인지 확인한다
serializer = Serializer(data=request.data)
if serializer.is_valid():
  new_data = serializer.save()
  serializer = Serializer(new_data)
  return Response(serializer.data)
else:
  return Response(serializer.errors)
POST는 client의 form data를 받아 server에서 처리하는 것이므로 request의 data를 data=request.data식으로 받는다
client가 입력한 data를 검증(.is_valid())하고 검증이 성공하면 계속 진행하며, 문제가 있을 경우 serializer.errors를 return한다
해당 data가 valid하다면 serializer.save()를 진행한다. POST에서 save는 create메서드에서 진행된다
다시 한번 serializer를 진행하고 이를 Response해준다
# serializer.py
def create(self, validated_data):
  return Category.objects.create(
    **validated_data
  )
.objects.create(~)로 data를 DB에 생성한다
valid된 data를 **를 앞에 붙여 자동으로 처리하게 한다
PUT
if not request.user.is_authenticated:
  return NotAuthenticated
if model.owner != request.user:
  return PermissionDenied
인증(Authenticated)받은 세션인가?
해당 data를 만든 장본인(Permission)인가?
try:
  queryset = Model.objects.get(pk=pk)
except Model.DoesNotExist:
  return NotFound
...
serializer = Serializer(
  queryset,
  data=request.data,
  partial=True,
)
if serializer.is_valid():
  updated_data = serializer.save()
  serializer = Serializer(updated_data)
  return Response(serializer.data)
else:
  return Response(serializer.errors)
PUT은 GET한 data를 client가 POST한 data로 변경하는 것이므로 queryset과 request.data 모두 필요하다
partial=True함으로써 일부 field만 입력해도 수정가능하게 한다
이후 data검증(.is_valid)하고 POST와 같이 검증이 성공하면 save한 뒤 Response한다
PUT에서 save는 update 메서드에서 진행된다
def update(self, instance, validated_data):
  instance.field1 = validated_data.get("field1_name", instance.field1)
  instance.field2 = validated_data.get("field2_name", instance.field2)
  ...
  instance.save()
  return instance
instance는 DB에 가져온 수정할 data이고
validated_data는 client가 입력할 수정될 data다
instance를 이루는 모든 field를 설명하고 이를 .get하여 수정할 data가 있으면 대체하고 아니면 기존 data로 둔다
마지막으로 instance를 save하고 return한다
DELETE
if not request.user.is_authenticated:
  return NotAuthenticated
if model.owner != request.user:
  return PermissionDenied
인증(Authenticated)받은 세션인가?
해당 data를 만든 장본인(Permission)인가?
try:
  queryset = Model.objects.get(pk=pk)
except Model.DoesNotExist:
  return NotFound
...
from rest_framework.status import HTTP_204_NO_CONTENT

queryset.delete()
return Response(status=HTTP_204_NO_CONTENT)
실제 DB에서 queryset을 삭제하는 과정 .delete()이다
삭제로 인해 GET할 data가 없음을 보여주기 위해 204 Error를 Response한다.
5.2.2 DRF Error와 DRF StatusCode
rest_framework.exceptions
해당 exception 상황에서 error를 raise하면 된다
NotFound: 해당 data가 존재하지 않을 때,
try:
  data = Model.objects.get(pk=pk)
  ...
except Model.DoesNotExist:
  raise NotFound
NotAuthenticated: 로그인하지 않은 세션일 때,
if not request.user.is_authenticated:
  raise NotAuthenticated 
PermissionDenied: data의 주인이 아닌 자가 PUT이나 DELETE를 시도할 때,
if model.owner != request.user:
  raise PermissionDenied
ParseError: 기타 유효하지 않은 Data에 대한 Error
raise ParseError("Invalid Data")
rest_framework.status
Response할 때, statuscode를 보낼 수 있다
...
return Response(status=~)
HTTP_200_OK: 정상적인 Response
HTTP_204_NO_CONTENT: data를 delete했을 때,
HTTP_404_NOT_FOUND: 해당 page가 존재하지 않을 때,
5.2.3 DRF Permissions
IsAuthenticated한지 직접 조건문을 작성하지 않고 import할 수 있다.
rest_framework.permissions를 import하기
IsAuthenticated 혹은 IsAuthenticatedOrReadOnly 선택하기
IsAuthenticated: 허가된 자만 모든 CRUD 행위 가능함
IsAuthenticatedOrReadOnly: GET을 제외한 모든 CRUD 행위는 허가된 자만 가능함
permission_classes에 포함시키기
from rest_framework.permissions import IsAuthenticatedOrReadOnly

class VIEW(APIView):
  
  permission_classes = [IsAuthenticatedOrReadOnly]

  ...
5.3 DRF APIView
FBV 대신 CBV를 사용했을 때 장점은 다음과 같다.
if..elif문 대신 Class Method로 HTTP_METHOD를 관리하여 가독성이 높다
pk인 queryset을 얻는 과정을 별도의 Class Method로 관리하면 코드가 간결해진다
CBV를 작성하는 방법은 다음과 같다.
urls.py에서 class를 view로 사용하려면 .as_view()을 추가해줘야 한다
path("", views.RoomList.as_view()),
rest_framework.views.APIView를 import하고 inherit한다
from rest_framework.views import APIView

class RoomList(APIView):
  ...
HTTP Method 메서드의 인자는 self, request 그리고 url을 통해 받은 변수이다
class RoomDetail(APIView):
  def get(self, request, pk):
    ...
5.3.1 ForeignKey가 있는 App의 POST 처리하기
.is_valid() 이후, request.data.get(~)을 통해 ForeignKey의 pk 값을 저장한다
해당 ForeignKey가 null=True가 아니라면 pk가 존재하는지 확인한다.
pk인 data가 DB에 존재하는지 확인한다.
foreignkey_pk = request.data.get("foreignkey")
try:
  queryset = Model.objects.get(pk=foreignkey_pk)
  ...
except Model.DoesNotExist:
  raise ParseError("Data not found.")
.save(~) 안에 validated된 foreignkey를 직접 넣어준다
new_data = serializer.save(
  owner=request.user,
  model=queryset,
)
ForeignKey를 포함한 data를 Serializer 거쳐주고 마지막으로 Response한다
5.3.2 ForeignKey가 있는 App의 PUT 처리하기
.is_valid() 이후, request.data.get(~)을 통해 ForeignKey의 pk 값을 저장한다
client가 입력한 ForeignKey data에 pk가 존재하는지 확인한다.
pk인 data가 DB에 존재하는지 확인한다.
foreignkey_pk = request.data.get("foreignkey")
try:
  queryset = Model.objects.get(pk=foreignkey_pk)
  ...
except Model.DoesNotExist:
  raise ParseError("Data not found.")
수정하고자 하는 Foreignkey Data가 있는지 여부에 따라 .save()를 다르게 처리한다
if foreignkey_pk:
  ...
  updated_data = serializer.save(data=data)
else:
  updated_data = serializer.save()
ForeignKey를 포함한 data를 Serializer 거쳐주고 마지막으로 Response한다
5.3.3 ManyToManyField를 Serialize할 때 transaction이 필요한 이유
ForeignKey와 달리 ManyToManyField는 .save()이후에 추가된다. 이는 MTMField가 error를 발생해도 이미 DB에 완성되지 않은 data가 저장되어버린다는 뜻이다
이를 해결하기 위해서 django.db.transaction을 이용하여 transaction.atomic 도중에 발생하는 error가 발생할 경우, rollback하여 data가 DB에 저장되지 않도록 한다
from django.db import transaction
...
with transaction.atomic():
  .save(~)
  ...
5.3.4 ManyToManyField가 있는 App의 POST 처리하기
is_valid() 이후에 request.data로부터 MTMField의 pk list를 저장한다
mtm_pks = request.data.get("mtms")
.save() 이전에 transaction.atomic()을 진행한다
transaction이 실패할 경우, 이를 error 처리하기 위해서 transaction 바깥쪽에 try..except문을 한다
try:
  with transaction.atomic():
    new_data - serializer.save(~)
    ...
client가 입력한 amenities가 있을 경우, for문을 돌려 각 pk에 대한 data를 DB에 찾아 add해준다
if mtm_pks:
  for mtm_pk in mtm_pks:
    mtm = MtmField.objects.get(pk=mtm_pk)
    new_data.mtms.add(mtm)
만약 Except가 발생할 경우, 해당 MTMField가 존재하지 않는지, 기타 오류로 인한건지 구분해서 Error를 띄운다
try:
...
except Model.DoesNotExist:
  raise ParseError("~")
excpet Exception as e:
  raise ParseError(e)
5.3.5 ManyToManyField가 있는 App의 PUT 처리하기
is_valid() 이후에 request.data로부터 MTMField의 pk list를 저장한다
mtm_pks = request.data.get("mtms")
.save() 이전에 transaction.atomic()을 진행한다
transaction이 실패할 경우, 이를 error 처리하기 위해서 transaction 바깥쪽에 try..except문을 한다
try:
  with transaction.atomic():
    updated_data = serializer.save(~)
    ...
client가 입력한 amenities가 있을 경우, 한번 clear해주고 for문을 돌려 각 pk에 대한 data를 DB에 찾아 add해준다
if mtm_pks:
  updated_data.mtms.clear()
  for mtm_pk in mtm_pks:
    mtm = MtmField.objects.get(pk=mtm_pk)
    new_data.mtms.add(mtm)
만약 Except가 발생할 경우, 해당 MTMField가 존재하지 않는지, 기타 오류로 인한건지 구분해서 Error를 띄운다
try:
...
except Model.DoesNotExist:
  raise ParseError("~")
excpet Exception as e:
  raise ParseError(e)
5.4 DRF ModelSerializer
일반 Serializer가 Model Field를 일일히 대응시켜야 한다는 불편함이 있기 때문에 이를 해결해주는 게 ModelSerializer이다.
rest_framework.serializers.ModelSerializer를 import한다
class Meta를 열고 model과 fields를 설명한다
from rest_framework import serializer
from .models import Model


class Serializer(ModelSerializer):
  class Meta:
    model = Model
    fields = "__all__"
fields는 json에 넣은 field를 튜플에 추가한다. 모든 field를 보여주려면 "__all__"으로 표현한다.
반대로 제외할 field가 있다면 exclude를 한다
fields를 직접 입력하는 경우, pk 항목을 넣어주자
5.4.1 ModelSerializer로 ForeignKey 처리하기
ForeignKey를 fields에만 언급하면 pk값만 나온다
ForeignKey의 자세한 data가 필요하다면 해당 model의 serializer를 언급하면 된다
class Serializer(ModelSerializer):

  foreign_key = FkSerializer()

  class Meta:
    model = Model
    fields = "__all__"
ManytoManyField의 경우, Serializer에 many=True를 언급해야 모든 개체를 포함한다
ForeignKey를 POST나 PUT할 경우, read_only=True로 처리하고 View 로직으로 직접 처리한다
5.4.2 SerializerMethodField로 Method data를 json에 넣기
rest_framework.serializers.SerializerMethodField를 import하기
Serializer Class에 SerializerMethodField 정의하기
class Serializer(ModelSerializer):
  rating = SerializerMethodField()
해당 SerializerMethodField를 get_ method로 처리하기
def get_[method](self, instance):
  return model.model_method()
해당 SerializerMethodField를 list_display에 표현하기
class Meta:
  fields = (
    ...
    "method",
  )
5.4.3 Serializer Context로 request data를 serializer에 가져오기
view 안에 Serializer에 context 항목을 추가하기
Serializer(
  queryset,
  context={"request": request},
)
SerializerMethodField를 정의하고 self.context에서 request를 가져오기
is_owner = SerializerMethodField()

def get_is_owner(self, room):
  request = self.context["request"]
  return room.owner == request.user
5.5 상황별 Serializers 구상하기
Data 구조가 단순하고 수량이 적다면 App Serializer 하나면 충분하다
Data 개수가 많다면 List형과 Detail형을 나누어 관리한다
List형은 말그대로 목록에 드러나는 경우로 일부 정보만 드러낸다
Detail형은 특정 한 경우를 자세히 설명하는 것으로 거의 모든 정보를 드러낸다
User처럼 본인에게만 허용되는 정보가 포함된다면 Private, Public으로 나눠서 관리하며 필요할 경우 추가로 만든다
Private
Public
User의 경우, TinyUserSerializer를 만들어 avatar와 name만 드러낼 수 있다
