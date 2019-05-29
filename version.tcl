#!/usr/bin/env tclsh

package require tdbc::odbc

set connStr "DSN=PostgreSQL; UID=postgres; PWD=postgres;"
tdbc::odbc::connection create db $connStr

set statement [db prepare {
    SELECT VERSION()
}]

$statement foreach row {
    puts [dict get $row version]
}

$statement close
db close
