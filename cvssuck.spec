%define		subver	20060124
Summary:	Inefficient cvs repository grabber using cvs command
Name:		cvssuck
Version:	0.3
Release:	1
License:	BSD
Group:		Applications
Source0:	ftp://ftp.debian.org/debian/pool/main/c/cvssuck/%{name}_%{version}.cvs%{subver}.orig.tar.gz
# Source0-md5:	87fceb81f6ea11d8582413a5a1fd965a
URL:		http://cvs.m17n.org/~akr/cvssuck/
BuildRequires:	rpmbuild(macros) >= 1.484
Requires:	cvs-client
Requires:	rcs
Requires:	ruby
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
CVSsuck is a mirroring tool for CVS repositories. Unlike other tools
such as CVSup or rsync, it uses cvs command to access the repository.
So, it works well with remote repositories without a special server or
shell account. However it is inefficient and not perfect because CVS
client/server protocol is not designed for mirroring. If a server
provides special way to grab a repository, you shouldn't use CVSsuck.

%prep
%setup -q -n %{name}-%{version}.cvs%{subver}
%{__sed} -i -e '1s,^#!.*ruby,#!%{__ruby},' cvssuck

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}
install -p cvssuck $RPM_BUILD_ROOT%{_bindir}
cp -a cvssuck.1 $RPM_BUILD_ROOT%{_mandir}/man1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README* NEWS ChangeLog
%attr(755,root,root) %{_bindir}/cvssuck
%{_mandir}/man1/cvssuck.1*
