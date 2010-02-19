%define module smbc
%define name python-%{module}
%define oname pysmbc
%define version 1.0.6
%define release %mkrel 1
    
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
Python bindings for the libsmbclient API from Samba

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
