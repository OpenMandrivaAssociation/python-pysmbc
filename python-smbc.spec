%define module smbc
%define name python-%{module}
%define oname pysmbc
%define version 1.0.10
%define release %mkrel 3
    
Name:    %{name}
Summary: Python bindings for the libsmbclient API from Samba
Version: %{version}
Release: %{release}
Group:   Development/Python
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
URL: http://cyberelk.net/tim/data/pysmbc/
Source0:       %oname-%version.tar.bz2 
BuildRequires: libsmbclient-devel
License: BSD
%py_requires -d
   
%description
Python bindings for the libsmbclient API, known as pysmbc. It was written
for use with system-config-printer, but can be put to other uses as well.

%prep
%setup -q -n %{oname}-%version
 
%build
%__python setup.py build
  
%install
%__rm -rf %{buildroot}
  
%__python setup.py install --root=%{buildroot}
  
%clean
%__rm -rf %{buildroot}
   
%files
%defattr(-,root,root)
%python_sitearch/*.egg-info
%python_sitearch/smbc.so


%changelog
* Thu May 05 2011 Oden Eriksson <oeriksson@mandriva.com> 1.0.10-2mdv2011.0
+ Revision: 668035
- mass rebuild

* Mon Nov 29 2010 Guillaume Rousse <guillomovitch@mandriva.org> 1.0.10-1mdv2011.0
+ Revision: 603075
- update to new version 1.0.10

* Sun Oct 31 2010 Andrey Borzenkov <arvidjaar@mandriva.org> 1.0.6-3mdv2011.0
+ Revision: 590767
- rebuild for new python 2.7

* Sun Jun 06 2010 Colin Guthrie <cguthrie@mandriva.org> 1.0.6-2mdv2010.1
+ Revision: 547157
- Bump release to ensure version is > 2010.0 update version

  + Nicolas Lécureuil <nlecureuil@mandriva.com>
    - Use description for the package in 2010.0

* Fri Feb 19 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 1.0.6-1mdv2010.1
+ Revision: 508398
- import python-smbc


