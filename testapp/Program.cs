using System;
using System.Data.Odbc;

namespace testapp
{
    class Program
    {
        static void Main(string[] args)
        {
            string connectionString = "DSN=PostgreSQL; UID=postgres; PWD=postgres;";
            string sql = "SELECT VERSION()";

            using (var conn= new OdbcConnection(connectionString)) {
                conn.Open();
                OdbcCommand comm = new OdbcCommand(sql, conn);
                OdbcDataReader dr = comm.ExecuteReader();
                while (dr.Read()) {
                    Console.WriteLine(dr.GetValue(0).ToString());
                }
            }
        }
    }
}
