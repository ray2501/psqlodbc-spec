/*
 * Qt SQL test for PostgreSQL ODBC driver
 */

#include <QTextStream>
#include <QtSql>

int main()
{
    QTextStream out(stdout);

    QString connectString = QStringLiteral(
        "Driver=/usr/lib64/psqlodbcw.so;"
        "Database=danilo;"
        "UID=danilo;"
        "PWD=danilo;");

    QSqlDatabase db = QSqlDatabase::addDatabase("QODBC3");
    db.setDatabaseName(connectString);
    if (db.open()) {
        QSqlQuery query("SELECT VERSION()");
        query.setForwardOnly(true);
        
        while (query.next()) {
            QString version = query.value(0).toString();
            out << "Postgresql: " << version << endl;
        }      
    } else {
        out << "Connection failed!!!" << endl;
        return 1;
    }

    return 0;
}

