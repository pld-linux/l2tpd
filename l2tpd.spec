Summary:	Layer two tunelling protocol daemon
Summary(pl):	Demon tuneluj�cy protoko�y warstwy drugiej
Name:		l2tpd
Version:	0.69
Release:	0.1
License:	GPL
Group:		Networking/Daemons
Source0:	http://www.l2tpd.org/downloads/%{name}-%{version}.tar.gz
# Source0-md5:	c5dba6b80f583070fe9e6ed6e0c2162e
Patch0:		%{name}-fix.patch
URL:		http://www.l2tpd.org/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A Layer 2 Tunneling Protocol VPN daemon for Linux and other
POSIX-bases OSs.

%description -l pl
Demon VPN tuneluj�cy protoko�y warstwy drugiej dla Linuksa i innych
system�w opartych na POSIX.

%prep
%setup -q
%patch0 -p1

%build
%{__make} \
	CC="%{__cc}" \
	DFLAGS="%{rpmcflags} -DDEBUG_PPPD -DDEBUG_CONTROL -DDEBUG_ENTROPY"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_sbindir}

install l2tpd $RPM_BUILD_ROOT%{_sbindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CREDITS README TODO
%attr(755,root,root) %{_sbindir}/*
