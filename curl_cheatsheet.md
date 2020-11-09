# CURL

> Nota: Si encuentras errores o tienes más opciones dímelas :D<p>
> Última actualización:09-11-2020 fuck year

## Usando curl con patrones

    $ curl http://www.{taget1,target2}.edu 
    $ curl ftp://ftp.target.edu/dump[001-100].txt

## Salida a fichero

    $ curl -o “file_#1.txt” http://www.{target1,target2}.edu
    
## Usando proxies
    $ curl --socks5 torproxy:9050 http://target/
    $ curl -x socks4a://localhost:9050 target

## Envio fichero, upload

    $ curl -F file=@“file.txt" http://target/file/upload/

## Estableciendo dns

    $ curl --dns-ipv4-addr 172.16.0.20 http://target
    $ curl --dns-interface eth1 http://target
resolver un host con una dirección IP específica

    $ curl --resolve target:80:172.16.0.20 http://target
## Http headers

    $ curl --header "X-Application: BotClient" http://target/
    $ curl --referer http://www.domain.com/login.php http://target
   Si has almacenado las cookies de sesión con la opción **--cookie-jar** puede ser útil no usar las cookies de sesión.
   

    $ curl --cookie cookies.txt --junk-session-cookies http://target
   
   ## Encadenando peticiones
   

    $ curl target --next -d $data_to_post target

## Traza de la petición

    $ curl --trace - https://target
   
  eliminar el dump hexadecimal con la opción **--trace-ascii**
 
## Dejando logs

    $ curl --silent --write-out "Response code: %{http_code}\nTotal time: %{time_total}" https://target
  recuerda poner **--silent | -s** para no ensuciar el log

## Referencias
* https://isc.sans.edu/forums/diary/Exploiting+the+Power+of+Curl/23934/
