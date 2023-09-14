# HTTP HTTPS и их параметры 
***
## Лабораторная работа №1

### РГУПС

Скрипт при помощи которого получил информацию о сайте  __[‍РГУПС](https://www.rgups.ru)__: 

`curl rgups.ru -I -k -L -s`

Использовались такие ключи как:

`-I` - Этот ключ указывает отправить только заголовки HTTP-ответа сервера, без тела ответа.  
`-k` - Этот ключ отключает проверку SSL-сертификата.  
`-L` - Этот ключ указывает следовать перенаправлениям при запросе, если сервер возвращает код (301 или 302).  
`-s` - это бесшумный режим

Ответ:

```shell
HTTP/1.1 301 Moved Permanently #Статус ответа, который указывает, что запрашиваемый ресурс был перемещен на постоянной основе и содержит новый адрес (URL) 
Server: nginx/1.19.1 #Веб-сервер, обслуживающий запрос, будет использовать программное обеспечение nginx версии 1.19.1.
Date: Thu, 07 Sep 2023 11:20:47 GMT #Дата и время отправки ответа от сервера  
Content-Type: text/html #Тип контента, предоставляемый сервером в данном ответе, будет HTML
Content-Length: 169 #Размер содержимого ответа в байтах: 169 байт 
Connection: keep-alive #Поддержание соединения между клиентом и сервером после обмена текущими данными  
Location: https://rgups.ru/ #URL

HTTP/1.1 200 OK #Статус ответа, означающий, что запрос клиента был успешно выполнен.
Server: nginx/1.19.1 #Веб-сервер, обслуживающий запрос, будет использовать программное обеспечение nginx версии 1.19.1.
Date: Thu, 07 Sep 2023 11:20:49 GMT #Дата и время отправки ответа от сервера. 
Content-Type: text/html; charset=utf-8 #Тип контента, предоставляемый сервером в данном ответе будет HTML с указанным набором символов UTF-8
Connection: keep-alive #Поддержание соединения между клиентом и сервером после обмена текущими данными 
X-Powered-By: ProcessWire CMS #Контент-менеджер сайта  
Set-Cookie: wire=3f9fa34b1c69a454fc5a9aaac409516a; path=/; HttpOnly; SameSite=Lax #устанавливает cookie с именем "wire", значением, дополнительными настройками доступности и атрибутами безопасности 
Expires: Thu, 19 Nov 1981 08:52:00 GMT #Заголовок управления кэшированием, указывающий, что ресурс истек и не должен храниться в кэше 
Cache-Control: no-store, no-cache, must-revalidate # Заголовок управления кэшированием, указывающий, что ответ не должен кэшироваться и должен быть повторно подтвержден перед каждым использованием
Pragma: no-cache #Дополнительный заголовок, который сообщает клиенту, что кэширование данного ответа запрещено
```

### GitHub

Скрипт при помощи которого получил информацию о сайте  __[GitHub](https://github.com/)__:

`curl github.com -I -k -L -s`

Ответ:

```shell
HTTP/1.1 301 Moved Permanently
Content-Length: 0
Location: https://github.com/

HTTP/1.1 200 OK
Server: GitHub.com
Date: Wed, 13 Sep 2023 19:48:54 GMT
Content-Type: text/html; charset=utf-8
Vary: X-PJAX, X-PJAX-Container, Turbo-Visit, Turbo-Frame, Accept-Language, Accept-Encoding, Accept, X-Requested-With #Этот заголовок указывает на факторы, 
которые могут влиять на кэширование ответа на стороне клиента или прокси-сервера. 
content-language: en-US #Этот заголовок указывает на язык контента, который отправляется в ответе.
ETag: W/"690edd9a6201ee8d2529c6d7fee665c2" #Этот заголовок представляет собой метку, которая идентифицирует уникальную версию ресурса. Он используется для управления кэшированием на стороне клиента. Если ресурс изменяется, ETag изменяется, и клиент может использовать его для определения, нужно ли ему получить обновленную версию ресурса.
Cache-Control: max-age=0, private, must-revalidate 
Strict-Transport-Security: max-age=31536000; includeSubdomains; preload #Этот заголовок относится к безопасности. Он указывает, что клиент должен поддерживать строгую защиту транспортного уровня (HTTPS) в течение 31536000 секунд и включать поддомены 
X-Frame-Options: deny #Это мера безопасности, которая может помочь предотвратить атаки.
X-Content-Type-Options: nosniff #Этот заголовок предотвращает браузер от интерпретации содержимого как чего-то, отличного от указанного в Content-Type.
X-XSS-Protection: 0 #Этот заголовок указывает на то, что браузер не должен активировать механизм защиты от межсайтового скриптового выполнения (XSS)
Referrer-Policy: origin-when-cross-origin, strict-origin-when-cross-origin #Этот заголовок управляет тем, какой информацией о предыдущей странице делится браузер при переходе по ссылке.
Content-Security-Policy: default-src 'none'; base-uri 'self'; child-src github.com/assets-cdn/worker/ gist.github.com/assets-cdn/worker/; connect-src 'self' uploads.github.com objects-origin.githubusercontent.com www.githubstatus.com collector.github.com raw.githubusercontent.com api.github.com github-cloud.s3.amazonaws.com github-production-repository-file-5c1aeb.s3.amazonaws.com github-production-upload-manifest-file-7fdce7.s3.amazonaws.com github-production-user-asset-6210df.s3.amazonaws.com cdn.optimizely.com logx.optimizely.com/v1/events *.actions.githubusercontent.com productionresultssa0.blob.core.windows.net/ productionresultssa1.blob.core.windows.net/ productionresultssa2.blob.core.windows.net/ productionresultssa3.blob.core.windows.net/ productionresultssa4.blob.core.windows.net/ productionresultssa5.blob.core.windows.net/ productionresultssa6.blob.core.windows.net/ productionresultssa7.blob.core.windows.net/ productionresultssa8.blob.core.windows.net/ productionresultssa9.blob.core.windows.net/ wss://*.actions.githubusercontent.com github-production-repository-image-32fea6.s3.amazonaws.com github-production-release-asset-2e65be.s3.amazonaws.com insights.github.com wss://alive.github.com github.githubassets.com; font-src github.githubassets.com; form-action 'self' github.com gist.github.com objects-origin.githubusercontent.com; frame-ancestors 'none'; frame-src viewscreen.githubusercontent.com notebooks.githubusercontent.com support.github.com; img-src 'self' data: github.githubassets.com media.githubusercontent.com camo.githubusercontent.com identicons.github.com avatars.githubusercontent.com github-cloud.s3.amazonaws.com objects.githubusercontent.com objects-origin.githubusercontent.com secured-user-images.githubusercontent.com/ user-images.githubusercontent.com/ private-user-images.githubusercontent.com opengraph.githubassets.com github-production-user-asset-6210df.s3.amazonaws.com customer-stories-feed.github.com spotlights-feed.github.com *.githubusercontent.com; manifest-src 'self'; media-src github.com user-images.githubusercontent.com/ secured-user-images.githubusercontent.com/ private-user-images.githubusercontent.com github.githubassets.com; script-src github.githubassets.com; style-src 'unsafe-inline' github.githubassets.com; upgrade-insecure-requests; worker-src github.com/assets-cdn/worker/ gist.github.com/assets-cdn/worker//* # это дополнительный уровень безопасности, позволяющий распознавать и устранять определённые типы атак, таких как Cross Site Scripting (XSS) и атаки внедрения данных
Set-Cookie: gh_sess=BhW9DTjnOfpPd12bTHIp1OG1MaNkvgyCypHS0skPYeZNhjLWn5WxKUPYA12d%2BV9Jm27DW5FtvCu9qQqAoxmdvqn2EImHVVXi80nyYjTtL0nJ2HpXnWjPv2BivJKfUDFK27i1Nr0rNyByWoeA0G8Xt3hys2xsb6bDsUUqOZRDuImT%2BA%2BiT6ATbiGOZMuxD6wV%2BaNmuig%2B2cyWCIoejZBUF2Csb%2FmAuuL%2F3YJlSFKVk%2BwsK%2FvmpXenHoC%2By%2FxGkD8mY9dSLFiT5GgK4754bInvkw%3D%3D--WWqqxkVjNoLO09Wu--1Nyl%2F%2Biay6nXpEMIFkWNbQ%3D%3D; Path=/; HttpOnly; Secure; SameSite=Lax
Set-Cookie: octo=GH1.1.22200406.1694634541; Path=/; Domain=github.com; Expires=Fri, 13 Sep 2024 19:49:01 GMT; Secure; SameSite=Lax
Set-Cookie: logged_in=no; Path=/; Domain=github.com; Expires=Fri, 13 Sep 2024 19:49:01 GMT; HttpOnly; Secure; SameSite=Lax
Accept-Ranges: bytes #Этот заголовок указывает, что сервер поддерживает диапазоны запросов для данного ресурса.
X-GitHub-Request-Id: A548:0762:323A68B:32BD932:6502122D* #Этот заголовок содержит идентификатор запроса, который может быть полезен для отслеживания запроса на стороне сервера. 
```

### РЖД

Скрипт при помощи которого получил информацию о сайте  __[РЖД](https://www.rzd.ru/)__:

`curl rzd.ru -I -k -L -s --User-agent "Yandex"`

Использовал дополнительно такую строку как:

`--User-agent "Yandex"` -  Это строка, которую клиент  отправляет на сервер, чтобы указать серверу, какое программное обеспечение или устройство отправляет запрос.  

Ответ:

```shell
HTTP/1.1 301 Moved Permanently
Date: Wed, 13 Sep 2023 20:00:30 GMT
Content-Type: text/html
Content-Length: 150
Connection: keep-alive
Location: https://rzd.ru:443/

HTTP/1.1 301 Moved Permanently
Content-Type: text/html
Content-Length: 185
Connection: keep-alive
Date: Wed, 13 Sep 2023 20:00:33 GMT
Location: https://www.rzd.ru/
Set-Cookie: session-cookie=17848dc3ab95c760f9dbb0b218991a2460554ebefea73af54747e35dbae4478456623511784e74b68efda2f29082d750; Max-Age=86400; Path=/; secure; HttpOnly
X-XSS-Protection: 1; mode=block #Этот заголовок говорит браузеру о включенной защите от XSS и указывает ему блокировать скрипты, 
которые могут представлять угрозу безопасности

HTTP/1.1 200
Content-Type: text/html;charset=utf-8
Content-Length: 209269
Connection: keep-alive
Date: Wed, 13 Sep 2023 20:00:36 GMT
Vary: Accept-Encoding
X-UCM-Pod-Name: inex-ucm-776d97f9d-lpczs #Этот заголовок связан с идентификацией серверного подключения.
Strict-Transport-Security: max-age=15724800; includeSubDomains
Via: nginx2 #Этот заголовок указывает на прокси-сервер, через который прошел запрос.
X-Frame-Options: sameorigin
Set-Cookie: session-cookie=17848dc3c56da89cf9dbb0b218991a240e7fe25db53f0c416d9395ca18348a895d543dc9fc3850d15ddd5e3c55cb8346; Max-Age=86400; Path=/; secure
X-XSS-Protection: 1; mode=block
```

### Yandex

Скрипт при помощи которого получил информацию о сайте  __[Яндекс](https://yandex.ru/)__:

`curl yandex.ru -I -k -L -s --User-agent "Yandex"`

Ответ:

```shell
HTTP/1.1 302 Moved temporarily
Accept-CH: Sec-CH-UA-Platform-Version, Sec-CH-UA-Mobile, Sec-CH-UA-Model, Sec-CH-UA, Sec-CH-UA-Full-Version-List, Sec-CH-UA-WoW64, Sec-CH-UA-Arch, Sec-CH-UA-Bitness, Sec-CH-UA-Platform, Sec-CH-UA-Full-Version, Viewport-Width, DPR, Device-Memory, RTT, Downlink, ECT # Строка указывающая на тип принимаемого контента 
Location: http://yandex.ru/showcaptcha?cc=1&mt=13F61346678342D966528E52A6466D4673C818A6A5768999896EAAB7835BD9EE51CEAE3C8F8D55F8E5FE3EC1084E8444A3526DABF0BDAD38F3299987DB110A90B484B573988E2D6F76E7B86F399708C808CBDBE1B4ED1D441E4D5EABD14242078DA0703BF72896A2AEA916CE8842CF&retpath=aHR0cDovL3lhbmRleC5ydS8__44e6f019dee6b85065dc15f78c1f5767&t=2/1694636013/423e5884d5f366ea92e05ef2054b9cf6&u=f8dbf222-49138c0b-901570f-9168253d&s=38b6fcba1ab2755a3e59a5d0dd7478ad
NEL: {"report_to": "network-errors", "max_age": 100, "success_fraction": 0.001, "failure_fraction": 0.1} #политика обработки ошибок сети, указывает, что отчеты об ошибках сети должны быть отправлены на указанный адрес URI в поле report_to
Report-To: { "group": "network-errors", "max_age": 100, "endpoints": [{"url": "https://dr.yandex.net/nel", "priority": 1}, {"url": "https://dr2.yandex.net/nel", "priority": 2}]} #объявляет группы конечных точек отчетности для веб-сайта разработчика.
Set-Cookie: spravka=dD0xNjYzMTAwMDEzO2k9MTc4LjE3Ni4yMTkuMjQ5O0Q9QkQ5N0U3OTM5RTE1Mjg4RDk2Q0Q0MEQwMjI4RjlERjVCNjFDNEQ4NzhDMTE1NDM4NEU5Q0FFREIyMEI0NkEzODE4RTA0OEFERDk3MzUwMzI7dT0xNjYzMTAwMDEzMDAzMjk2ODczO2g9MTUxNzE4MWVlYTc5ZGI4NjViYTlkMDY1ZjA0MzE0ZmI=; domain=.yandex.ru; path=/; expires=Fri, 13 Oct 2023 20:13:33 GMT
Set-Cookie: _yasc=Ljvzy5vdiF32/UaWY21viAZulnu5Sv4IRTtQIEJyboCN8TiWv+Q5L4bqrnr0ftHLRxA=; domain=.yandex.ru; path=/; expires=Sat, 10 Sep 2033 20:13:33 GMT; secure
X-Content-Type-Options: nosniff
X-Yandex-Captcha: captcha
X-Yandex-EU-Request: 0
X-Yandex-Req-Id: 1694636013003139-1518536894119326144-balancer-l7leveler-kubr-yp-sas-114-BAL_

HTTP/1.1 200 Ok
Accept-CH: Sec-CH-UA-Platform-Version, Sec-CH-UA-Mobile, Sec-CH-UA-Model, Sec-CH-UA, Sec-CH-UA-Full-Version-List, Sec-CH-UA-WoW64, Sec-CH-UA-Arch, Sec-CH-UA-Bitness, Sec-CH-UA-Platform, Sec-CH-UA-Full-Version, Viewport-Width, DPR, Device-Memory, RTT, Downlink, ECT
Access-Control-Allow-Origin: yastatic.net
Content-Length: 12888
Content-Type: text/html
NEL: {"report_to": "network-errors", "max_age": 100, "success_fraction": 0.001, "failure_fraction": 0.1}
Report-To: { "group": "network-errors", "max_age": 100, "endpoints": [{"url": "https://dr.yandex.net/nel", "priority": 1}, {"url": "https://dr2.yandex.net/nel", "priority": 2}]}
Set-Cookie: _yasc=txK9pX1rftOVHJfnWkrqcEOchS99JlhUSA5jnIvckGbdVFUY0VFe2ystI+ljVrrmemw=; domain=.yandex.ru; path=/; expires=Sat, 10 Sep 2033 20:13:33 GMT; secure
X-Content-Type-Options: nosniff
X-Yandex-Captcha: captcha
X-Yandex-EU-Request: 0
X-Yandex-Req-Id: 1694636013092032-867776299076290663-balancer-l7leveler-kubr-yp-sas-114-BAL_
```

### Python

Скрипт при помощи которого получил информацию о сайте  __[Python](https://www.python.org/)__:

`curl python.org -I -k -L -s`

Ответ:

```shell
HTTP/1.1 301 Moved Permanently
Connection: close
Content-Length: 0
Server: Varnish #заголовок Server указывает на программное обеспечение, используемое сервером. Здесь Varnish является сервером кеширования и/или балансировщиком нагрузки.
Retry-After: 0 #заголовок Retry-After используется сервером для указания клиенту времени ожидания перед повторным запросом. Значение 0 означает, что клиент может повторить запрос без задержки.
Accept-Ranges: bytes #заголовок Accept-Ranges указывает, что сервер поддерживает диапазоны байтов в запросах и может обрабатывать запросы на частичное содержимое
Date: Wed, 13 Sep 2023 20:19:57 GMT
Via: 1.1 varnish
X-Served-By: cache-fra-eddf8230059-FRA
X-Cache: HIT
X-Cache-Hits: 0
X-Timer: S1694636397.096770,VS0,VE0
Location: https://www.python.org/
Strict-Transport-Security: max-age=315360000; preload

HTTP/1.1 200 OK
Connection: keep-alive
Content-Length: 50558
Server: nginx
Content-Type: text/html; charset=utf-8
X-Frame-Options: SAMEORIGIN
Via: 1.1 vegur, 1.1 varnish, 1.1 varnish
Accept-Ranges: bytes
Date: Wed, 13 Sep 2023 20:19:57 GMT
Age: 2878
X-Served-By: cache-iad-kiad7000025-IAD, cache-fra-eddf8230069-FRA
X-Cache: HIT, HIT
X-Cache-Hits: 375, 20
X-Timer: S1694636398.749929,VS0,VE0
Vary: Cookie
Strict-Transport-Security: max-age=63072000; includeSubDomains; preload
```

### Git

Скрипт при помощи которого получил информацию о сайте  __[Git](https://git-scm.com/)__:

`curl git-scm.com -I -k -L -s`

Ответ:

```shell
HTTP/1.1 301 Moved Permanently
Date: Wed, 13 Sep 2023 20:21:15 GMT
Connection: keep-alive
Cache-Control: max-age=3600
Expires: Wed, 13 Sep 2023 21:21:15 GMT
Location: https://git-scm.com/
Server: cloudflare
CF-RAY: 80631872b8d54c8b-HEL #уникальный идентификатор запроса, который помогает Cloudflare обеспечить отслеживание и отладку запросов при возникновении проблем

HTTP/1.1 200 OK
Date: Wed, 13 Sep 2023 20:21:15 GMT
Content-Type: text/html; charset=utf-8
Connection: keep-alive
X-Frame-Options: SAMEORIGIN
X-Xss-Protection: 1; mode=block
X-Content-Type-Options: nosniff
X-Download-Options: noopen #это HTTP-заголовок безопасности, предназначенный для использования в браузерах на основе Internet Explorer и объясняет, как браузер должен обрабатывать файлы, предложенные для загрузки.
X-Permitted-Cross-Domain-Policies: none
Referrer-Policy: strict-origin-when-cross-origin
Cache-Control: public, max-age=14400
Etag: W/"db69273d9410cbf4536e9d4b3a59685d" #это аббревиатура для "Сущность-тег" и является заголовком HTTP-ответа, который позволяет клиенту получить информацию о версии ресурса на сервере. Это уникальный идентификатор
X-Request-Id: 5b655b2f-128f-4205-940e-13860b4aaf19
X-Runtime: 0.008824
Via: 1.1 vegur
CF-Cache-Status: REVALIDATED
Server: cloudflare
CF-RAY: 80631874dee9d957-HEL
```

### JetBrains

Скрипт при помощи которого получил информацию о сайте  __[JetBrains](https://www.jetbrains.com/)__:

`curl jetbrains.com -I -k -L -s`

Ответ: 

```shell
HTTP/1.1 301 Moved Permanently
Server: CloudFront
Date: Wed, 13 Sep 2023 20:21:40 GMT
Content-Type: text/html
Content-Length: 167
Connection: keep-alive
Location: https://jetbrains.com/
X-Cache: Redirect from cloudfront
Via: 1.1 4c0149793a766b424f3ddc1372e41924.cloudfront.net (CloudFront)
X-Amz-Cf-Pop: WAW51-P4 #Этот заголовок указывает на CloudFront Point of Presence (PoP), через который обрабатывается ваш запрос. Значение WAW51-P4 соответствует определенному PoP, обычно обозначающему географическое местонахождение
Alt-Svc: h3=":443"; ma=86400 #Этот заголовок определяет альтернативные сервисы для текущего ресурса 
X-Amz-Cf-Id: gpH8zvoyGBToakwvmKpiPOQtGeWGtpv9epljUm-ttf5i1-4STStCEg== #Этот заголовок используется Amazon Cloudfront для связывания ответа с определенной сессией и запросом, который он обрабатывал

HTTP/1.1 308 Found
Server: CloudFront
Date: Wed, 13 Sep 2023 20:21:40 GMT
Content-Length: 0
Connection: keep-alive
Location: https://www.jetbrains.com/
Strict-Transport-Security: max-age=31536000;
X-Cache: FunctionGeneratedResponse from cloudfront
Via: 1.1 9f886054ff6f095f177ce8fc0f0175ee.cloudfront.net (CloudFront)
X-Amz-Cf-Pop: WAW51-P4
Alt-Svc: h3=":443"; ma=86400
X-Amz-Cf-Id: zx9LhdFE68_tU8Vfl6DGIb346EvWf9cyqZThVFEFpx0cN00e4ocgvw==

HTTP/1.1 200 OK
Content-Type: text/html; charset=utf-8
Content-Length: 47213
Connection: keep-alive
Date: Wed, 13 Sep 2023 20:19:59 GMT
Server: nginx
X-Content-Type-Options: nosniff
Referrer-Policy: same-origin
Expires: Wed, 13 Sep 2023 20:19:59 GMT
Cache-Control: max-age=0
Pragma: no-cache #это HTTP заголовок запроса, используемый для указания, что промежуточные серверы (прокси или кеширование серверы) не должны кешировать этот конкретный запрос
X-Frame-Options: DENY
X-Content-Type-Options: nosniff
X-Xss-Protection: 1; mode=block
Strict-Transport-Security: max-age=31536000;
Vary: Accept-Encoding
Via: 1.1 9448fc1c48817eb327c6aba5fe8c8544.cloudfront.net (CloudFront)
Alt-Svc: h3=":443"; ma=86400
Age: 102 #это HTTP-заголовок ответа, который определяет время (в секундах), которое прошло с момента создания объекта ресурса на сервере-прокси или кеширующем сервере
Set-Cookie: cf_country-region=RU-KDA; Domain=jetbrains.com; Path=/; Secure
X-Cache: Hit from cloudfront
X-Amz-Cf-Pop: WAW51-P2
X-Amz-Cf-Id: 84o3_cTG33d-S9_j8Mct8OK47U_DTmhlLZIoyWUY1BuSItzck4Qn0g==
```

### VSC

Скрипт при помощи которого получил информацию о сайте  __[VSC](https://code.visualstudio.com/)__:

`curl code.visualstudio.com -I -k -L -s`

Ответ: 

```shell
HTTP/1.1 307 Temporary Redirect
Content-Length: 0
Location: https://code.visualstudio.com/
X-Azure-Ref: 08BkCZQAAAACVn/TQTWn+TZLfs6+lW/APU1RPRURHRTEzMTgAYmU4N2RjNmQtNDBmOS00NWIwLTg4MTAtOTkxMDg3ZWY4YjI5 #это пользовательский (нестандартный) HTTP-заголовок, используемый Microsoft Azure для обеспечения корреляции запросов в рамках своих сервисов. Значение этого заголовка представляет собой уникальный идентификатор
Date: Wed, 13 Sep 2023 20:22:08 GMT

HTTP/1.1 200 OK
Content-Length: 50213
Content-Type: text/html; charset=utf-8
Accept-Ranges: bytes
ETag: W/"c425-XBxswsHoV0dlJCAKuBbwZ9s5rjQ"
Strict-Transport-Security: max-age=31536000; includeSubDomains
Content-Security-Policy: frame-ancestors 'self'
X-Frame-Options: SAMEORIGIN
X-XSS-Protection: 1; mode=block
X-Content-Type-Options: nosniff
X-Content-Type-Options: nosniff
X-Powered-By: ASP.NET
x-azure-ref: 08RkCZQAAAAAPdmeqVmObTIBOV5v3JlcdU1RPRURHRTE0MjEAYmU4N2RjNmQtNDBmOS00NWIwLTg4MTAtOTkxMDg3ZWY4YjI5
X-Cache: CONFIG_NOCACHE
Date: Wed, 13 Sep 2023 20:22:08 GMT
```
