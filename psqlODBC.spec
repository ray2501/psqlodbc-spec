#
# spec file for package psqlODBC
#

%{!?directory:%define directory /usr}

%define buildroot %{_tmppath}/%{name}
%define tarname psqlodbc

Name:          psqlODBC
Summary:       ODBC Driver for PostgreSQL
Version:       12.02.0000
Release:       0
License:       LGPL-2.1+
Group:         Productivity/Databases/Tools
Source:        https://ftp.postgresql.org/pub/odbc/versions/src/%tarname-%{version}.tar.gz
URL:           https://odbc.postgresql.org/
PreReq:         /usr/bin/odbcinst
BuildRequires: autoconf
BuildRequires: automake
BuildRequires: openssl-devel
BuildRequires: postgresql-devel
#BuildRequires: postgresql-server-devel
BuildRequires: unixODBC-devel
BuildRoot:     %{buildroot}
Requires: unixODBC
Requires: postgresql

%description
This package contains the ODBC (Open DataBase Connectivity) driver and
sample configuration files needed for applications to access a
PostgreSQL database using ODBC.

%prep
%setup -q -n %{tarname}-%{version}

%build
./configure --prefix=%{directory} --libdir=%{directory}/%{_lib} --with-unixodbc --with-libpq
make 

%install
make DESTDIR=%{buildroot} install
rm -f %buildroot%_libdir/*.la

%post
if [ -x %{_bindir}/odbcinst ] ; then
   INST=/tmp/postgresqlinst$$
   if [ -r %{_libdir}/psqlodbcw.so ] ; then
      cat > $INST << 'EOD'
[PostgreSQL]
Description=PostgreSQL ODBC driver
Driver=%{_libdir}/psqlodbcw.so
FileUsage=1
EOD
      %{_bindir}/odbcinst -q -d -n PostgreSQL | grep '^\[PostgreSQL\]' >/dev/null || {
	 %{_bindir}/odbcinst -i -d -n PostgreSQL -f $INST || true
      }
      cat > $INST << 'EOD'
[PostgreSQL]
Description         =PostgreSQL
Driver              =PostgreSQL
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
EOD
      %{_bindir}/odbcinst -q -s -n "PostgreSQL" | \
	 grep '^\[PostgreSQL\]' >/dev/null || {
	 %{_bindir}/odbcinst -i -l -s -n "PostgreSQL" -f $INST || true
      }
   fi
   rm -f $INST || true
fi

%preun
if [ "$1" = "0" ] ; then
    test -x %{_bindir}/odbcinst && {
	%{_bindir}/odbcinst -u -d -n PostgreSQL || true
	%{_bindir}/odbcinst -u -l -s -n "PostgreSQL" || true
    }
    true
fi

%postun
/sbin/ldconfig

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%{directory}/%{_lib}
