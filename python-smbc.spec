%define module smbc
%define oname py%{module}

Summary:	Python bindings for the libsmbclient API from Samba
Name:		python-%{module}
Version:	1.0.13
Release:	2
Group:		Development/Python
License:	BSD
Url:		http://cyberelk.net/tim/data/pysmbc/
Source0:	http://cyberelk.net/tim/data/pysmbc/%{oname}-%{version}.tar.bz2
Patch0:		pysmbc-1.0.13_samba-4.0_libsmbclient_h.patch
BuildRequires:	pkgconfig(smbclient)
%py_requires -d
   
%description
Python bindings for the libsmbclient API, known as pysmbc. It was written
for use with system-config-printer, but can be put to other uses as well.

%prep
%setup -qn %{oname}-%{version}
%apply_patches

%build
%__python setup.py build

%install
%__python setup.py install --root=%{buildroot}

%files
%python_sitearch/*.egg-info
%python_sitearch/smbc.so

