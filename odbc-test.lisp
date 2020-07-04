#!/usr/bin/ecl --shell
(require "asdf")
(require "plain-odbc")

;; DSN=PostgreSQL
(setf *con* (plain-odbc:connect "PostgreSQL" "postgres" "postgres"))
(setf result (plain-odbc:exec-query *con* "select VERSION() as version"))
(write-line (caar result))
(plain-odbc:close-connection *con*)
