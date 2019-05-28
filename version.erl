#!/usr/bin/env escript
-mode(compile).
-export([main/1]).

main(_) ->
   odbc:start(),
   {ok, Ref} = odbc:connect("DSN=PostgreSQL; UID=postgres; PWD=postgres;", []),
   {selected, Columnnames, Rows} = odbc:sql_query(Ref, "SELECT VERSION()"),
   io:format("~s:~n", [lists:nth(1, Columnnames)]),
   lists:foreach(fun(X) -> io:format("~s~n", [tuple_to_list(X)]) end, Rows),
   odbc:disconnect(Ref).
