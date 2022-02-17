<?php
$json = file_get_contents('config.json');
$jsonArray = json_decode($json, true);
$name = $jsonArray["Фамилия"];
$name1 = $jsonArray["Имя"];
$name2 = $jsonArray["Отчество"];
$date =  $jsonArray["DR"];
#echo($jsonArray["Имя"]);
?>