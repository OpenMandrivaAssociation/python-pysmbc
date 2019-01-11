%define module smbc
%define oname py%{module}

Summary:	Python bindings for the libsmbclient API from Samba
Name:		python-%{module}
Version:	1.0.15.8
Release:	1
Group:		Development/Python
License:	BSD
Url:		http://cyberelk.net/tim/data/pysmbc/
Source0:	http://pypi.io/packages/source/p/pysmbc/pysmbc-%{version}.tar.bz2
Patch0:		pysmbc-1.0.13_samba-4.0_libsmbclient_h.patch
BuildRequires:	pkgconfig(smbclient)
BuildRequires:  pkgconfig(python2)

%description
Python bindings for the libsmbclient API, known as pysmbc. It was written
for use with system-config-printer, but can be put to other uses as well.

%prep
%setup -qn %{oname}-%{version}
%apply_patches

%build
python2 setup.py build build_ext

%install
python2 setup.py install --root=%{buildroot}

%files
%py2_platsitedir/*.egg-info
%py2_platsitedir/smbc.so
