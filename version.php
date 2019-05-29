#!/usr/bin/env php
<?php
    $host = 'localhost';
    $port = 5432;
    $dbname = 'postgres';
    $user = 'postgres';
    $passwd = 'postgres';

    try {
        $dbConn = new PDO('odbc:Driver=PostgreSQL;Server=' . $host . 
                              ';Port=' . $port . 
                              ';Database=' . $dbname . 
                              ';UID=' . $user . 
                              ';PWD=' . $passwd . ';clientcharset=UTF-8');
    } catch (PDOException $e){
        echo $e->getMessage();
    }

    $stmt = $dbConn->query('SELECT VERSION() as version');

    $row = $stmt->fetch(PDO::FETCH_ASSOC);
    foreach ($row as $r) {
        echo $r;
    }
?>   
