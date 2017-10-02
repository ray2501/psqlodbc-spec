# psqlodbc-spec
openSUSE RPM spec for psqlODBC (PostgreSQL ODBC driver)

下載的檔案來自於 [psqlODBC - PostgreSQL ODBC driver](https://odbc.postgresql.org/). 安裝以後的設定，
可以參考 [unixODBC without the GUI](http://www.unixodbc.org/odbcinst.html).

接下來參考的設定範例，首先是 odbcinst.ini 的內容： 

    [PostgreSQL] 
    Description     = PostgreSQL driver
    Driver          = psqlodbcw.so
    FileUsage       = 1

再來是 odbc.ini， 

    [PostgreSQL]
    Description         = PostgreSQL
    Driver              = PostgreSQL
    Trace               = No
    TraceFile           = 
    Database            = postgres
    Servername          = localhost
    UserName            = postgres
    Password            = postgres
    Port                = 5432
    Protocol            = 7.4
    ReadOnly            = No
    RowVersioning       = No
    ShowSystemTables    = No
    ShowOidColumn       = No
    FakeOidIndex        = No
    ConnSettings        =

測試的 Tcl script： 

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
