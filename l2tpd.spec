Summary:	Layer two tunelling protocol daemon
Name:		l2tpd
Version:	0.69
Release:	0.1
License:	GPL
Group:		Networking/Daemons
Source0:	%{name}-%{version}.tar.gz
# Source0-md5:	c5dba6b80f583070fe9e6ed6e0c2162e
Patch0:		%{name}-fix.patch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
empty

%prep
%setup -q
%patch0 -p1

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_sbindir}
install l2tpd $RPM_BUILD_ROOT%{_sbindir}

%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(644,root,root,755)
%doc CREDITS README TODO
%attr(755,root,root) %{_sbindir}/*
