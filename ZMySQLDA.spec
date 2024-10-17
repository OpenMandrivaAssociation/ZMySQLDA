Name:               ZMySQLDA
Summary:            A Zope connector to Mysql
Version:            2.0.9b2
Release:            4mdk
Group:              Development/Python
Requires:           zope MySQL-python
License:            GPL
URL:                https://www.erp5.org
Packager:           Sebastien Robin <seb@nexedi.com>
BuildRoot:          %{_tmppath}/%{name}-%{version}-rootdir
Buildarch:	noarch

Source: %{name}-%{version}.tar.bz2
Patch1: ZMySQLDA-2.0.9b2_with_MySQL-python-0.9.0.patch

#----------------------------------------------------------------------
%description
ZMySQLDA allows to quickly connect to Mysql with Zope.

http://www.erp5.org

#----------------------------------------------------------------------
%prep

rm -rf $RPM_BUILD_ROOT
mkdir $RPM_BUILD_ROOT
%setup -a 0
%patch1 -p1

#----------------------------------------------------------------------
%build

#----------------------------------------------------------------------
%install

install -d $RPM_BUILD_ROOT%{_libdir}/zope/lib/python/Products/%{name}
install *.py $RPM_BUILD_ROOT%{_libdir}/zope/lib/python/Products/%{name}
install *.txt $RPM_BUILD_ROOT%{_libdir}/zope/lib/python/Products/%{name}
install *.dtml $RPM_BUILD_ROOT%{_libdir}/zope/lib/python/Products/%{name}

install -d $RPM_BUILD_ROOT%{_libdir}/zope/lib/python/Products/%{name}/help
install help/*.py $RPM_BUILD_ROOT%{_libdir}/zope/lib/python/Products/%{name}/help

install -d $RPM_BUILD_ROOT%{_libdir}/zope/lib/python/Products/%{name}/icons
install icons/*.gif $RPM_BUILD_ROOT%{_libdir}/zope/lib/python/Products/%{name}/icons

%clean
rm -rf $RPM_BUILD_ROOT

#----------------------------------------------------------------------
%files
%defattr(-,root,root,0755)
%doc CHANGES.txt DEPENDENCIES.txt README.txt VERSION.txt

%{_libdir}/zope/lib/python/Products/%{name}/

#----------------------------------------------------------------------
